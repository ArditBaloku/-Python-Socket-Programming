import socket

serverName = input("Shenoni emrin e serverit (apo lini zbrazet per vlere te nenkuptuar)")
port = input("Shenoni portin e serverit (apo lini zbrazet per vlere te nenkuptuar)")
if (serverName == ''):
    serverName = 'localhost'
if (port == ''):
    port = 12000
else:
    port = int(port)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((serverName, port))
    while True:
        try:
            request = input("Type your server request here or type quit to quit: ")
            if (request == "quit"):
                break
            s.sendall(str.encode(request))
            response = s.recv(1024).decode()
            print('Pergjigja: ', repr(response))
        except:
            print("Ka ndodhur nje gabim, ju lutem provoni perseri")


