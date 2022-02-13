import socket
UDP_IP = '0.0.0.0'
UDP_PORT = 8129
BUFFER_SIZE = 1024
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: #1
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) #2
    s.bind( (UDP_IP, UDP_PORT) ) #3
    print('Listening on', UDP_IP)
    print('Send EXIT to terminate the server!')
    while True:
        data, addr = s.recvfrom(BUFFER_SIZE) #4
        data = data.decode()
        print(addr, data)
        if data == 'EXIT':
            break
print("Connection closed!")
