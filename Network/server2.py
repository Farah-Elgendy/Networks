import socket, os
import sys
import math
from math import sin,cos,tan,pi,exp,pow
import logging

if __name__ == "__main__":
	ip = "127.0.0.1"
	port = int (sys.argv[1])
        
	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	server.bind((ip,port))
	server.listen()
	i = 1
	logging.basicConfig(filename="log.txt",format='%(asctime)s %(message)s',filemode='w')
	logger = logging.getLogger()
	logger.setLevel(logging.DEBUG)
	while 1:
		
		c, address = server.accept()
		child_pid=os.fork()
		if child_pid==0:
			print(f"connection established - {address[0]}:{address[1]}")
			logger.info(f"connection established - {address[0]}:{address[1]}")
			while True:
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
				if not string:
					break
					break
		else:
			i+=1
	
	c.close()
	
# Test messages


#logger.critical("Internet is down")
