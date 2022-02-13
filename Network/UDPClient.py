import socket
UDP_IP = '192.168.5.230'
UDP_PORT = 23
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    message = input("Message: (terminate server = EXIT) ")
    s.sendto(message.encode(), (UDP_IP, UDP_PORT) )