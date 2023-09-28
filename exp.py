# stringget = "GET /assignment2?request="
# http11 = " HTTP/1.1"
# stringok = 'HTTP/1.1 200 OK\n\n'
# last_part = "\r\n\r\n"
# #declre responce_cache
# responce_cache = {}
# cache_limit = 0
# keylist = []
# recv_msg = c.recv(1024).decode()

# while recv_msg:
#     #if recv_msg[:len(stringget)] == stringget and recv_msg[len(http11 + last_part):] == http11 + last_part:
# 	if recv_msg[:len(stringget)] == stringget and recv_msg[-len(http11 + last_part):] == http11 + last_part:
#         #secondstring = recv_msg[len(stringget):len(http11 + last_part)]
# 		secondstring = recv_msg[len(stringget):-len(http11 + last_part)]
# 		if secondstring in responce_cache:  
#             #required key value                
# 			final_responce = stringok + responce_cache[secondstring] + last_part
# 			c.send(final_responce.encode())
# 		else:
#             #s.send(secondstring.encode())
# 			S.send(secondstring.encode())

# 			final_responce = S.recv(1024).decode()
#             #final_responce = S.recv(1024).decode()
# 			if cache_limit<3:
# 				cache_limit += 1
# 			else:
# 				b = keylist.pop(0)
# 				del responce_cache[b]
# 			responce_cache[secondstring] = final_responce
# 			keylist.append(secondstring)

# 			responce = stringok + final_responce + last_part
# 			c.send(responce.encode())
# 	else:
# 		final_responce = '400 Bad Request\r\n\r\n'
# 		c.send(final_responce.encode())

# 	recv_msg = c.recv(1024).decode()
stringget = "GET /assignment2?request="
http11 = " HTTP/1.1"
stringok = 'HTTP/1.1 200 OK\n\n'
last_part = "\r\n\r\n"
lenget = len(stringget) #25
lentt = len(http11) #9 
lenok = len(stringok) #17
lenlasp = len(last_part) #4
print("lenget : ",lenget)
print("lentt : ",lentt)
print("lenok : ",lenok)
print("lenlasp :",lenlasp)
