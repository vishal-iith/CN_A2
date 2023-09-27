import socket
cache_ip = "10.0.1.2"
client_ip = "10.0.1.1"
server_ip = "10.0.1.3"
server_port = 12345  # Replace with the actual port number

cache_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port_client = 12345
port_server = 12345
port_cache = 12345


cache_socket.bind((server_ip, server_port))  # Bind to any available interface and port 12345
cache_socket.listen(5)

while True:
    print("Cache waiting for connections...")
    client_socket, client_address = cache_socket.accept()
    print(f"Connection from {client_address}")

    key = client_socket.recv(1024).decode()

    if key:
        # Check if key is in cache; if not, fetch from server
        # Implement caching logic here

        # For now, just forward the GET request to the server
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect((server_ip, server_port))
        server_socket.send(key.encode())
        data = server_socket.recv(1024).decode()
        server_socket.close()

        if data:
            print(f"Cache responding to GET key '{key}' with value: {data}")
            client_socket.send(data.encode())
        else:
            print(f"Key '{key}' not found in cache or server.")
            client_socket.send("".encode())

    client_socket.close()
