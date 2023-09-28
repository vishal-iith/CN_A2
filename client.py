import socket

serverIP = "10.0.1.2"

dst_ip = str(input("Enter dstIP: "))
s = socket.socket()
#S = socket.socket()
print(dst_ip)
port = 12346

s.connect((dst_ip, port))
while True:
	req = str(input("Enter the GET request: "))
	finalreq = req + '\r\n\r\n'
	s.send(finalreq.encode())
    #S.send(finalreq.encode())
	# print("decoded : ",s.recv(1024).decode())
	recvstr = s.recv(1024).decode()
	trd_part = recvstr.split(" ")
	val_part = trd_part[2].split("\n")
	val = val_part[2]
	print(val)



#print ('Client received '+s.recv(1024).decode())