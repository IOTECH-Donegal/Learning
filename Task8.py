import serial
import sys
import datetime
import matplotlib.pyplot as plt

def rmc_ds(nmea):
    valid, latitude, longitude, dt, heading, speed = False, 0, 0, None, None, None
    # $GPRMC,231211.00,A,2806.773465,N,01520.023184,W,011.4,103.5,031217,,,A
    rmc = nmea.split(',')
    if rmc[2] == 'A':
        valid = True
        latitude = float(rmc[3][:2]) + float(rmc[3][2:]) / 60
        if rmc[4] == 'S':
            latitude = -latitude
        longitude = float(rmc[5][:3]) + float(rmc[5][3:]) / 60
        if rmc[6] == 'W':
            longitude = -longitude
        speed = float(rmc[7]) if rmc[7] != "" else 0.0
        heading = float(rmc[8]) if rmc[8] != "" else 0.0
        hour, minute, second = int(rmc[1][:2]), int(rmc[1][2:4]), int(rmc[1][4:6])
        day, month, year = int(rmc[9][:2]), int(rmc[9][2:4]), 2000+int(rmc[9][4:])
        dt = datetime.datetime(year, month, day, hour, minute, second)

    return valid, latitude, longitude, dt, heading, speed

def timediff(dt1, dt2):
    dt = dt2 - dt1
    return(dt.total_seconds())

try:
    with serial.Serial("COM6") as s:
        s.baudrate = 4800
        s.bytesize = serial.EIGHTBITS
        s.parity = serial.PARITY_NONE
        s.stopbits = serial.STOPBITS_ONE
        s.timeout = None

        dt_prev = None
        dt_sum = 0
        x = []
        y = []
        while True:
            nmea = s.readline()
            nmea = nmea.strip().decode()
            if nmea == 'EOT':
                break
            if nmea[3:6] == 'RMC':
                valid, latitude, longitude, dt, heading, speed = rmc_ds(nmea)
                rmc = nmea.split(',')
                if valid:
                    if dt_prev is not None:
                        dt_sum += timediff(dt_prev, dt)
                    dt_prev = dt
                    speed = speed * 1.852
                    x.append(dt)
                    y.append(speed)
                    print(f'{dt} - {speed:.1f} km/h')

        plt.plot(x, y, 'ro')
        plt.show()

except serial.SerialException as err:
    print("Serial Port Error:\n" + str(err))
    sys.exit()
except KeyboardInterrupt:
    print("Keyboard break")
    sys.exit()
except Exception as err:
    print("An error has occurred!")
    print(err)
    sys.exit()

print("Session regularly closed!")