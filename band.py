import socket

HOST = 'localhost'
PORT = 10002

print 'band dummy online'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while 1:
	try:
		s.connect((HOST, PORT))
	except:
		continue
	break

#s.connect((HOST, PORT))
s.sendall('band')

data = s.recv(1024)
print data

s.close()

print 'band dummy offline'