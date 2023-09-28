import socket

dst1_ip = str(input('Enter dstTP: '))
#s = socket.socket(())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
server_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(dst_ip)
port = 12345

#server_connect.connect(dst_ip, port)
server_connect.connect((dst_ip, port))

recv_msg = c.recv(1024).decode()

#declre responce_cache
responce_cache = {}
keylist = []
cache_limit = 0



while recv_msg:
    #if recv_msg[:25] == "GET /assignment2?request=" and recv_msg[13:] == " HTTP/1.1\r\n\r\n"
	if recv_msg[:25] == "GET /assignment2?request=" and recv_msg[-13:] == " HTTP/1.1\r\n\r\n":
        #secondstring = recv_msg[25:13]
		secondstring = recv_msg[25:-13]
		if secondstring in responce_cache:  
            #required key value                
			final_responce = "HTTP/1.1 200 OK\n\n" + responce_cache[secondstring] + "\r\n\r\n"
			c.send(final_responce.encode())
		else:
            #s.send(secondstring.encode())
			server_connect.send(secondstring.encode())

			final_responce = server_connect.recv(1024).decode()
            #final_responce = server_connect.recv(1024).decode()
			if cache_limit<3:
				cache_limit += 1
			else:
				delelem = keylist.pop(0)
				del responce_cache[delelem]
			responce_cache[secondstring] = final_responce
			keylist.append(secondstring)

			responce = "HTTP/1.1 200 OK\n\n" + final_responce + "\r\n\r\n"
			c.send(responce.encode())
	else:
		final_responce = '400 Bad Request\r\n\r\n'
		c.send(final_responce.encode())

	recv_msg = c.recv(1024).decode()