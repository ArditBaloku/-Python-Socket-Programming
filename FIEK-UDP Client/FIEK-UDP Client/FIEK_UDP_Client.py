import socket

serverName = input("Shenoni emrin e serverit (apo lini zbrazet per vlere te nenkuptuar)")
port = input("Shenoni portin e serverit (apo lini zbrazet per vlere te nenkuptuar)")
if (serverName == ''):
    serverName = 'localhost'
if (port == ''):
    port = 12000
else:
    try:
        port = int(port)
    except:
        print("Nuk keni japur numer valid per port")

addr = (serverName, port)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((serverName, port))
    while True:
        try:
            request = input("Shenoni kerkesen per serverin apo shenoni quit per te dal nga programi: ")
            if (request == "quit"):
                break
            s.sendto(str.encode(request), addr)
            response = s.recvfrom(128)
            response = response[0].decode()
            print('Pergjigja: ', repr(response))
        except:
            print("Ka ndodhur nje gabim, ju lutem provoni perseri")



