'''
UDPClient by: JOR
Send UDP packets to a particular address and port.

Alpha: 13FEB22
'''


import socket
import settings.udp as settings

UDP_IP = settings.UDP["CLIENT_UDP_IPv4"]
UDP_PORT = settings.UDP["SERVER_PORT"]

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    message = input("Message: (terminate server = EXIT) ")
    s.sendto(message.encode(), (UDP_IP, UDP_PORT) )