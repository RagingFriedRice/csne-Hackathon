import socket
import sys

HOST = 'localhost'
PORT_G = 10001
PORT_B = 10002

print 'data_station online'
glove = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
glove.bind((HOST, PORT_G))
band = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
band.bind((HOST, PORT_B))

try:
	glove.listen(1)
	conn_glove, addr = glove.accept()
	print 'glove connection established'

	band.listen(1)
	conn_band, addr = band.accept()
	print 'band connection established'

	data1 = conn_glove.recv(1024)
	data2 = conn_band.recv(1024)

	cmd = raw_input('shall we start? ')

	conn_glove.sendall('idc')
	conn_band.sendall('idc')

	#while 1:
	#TODO collect data from scanner and sending command to client
finally:
	conn_glove.close()
	conn_band.close()
	print 'data station offline'