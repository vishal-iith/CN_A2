import socket

server_ip = "10.0.1.3"
cache_ip = "10.0.1.2"
client_ip = "10.0.1.1"

server_port = 12345
cache_port = 12345
client_port = 12345


#s = socket.socket(())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Successful Creation of Socket:")
#s.bind(dst1_ip, dport1)
s.bind((cache_ip,cache_port))

print ("socket binded to %s" %(cache_port))
s.listen(5)
print ("socket is listening")
c, addr = s.accept()
print ('Got connection from:', addr)

#print('Server received '+recv_msg)


# server_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server_connect.connect(dst_ip, port)
# server_connect.connect((server_ip, server_port))

recv_msg = c.recv(1024).decode()

#declre responce_cache
responce_cache = {'key1':'val1','key2':'val2','key3':'val3'}
keylist = ['key1','key2','key3']
cache_limit = 0

while True:
	# recv_msg in form of "GET /assignment2?request=key1 HTTP/1.1"
	keypart = recv_msg.split(" ")[1]
	key = keypart.split("=")[1]

	#we go key now 
	#check if key is in cache
	if key in responce_cache:
		okmsg = "HTTP/1.1 200 OK\r\n\r\n" + responce_cache[key]
		c.send(okmsg.encode())

	#if key is not in cache
	else:
		#ss is serversocket
		ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		ss.connect((server_ip,server_port))
		print("Connected to server...")
		reqmsg = "GET /assignment2?request="+key+" HTTP/1.1\r\n\r\n"
		ss.send(reqmsg.encode())

		#recvfs is recieved msg from server

		recvfs = ss.recv(1024).decode()
		# recived message in the form of "HTTP/1.1 200 OK <key>"
		print(recvfs)
		ss.close()

		tempstr = recvfs.split(" ")[1]
		#message to client
		if tempstr == "200":
			climsg = recvfs.split(" ")[3]
			responce_cache[key]=climsg
		elif tempstr == "404":
			climsg = "Request key not found"

		c.send(climsg.encode())

	recv_msg = c.recv(1024).decode()




# while recv_msg:
#     #if recv_msg[:25] == "GET /assignment2?request=" and recv_msg[13:] == " HTTP/1.1\r\n\r\n"
# 	if recv_msg[:25] == "GET /assignment2?request=" and recv_msg[-13:] == " HTTP/1.1\r\n\r\n":
#         #secondstring = recv_msg[25:13]
# 		secondstring = recv_msg[25:-13]
# 		if secondstring in responce_cache:  
#             #required key value                
# 			final_responce = "HTTP/1.1 200 OK\n\n" + responce_cache[secondstring] + "\r\n\r\n"
# 			c.send(final_responce.encode())
# 		else:
#             #s.send(secondstring.encode())
# 			server_connect.send(secondstring.encode())

# 			final_responce = server_connect.recv(1024).decode()
#             #final_responce = server_connect.recv(1024).decode()
# 			if cache_limit<3:
# 				cache_limit += 1
# 			else:
# 				delelem = keylist.pop(0)
# 				del responce_cache[delelem]
# 			responce_cache[secondstring] = final_responce
# 			keylist.append(secondstring)

# 			responce = "HTTP/1.1 200 OK\n\n" + final_responce + "\r\n\r\n"
# 			c.send(responce.encode())
# 	else:
# 		final_responce = '400 Bad Request\r\n\r\n'
# 		c.send(final_responce.encode())

# 	recv_msg = c.recv(1024).decode()
