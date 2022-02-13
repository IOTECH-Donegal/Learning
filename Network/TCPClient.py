'''
TCPClient by: JOR
Send TCP packets to a particular address and port.

Alpha: 13FEB22
'''

import socket
import time
from datetime import datetime
import settings.tcp as settings

TCP_IP = settings.TCP["SERVER_TCP_IPv4"]
TCP_PORT = settings.TCP["SERVER_PORT"]

BUFFER_SIZE = 1024
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        message_text = f"IOTECH {datetime.now()}"
        message = message_text.encode('utf-8')
        s.connect( (TCP_IP, TCP_PORT) )
        s.send(message)
        data = s.recv(BUFFER_SIZE)
        print('Server echoed:', data)
        time.sleep(1)