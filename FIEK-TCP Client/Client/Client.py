import socket

serverName = input("Shenoni emrin e serverit (apo lini zbrazet per vlere te nenkuptuar): ")
port = input("Shenoni portin e serverit (apo lini zbrazet per vlere te nenkuptuar): ")
if (serverName == ''):
    serverName = 'localhost'
if (port == ''):
    port = 12000
else:
    try:
        port = int(port)
    except:
        print("Nuk keni japur numer valid per port")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((serverName, port))
    while True:
        try:
            request = input("Shenoni kerkesen per serverin apo shenoni quit per te dalur nga programi: ")
            if (request == "quit"):
                break
            elif (len(request.encode()) > 128):
                print("Keni japur kerkese me te madhe se 128 bajt")
                continue
            elif (request == ""):
                continue
            s.sendall(str.encode(request))
            response = s.recv(128).decode()
            print('Pergjigja: ', repr(response))
        except:
            print("Ka ndodhur nje gabim, ju lutem provoni perseri")


