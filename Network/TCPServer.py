import socket
TCP_IP = '0.0.0.0'
TCP_PORT = 23
BUFFER_SIZE = 1024

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #1
        s.bind( ( TCP_IP, TCP_PORT ) ) #2
        print(f'bind to {TCP_IP}:{TCP_PORT}')
        print('Send EXIT to terminate the server!')
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
