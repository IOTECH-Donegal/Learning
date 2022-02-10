import socket
TCP_IP = '192.168.5.173'
TCP_PORT = 12345
BUFFER_SIZE = 1024
message = input('Message: ')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect( (TCP_IP, TCP_PORT) )
    #s.send(message.encode())
    data = s.recv(BUFFER_SIZE)
    print('received data:', data)