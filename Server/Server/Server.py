import socket

serverPort = 12000
serverName = 'localhost'
serverSocket = socket.socket(AF_INET, SOCK_STREAM)

serverSocket.bind((serverName, serverPort))
print('Serveri eshte startuar ne localhost: ' + str(serverPort))
serverSocket.listen(5)
print('Serveri eshte i gatshem te pranoj kerkesa')

while 1:
    connectSocket, addr = serverSocket.accept()
    print('Klienti eshte lidhur ne server %s me port %s' % addr)
    fjalia = connectSocket.recv(1200)
    fjaliaM = fjalia.upper()
    print(fjaliaM)
    connectSocket.send(fjaliaM)
    connectSocket.close()

