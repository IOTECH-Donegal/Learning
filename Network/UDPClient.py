import socket
UDP_IP = '255.255.255.255'
UDP_PORT = 8129
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    message = input("Message: (terminate server = EXIT) ")
    s.sendto(message.encode(), (UDP_IP, UDP_PORT) )