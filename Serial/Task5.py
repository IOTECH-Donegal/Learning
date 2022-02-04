import serial
import sys

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

try:
    with open("zEx05.kml", "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<kml xmlns="http://earth.google.com/kml/2.0">\n')
        f.write('<Document>\n')
        with serial.Serial("COM6") as s:
            s.baudrate = 4800
            s.bytesize = serial.EIGHTBITS
            s.parity = serial.PARITY_NONE
            s.stopbits = serial.STOPBITS_ONE
            s.timeout = None

            while True:
                nmea = s.readline()
                nmea = nmea.strip().decode()
                if nmea == 'EOT':
                    break

                if nmea[3:6] == 'GGA':
                    lat, lon, sats = gga_ds(nmea)
                    f.write('<Placemark>\n')
                    f.write(f'<name>{sats}</name>\n')
                    f.write('<Point>\n')
                    f.write(f'<coordinates>{lon:.6f},{lat:.6f},0.0</coordinates>\n')
                    f.write('</Point>\n')
                    f.write('</Placemark>\n')

                    print(lat, lon)

        f.write('</Document>\n')
        f.write('</kml>\n')

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