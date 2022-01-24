import serial
import sys
import math
import datetime


def rmc_ds(nmea):
    latitude, longitude, dt, heading, speed = 0, 0, None, None, None
    # $GPRMC,231211.00,A,2806.773465,N,01520.023184,W,011.4,103.5,031217,,,A
    rmc = nmea.split(',')
    if rmc[2] == 'A':
        latitude = float(rmc[3][:2]) + float(rmc[3][2:]) / 60
        if rmc[4] == 'S':
            latitude = -latitude
        longitude = float(rmc[5][:3]) + float(rmc[5][3:]) / 60
        if rmc[6] == 'W':
            longitude = -longitude
        speed = float(rmc[7]) if rmc[7] != "" else None
        heading = float(rmc[8]) if rmc[8] != "" else None
        hour, minute, second = int(rmc[1][:2]), int(rmc[1][2:4]), int(rmc[1][4:6])
        day, month, year = int(rmc[9][:2]), int(rmc[9][2:4]), 2000+int(rmc[9][4:])
        dt = datetime.datetime(year, month, day, hour, minute, second)

    return latitude, longitude, dt, heading, speed


def distance(lon1, lat1, lon2, lat2):
    lat = (lat1 + lat2) / 2 * math.pi / 180
    dx = 111.3 * math.cos(lat) * (lon1 - lon2)
    dy = 111.3 * (lat1 - lat2)
    return math.sqrt(dx + dy)

try:
    with serial.Serial("COM6") as s:
        s.baudrate = 4800
        s.bytesize = serial.EIGHTBITS
        s.parity = serial.PARITY_NONE
        s.stopbits = serial.STOPBITS_ONE
        s.timeout = None


    lat_prev = 0
    lon_prev = 0

    cnt = 0

    with open('zEx07.kml', 'w') as kmlFile:
        # https://developers.google.com/kml/
        kmlFile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        kmlFile.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
        kmlFile.write('<Document>\n')
        kmlFile.write('<Placemark>\n')
        kmlFile.write('<Style>\n')
        kmlFile.write('<LineStyle>\n')
        kmlFile.write('<color>FFCC0000</color>\n')
        # aabbggrr (4 bytes, 0x00-0xFF or 0-255)
        # a = alpha channel (for representing the transparency)
        # b, g, r = blue, green, red
        kmlFile.write('<width>5</width>\n')
        kmlFile.write('</LineStyle>\n')
        kmlFile.write('</Style>\n')
        kmlFile.write('<LineString>\n')
        kmlFile.write('<coordinates>\n')

        while True:
            nmea = s.readline()
            nmea = nmea.strip().decode()
            if nmea == 'EOT':
                break

            if nmea[3:6] == 'RMC':
                latitude, longitude, dt, heading, speed = rmc_ds(nmea)

                if latitude != 0 and lat_prev != 0 and lon_prev != 0:
                    dist = distance(lon_prev, lat_prev, longitude, latitude)*1000
                    print(latitude, longitude, dt, heading, speed, dist)
                    if dist > 5:
                        kmlFile.write(f'{longitude:.6f},{latitude:.6f},0 \n')
                        print(f'{cnt:05d}: {longitude:.5f}, {latitude:.5f}')
                        cnt += 1

                lon_prev = longitude
                lat_prev = latitude

        kmlFile.write('</coordinates></LineString></Placemark>\n')
        kmlFile.write('</Document></kml>\n')



except serial.SerialException as err:
    print("Serial Port Error: \n" + str(err))
    sys.exit()
except KeyboardInterrupt:
    print("Keyboard break")
    sys.exit()


print("Session regularly closed!")