import socket	
import sys	
try:
	#create an AF_INET, STREAM socket (TCP)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except (socket.error, msg):
	print ('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
	sys.exit()

print("Socket Created")

#The try block lets you test a block of code for errors.
#The except block lets you handle the error.