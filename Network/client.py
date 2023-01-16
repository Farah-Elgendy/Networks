import socket
import sys
import math
from math import sin,cos,tan,pi,exp,pow

if __name__ == "__main__":
	ip = sys.argv[1] 
	port = int (sys.argv[2])
	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client.connect((ip,port))
	#client.setblocking(True)
	string = input("Enter your equation: ")
	while True:
		client.send(bytes(string,"utf-8"))
		msg = client.recv(1024)
		#while True:
		print("The answer = " + msg.decode())
		string = input("Enter your equation: ")
		#msg = client.recv(1024)
	client.close()
