import socket

def create_server_socket(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    return server_socket

def accept_client_connection(server_socket):
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")
    return client_socket, client_address

def main():
    host = '127.0.0.1'
    port = 65432

    server_socket = create_server_socket(host, port)
    
    while True:
        client_socket, client_address = accept_client_connection(server_socket)
        client_socket.sendall(b'Hello, client!')
        client_socket.close()

if __name__ == "__main__":
    main()