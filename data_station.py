import socket
import sys

HOST = 'local host'
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

while 1:
#TODO data collection adn sending command back to client

conn.close()