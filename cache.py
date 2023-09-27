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

strget = "GET /assignment1?request="
http11 = " HTTP/1.1"
strok = 'HTTP/1.1 200 OK\n\n'
last = "\r\n\r\n"

local = {}
i = 0
key_list = []

rcmsg = c.recv(1024).decode()

while rcmsg:
	if rcmsg[:len(strget)] == strget and rcmsg[-len(http11 + last):] == http11 + last:
		sstring = rcmsg[len(strget):-len(http11 + last)]
		if sstring in map:                  #key
			a = strok + map[sstring] + last
			c.send(a.encode())
		else:
			cc.send(sstring.encode())
			a = cc.recv(1024).decode()
			if i<3:
				i += 1
			else:
				b = key_list.pop(0)
				del map[b]
			map[sstring] = a
			key_list.append(sstring)
			b = strok + a + last
			c.send(b.encode())
	else:
		a = '400 Bad Request\r\n\r\n'
		c.send(a.encode())

	rcmsg = c.recv(1024).decode()


