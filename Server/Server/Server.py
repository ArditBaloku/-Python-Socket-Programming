import socket

serverName = 'localhost'
port = 12000

#def bashketingllore(message):
#    bashketinglloret = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
#    numri = 0
#    message1 = str(message).upper
#    for i in range(0, len(message)-16):
#        if(message[i+16] in bashketinglloret):
#            ++numri
#    return str(numri)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((serverName, port))
    s.listen(5)
    print("Server is ready to accept requests")
    connectSocket, addr = s.accept()
    with connectSocket:
        print('Connected by %s on port %s' % addr)
        while True:
            data = connectSocket.recv(1024).decode()
            request = data.split()
            response = ""
            if not data:
                break
            elif request[0] == "IPADRESA":
                response = "Ip adresa juaj eshte %s" % addr[0]
            elif request[0] == "NUMRIIPORTIT":
                response = "Porti juaj eshte %s" % addr[1]
            #elif request[0] == "BASHKETINGLLORE":
            #    response = bashketingllore(request)
            else:
                response = "Invalid request"
            connectSocket.sendall(bytes(str.encode(response)))

