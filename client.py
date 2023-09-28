import socket

server_ip = "10.0.1.3"
cache_ip = "10.0.1.2"
client_ip = "10.0.1.1"

server_port = 12345
cache_port = 12345
client_port = 12345


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.connect((cache_ip, cache_port))

while True:
	key = str(input('Enter the Key: '))
	final_request = "GET /assignment2?request="+key+" HTTP/1.1\r\n\r\n"
	#final request in form of "GET /assignment2?request=key1 HTTP/1.1"
	s.send(final_request.encode())
    
	recv_msg = s.recv(1024).decode()

	print("Recieve: ",recv_msg)
	



#print ('Client received '+s.recv(1024).decode())
