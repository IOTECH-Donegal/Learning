import serial
from settings import loopback

test_string = "IOTEST".encode('utf-8')
port_list = loopback.PORTS
#port_list = ['/dev/ttyS0', '/dev/ttyAMA1', '/dev/ttyAMA2', '/dev/ttyAMA3', '/dev/ttyAMA4']

for port in port_list:

    try:
        serialPort = serial.Serial(port, 9600, timeout = 2)
        serialPort.flushInput()
        serialPort.flushOutput()
        print("Opened port", port, "for testing:")
        bytes_sent = serialPort.write(test_string)
        print ("Sent", bytes_sent, "bytes")
        loopback = serialPort.read(bytes_sent)
        if loopback == test_string:
            print ("Received", len(loopback), "valid bytes, Serial port", port, "working \n")
        else:
            print ("Received incorrect data", loopback, "over Serial port", port, "loopback\n")
        serialPort.close()
    except IOError:
        print ("Failed at", port, "\n")
