import socket

server_ip = "10.0.1.3"
server_port = 12345


# Defining key-value pairs stored in the server
keyValueDict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5",
    "key6": "value6"
}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket connecter successfully")
server_socket.bind((server_ip, server_port))  
print("Socket binded to %s " %(server_port))
server_socket.listen(5)
print("Socket is listening ")
c, addr = server_socket.accept()
print ('Got connection from: ', addr )
recv_message = c.recv(1024).decode()


while recv_message:

    if recv_message in keyValueDict:
        value = keyValueDict[recv_message]
        c.send(value.encode())
    else:
        print("Erro 404: NOT FOUND")
        c.send("".encode())

    recv_message = c.recv(1024).decode()
