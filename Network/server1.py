import socket
import sys
import math
from math import sin,cos,tan,pi,exp,pow

if __name__ == "__main__":

	ip = "127.0.0.1"
	port = int (sys.argv[1])

	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	server.bind((ip,port))
	server.listen(1)
	
	while True:
		c, address = server.accept()
		print(f"connection established - {address[0]}:{address[1]}")
		while True:
			string = c.recv(1024)
			string = string.decode("utf-8")
			if not string:
				break
			print(string)
			res = eval(string)
			print(str(res))
			msg = str(res)
			c.send(msg.encode())
	c.close()
