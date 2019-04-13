import socket

serverName = 'localhost'
port = 12000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((serverName, port))
    while True:
        request = input("Type your server request here or type quit to quit: ")
        if (request == "quit"):
            break
        s.sendall(str.encode(request))
        response = s.recv(1024).decode()
        print('Pergjigja: ', repr(response))


