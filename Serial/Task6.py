import serial
import sys
import math
import datetime

def gga_ds(nmea):
    gga = nmea.split(',')
    if int(gga[6]) > 0:
        latitude = float(gga[2][:2]) + float(gga[2][2:]) / 60
        if gga[3] == 'S':
            latitude = -latitude
        longitude = float(gga[4][:3]) + float(gga[4][3:]) / 60
        if gga[5] == 'W':
            longitude = -longitude
        num_sats = int(gga[7])
    return latitude, longitude, num_sats

def rmc_ds(nmea):
    # $GPRMC,231211.00,A,2806.773465,N,01520.023184,W,011.4,103.5,031217,,,A
    rmc = nmea.split(',')
    if rmc[2] == 'A':
        latitude = float(rmc[3][:2]) + float(rmc[3][2:]) / 60
        if rmc[4] == 'S':
            latitude = -latitude
        longitude = float(rmc[5][:3]) + float(rmc[5][3:]) / 60
        if rmc[6] == 'W':
            longitude = -longitude
        speed = float(rmc[7])
        heading = float(rmc[8])
        hour, minute, second = int(rmc[1][:2]), int(rmc[1][2:4]), int(rmc[1][4:6])
        day, month, year = int(rmc[9][:2]), int(rmc[9][2:4]), 2000+int(rmc[9][4:])
        dt = datetime.datetime(year, month, day, hour, minute, second)

    return latitude, longitude, dt, heading, speed


def distance(lon1, lat1, lon2, lat2):
    lat = (lat1 + lat2) / 2 * math.pi / 180
    dx = 111.3 * math.cos(lat) * (lon1 - lon2)
    dy = 111.3 * (lat1 - lat2)
    return math.sqrt(dx**2 + dy**2)


try:
    with serial.Serial("COM6") as s:
        s.baudrate = 4800
        s.bytesize = serial.EIGHTBITS
        s.parity = serial.PARITY_NONE
        s.stopbits = serial.STOPBITS_ONE
        s.timeout = None

        lat_prev = 0
        lon_prev = 0

        dt_prev = 0
        dt_sum = 0

        dist = 0

        while True:
            nmea = s.readline()
            nmea = nmea.strip().decode()
            if nmea == 'EOT':
                break

            if nmea[3:6] == 'RMC':
                latitude, longitude, dt, heading, speed = rmc_ds(nmea)
                print(latitude, longitude, dt, heading, speed)

                if lat_prev != 0 and lon_prev !=0:
                    dist += distance(lon_prev, lat_prev, longitude, latitude)
                    dt_sum += (dt - dt_prev).total_seconds()


                lon_prev = longitude
                lat_prev = latitude
                dt_prev = dt

                print(f"{dist:.3f} km")
                print(f"{datetime.timedelta(seconds=dt_sum)}")


except serial.SerialException as err:
    print("Serial Port Error: \n" + str(err))
    sys.exit()
except KeyboardInterrupt:
    print("Keyboard break")
    sys.exit()
except Exception as err:
    print("An error has occurred!")
    print(err)
    sys.exit()

print("Session regularly closed!")