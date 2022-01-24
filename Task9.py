import serial
import sys

def nmea_checksum_calculator(nmea):
    checksum = nmea[-2:]
    nmea = nmea.strip()[1:-3]
    sum = 0
    for c in nmea:
        sum = sum ^ ord(c)
    return f'{sum:02X}' == checksum


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
            if nmea_checksum_calculator(nmea):
                print(nmea)
            else:
                print("Checksum Error")

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