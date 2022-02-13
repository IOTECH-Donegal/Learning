'''
TCPServer by: JOR
Listens for packets on a particular address and port.

Alpha: 13FEB22
'''

import socket
import settings.tcp as settings

TCP_IP = settings.TCP["SERVER_TCP_IPv4"]
TCP_PORT = settings.TCP["SERVER_PORT"]
BUFFER_SIZE = 1024

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #1
        s.bind( ( TCP_IP, TCP_PORT ) ) #2
        print(f'Bound to {TCP_IP}:{TCP_PORT}')
        print('Send EXIT to terminate the server.')
        while True:
            s.listen(1)
            conn, addr = s.accept()
            print(f'Connection address: {addr}')
            data = conn.recv(BUFFER_SIZE).decode()
            print(data)
            if data == 'EXIT':
                break
            conn.send(data.encode())
except socket.error as e:
    print(f'Error: {e}')

    print("Connection closed!")
