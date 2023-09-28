import socket

server_ip = "10.0.1.3"
cache_ip = "10.0.1.2"
client_ip = "10.0.1.1"

server_port = 12345
cache_port = 12345
client_port = 12345

local_dictionary = {
    'key1': 'val1', 'key2': 'val2', 'key3': 'val3'
}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Successful creation of socket:")

s.bind((cache_ip, cache_port))
print("socket binded to %s" % (server_port))

s.listen(5)
print("socket is listening")

while True:
    c, addr = s.accept()
    print('Got connection from:', addr)

    while True:
        recv_message = c.recv(1024).decode()
        # recv_message is in the form of "GET /assignment2?request=key HTTP/1.1"
        keyp = recv_message.split(" ")
        method = keyp[0]

        if method == "GET":
            key = keyp[1].split("=")[1]
            if key in local_dictionary:
                # if key is in the data
                respmsg = "HTTP/1.1 200 OK\r\n\r\n" + " " + local_dictionary[key]
                # server response in the form of "HTTP/1.1 200 OK <key>"
            else:
                ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                ss.connect((server_ip, cache_port))
                ss.send(recv_message.encode())

                respmsg = ss.recv(1024).decode()
                ss.close()
                respcode = respmsg.split(" ")[1]
                if respcode == "200":
                    value=respmsg.split(" ")[3]
                    local_dictionary[key] = value
                
                c.send(respmsg.encode())

                # server response in the form of "HTTP/1.1 404 NOT FOUND"

            c.send(respmsg.encode())

        elif method == "PUT":
            ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ss.connect((server_ip, cache_port))
            ss.send(recv_message.encode())
            respmsg = ss.recv(1024).decode()
            ss.close()
            c.send(respmsg.encode())
        else:
            break

    c.close()
