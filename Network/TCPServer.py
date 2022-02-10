import socket
TCP_IP = '0.0.0.0'
TCP_PORT = 8128
BUFFER_SIZE = 1024

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #1
        s.bind( ( TCP_IP, TCP_PORT ) ) #2
        print(f'bind to {TCP_IP}:{TCP_PORT}')
        print('Send EXIT to terminate the server!')
        while True:
            s.listen(1) #3
            conn, addr = s.accept() #4
            print(f'Connection address: {addr}')
            data = conn.recv(BUFFER_SIZE).decode() #5
            print(data)
            if data == 'EXIT':
                break
            conn.send(data.encode()) #6
except socket.error as e:
    print(f'Error: {e}')

    print("Connection closed!")
