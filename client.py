import socket

cache_ip = "10.0.1.2"  # Replace with the actual IP address of the cache (H2)
cache_port = 12345  # Replace with the actual port number

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((cache_ip, cache_port))

while True:
    key = input("Enter key to GET (or 'quit' to exit): ")
    if key == 'quit':
        break

    client_socket.send(key.encode())
    data = client_socket.recv(1024).decode()

    if data:
        print(f"Value for key '{key}': {data}")
    else:
        print(f"Key '{key}' not found in cache.")

client_socket.close()
