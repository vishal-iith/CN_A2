import socket

cache_ip = "10.0.1.2"
client_ip = "10.0.1.1"
server_ip = "10.0.1.3"


client_port = 12345
server_port = 12345
cache_port = 12345


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((cache_ip, cache_port))

while True:
    key = str(input('Enter the get command: '))
    key_url = key + '\r\n\r\n'
    s.send(key_url.encode())
    print(s.recv(1024).decode())