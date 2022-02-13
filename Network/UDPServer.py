'''
UDPServer by: JOR
Listens for packets on a particular address and port.

Alpha: 13FEB22
'''

import socket
import settings.udp as settings

UDP_IP = settings.UDP["SERVER_UDP_IPv4"]
UDP_PORT = settings.UDP["SERVER_PORT"]
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.bind( (UDP_IP, UDP_PORT) )
    print('Listening on', UDP_IP)
    print('Send EXIT to terminate the server!')
    while True:
        data, addr = s.recvfrom(BUFFER_SIZE)
        data = data.decode()
        print(addr, data)
        if data == 'EXIT':
            break
print("Connection closed!")
