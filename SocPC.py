import socket
from time import sleep

port = 8833
host = '192.168.137.212'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print("Successfully connected to server")

for i in range(3):
    sleep(2)
    s.send(bytes(str(i).encode('utf-8')))

s.send(bytes("end".encode('utf-8')))