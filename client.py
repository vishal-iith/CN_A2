import socket

server_ip = "10.0.1.3"
cache_ip = "10.0.1.2"
client_ip = "10.0.1.1"

server_port = 12345
cache_port = 12345
client_port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((cache_ip, cache_port))

while True:
    method = str(input("Enter PUT or GET : "))

    if method == "PUT":
        key = str(input('Enter the Key: '))
        value = str(input('Enter the Value: '))
        final_request = "PUT /assignment2/" + key + "/" + value + " HTTP/1.1\r\n\r\n"
    elif method == "GET":
        key = str(input('Enter the Key: '))
        final_request = "GET /assignment2?request=" + key + " HTTP/1.1\r\n\r\n"
    else:
        final_request = method
        s.send(final_request.encode())
        break

    s.send(final_request.encode())

    recv_msg = s.recv(1024).decode()

    print("Receive: ", recv_msg)

s.close()
