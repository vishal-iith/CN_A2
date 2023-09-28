import socket

dst1_ip = str(input('Enter dstTP: '))
#s = socket.socket(())
s = socket.socket()
print ("Successful Creation of Socket:")
dport1 = 12346
#s.bind(dst1_ip, dport1)
s.bind((dst1_ip, dport1))

print ("socket binded to %s" %(dport1))
s.listen(5)
print ("socket is listening")
c, addr = s.accept()
print ('Got connection from:', addr)

#print('Server received '+recv_msg)
serverIP = "10.0.1.3"

dst_ip = str(input("Enter dstIP: "))
server_connect = socket.socket()
print(dst_ip)
port = 12345

#s.connect((dst_ip,port))
server_connect.connect((dst_ip, port))


stringget = "GET /assignment2?request="
http11 = " HTTP/1.1"
stringok = 'HTTP/1.1 200 OK\n\n'
last_part = "\r\n\r\n"
#declre responce_cache
responce_cache = {}
cache_limit = 0
keylist = []
recv_msg = c.recv(1024).decode()

while recv_msg:
    #if recv_msg[:len(stringget)] == stringget and recv_msg[len(http11 + last_part):] == http11 + last_part:
	if recv_msg[:len(stringget)] == stringget and recv_msg[-len(http11 + last_part):] == http11 + last_part:
        #secondstring = recv_msg[len(stringget):len(http11 + last_part)]
		secondstring = recv_msg[len(stringget):-len(http11 + last_part)]
		if secondstring in responce_cache:  
            #required key value                
			final_responce = stringok + responce_cache[secondstring] + last_part
			c.send(final_responce.encode())
		else:
            #s.send(secondstring.encode())
			server_connect.send(secondstring.encode())

			final_responce = server_connect.recv(1024).decode()
            #final_responce = server_connect.recv(1024).decode()
			if cache_limit<3:
				cache_limit += 1
			else:
				b = keylist.pop(0)
				del responce_cache[b]
			responce_cache[secondstring] = final_responce
			keylist.append(secondstring)

			responce = stringok + final_responce + last_part
			c.send(responce.encode())
	else:
		final_responce = '400 Bad Request\r\n\r\n'
		c.send(final_responce.encode())

	recv_msg = c.recv(1024).decode()