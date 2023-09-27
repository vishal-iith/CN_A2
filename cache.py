import socket
cache_ip = "10.0.1.2"
client_ip = "10.0.1.1"
server_ip = "10.0.1.3"

cache_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_port = 12345
server_port = 12345
cache_port = 12345


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket successfully created")
client_port = 12346
s.bind((client_ip, client_port))
print ("socket binded to %s" %(client_port))
s.listen(5)
print ("socket is listening")
c, addr = s.accept()
print ('Got connection from', addr)


server_ip = str(input("Enter dstIP: "))
cc = socket.socket()
print(server_ip)
port = 12345
cc.connect((server_ip, server_port))

get_part = "GET /assignment1?request="
get_len = len(get_part)
http_part = " HTTP/1.1 \r\n\r\n"
http_len = len(http_part)

local = {}
key_list = []
i = 0

recv_message = c.recv(1024).decode()

while recv_message:
	if recv_message[0:get_len] == get_part and recv_message[-http_len:] == http_part:
		randstr = recv_message[len(get_part):-http_len]
		if randstr in local:                  
			a = 'HTTP/1.1 200 OK\n\n' + local[randstr] + "\r\n\r\n"
			c.send(a.encode())
		else:
			cc.send(randstr.encode())
			a = cc.recv(1024).decode()
			if i<3:
				i += 1
			else:
				b = key_list.pop(0)
				del local[b]
			local[randstr] = a
			key_list.append(randstr)
			b = 'HTTP/1.1 200 OK\n\n' + a + "\r\n\r\n"
			c.send(b.encode())
	else:
		a = '400 Bad Request\r\n\r\n'
		c.send(a.encode())

	recv_message = c.recv(1024).decode()


