import socket

HOST = 'localhost'
PORT = 10001

print 'glove_dummy online'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while 1:
	try:
		s.connect((HOST, PORT))
	except:
		continue
	break
s.sendall('gloves')

data = s.recv(1024)
print data

s.close()

print 'band dummy offline'