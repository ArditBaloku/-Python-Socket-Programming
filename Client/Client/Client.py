import socket

serverName = 'localhost'
port = 12000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((serverName, port))
var = input("Ju lutem shenoni nje fjali: ")
s.sendall(str.encode(var))
r = s.recv(1024).decode()
s.close()
print('Te dhenat e pranuara nga serveri', repr(r))
