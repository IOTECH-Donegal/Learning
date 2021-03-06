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
    return latitude, longitude

try:
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
                lat, lon = gga_ds(nmea)
                print(lat, lon)

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