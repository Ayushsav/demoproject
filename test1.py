import socket

def code_sync_demo():
    print("This is a demo of code synchronization.")
    print("Code synchronization ensures that changes in one place are reflected in another.")
    print("This is useful for maintaining consistency across different parts of a project.")
    print("End of demo.")
    def get_name():
        return "GitHub Copilot"
    print(f"Hello, {get_name()}!")
    print("This is a test.")
    print("This is a test.")
    for i in range(5):
        print(f"Loop iteration {i+1}")
    
    def calculate_sum(a, b):
        return a + b
    
    num1 = 10
    num2 = 20
    result = calculate_sum(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")
    
    try:
        with open("/home/ayush/Videos/errorbynight/demoproject/sample.txt", "r") as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("The file was not found.")

def create_client_socket(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")
    return client_socket

def communicate_with_server(host, port):
    client_socket = create_client_socket(host, port)
    message = client_socket.recv(1024)
    print(f"Received message from server: {message.decode()}")
    client_socket.close()

if __name__ == "__main__":
    code_sync_demo()
    communicate_with_server('127.0.0.1', 65432)