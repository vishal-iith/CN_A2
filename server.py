import socket

server_ip = "10.0.1.3"
cache_ip = "10.0.1.2"
client_ip = "10.0.1.1"

server_port = 12345
cache_port = 12345
client_port = 12345

key_dictionary = {
  'key1': 'val1','key2': 'val2','key3': 'val3','key4': 'val4', 'key5': 'val5','key6': 'val6'
}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Successful creation of socket:")

s.bind((server_ip, server_port))
print ("socket binded to %s" %(server_port))

s.listen(5)
print ("socket is listening")
c, addr = s.accept()
print ('Got connection from:', addr)



# keypart = recv_message.split(" ")[1]
# key = keypart.split("=")[1]





while True:
	recv_message = c.recv(1024).decode()
	#recv_message is in the form of "GET /assignment2?request=key HTTP/1.1"
	keyp = recv_message.split(" ")
	if len(keyp)>2 :
		keypart = keyp[1]
		key = keypart.split("=")[1]

		if key in key_dictionary:
		    #if key is in the data
			respmsg = "HTTP/1.1 200 OK\r\n\r\n"+" "+key_dictionary[key]
				#server response in the form of "HTTP/1.1 200 OK <key>"
		else:
			respmsg = 'HTTP/1.1 404 NOT FOUND\r\n\r\n'
			#server response int he form of "HTTP/1.1 404 NOT FOUND"

		c.send(respmsg.encode())
c.close()
