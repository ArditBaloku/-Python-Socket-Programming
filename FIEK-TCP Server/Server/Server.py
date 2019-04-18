from socket import *
from datetime import *
from numpy import *
from _thread import *

def ipAdresa():
    return "Ip adresa juaj eshte %s" % addr[0]

def porti():
    return "Porti juaj eshte %s" % addr[1]

def bashketingllore(request):
    bashketinglloret = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    numri = 0
    message = str(request[1:]).upper()
    for i in range (0, len(message)):
        if(message[i] in bashketinglloret):
            numri += 1
    return str(numri)

def printimi(request):
    return ' ' .join(request[1:]).strip()

def emri_i_kompjuterit():
    if (gethostname() != ''):
        return gethostname()
    return "Emri i hostit nuk mund te gjendet"

def koha():
    return datetime.now().strftime("%H:%M:%S")

def loja():
    return str(random.randint(1, 50, 7))

def fibonacci(n):
    if (not(n.isnumeric())):
        return "Nuk keni japur nje vlere numerike apo eshte vlere jovalide per fibonacci"
    n = int(n)
    a = 0
    b = 1
    if n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n+1): 
            c = a + b 
            a = b 
            b = c 
        return b

def konvertimi (type, number):
    if (not(is_number(number))):
        return "Nuk keni japur nje numer per konvertim ose keni japur numer jo valid"
    
    number = float(number)
    
    if (type == "DegreesToRadians"):
        return number * pi / 180
    elif (type == "RadiansToDegrees"):
        return number * 180 / pi
    if (number < 0):
        return "Vlera negative nuk ka kuptim per kete konvertim"
    else:
        if (type == "KilowattToHorsepower"):
            return number * 1.341
        elif (type == "HorsepowerToKilowatt"):
            return number / 1.341
        elif (type == "GallonsToLiters"):
            return number * 3.785
        elif (type == "LitersToGallons"):
            return number / 3.785
        else:
            return "Konvertimi i kerkuar nuk ekziston"

def totient(n):
     try:
        n = int(n)
        if (n<0):
            return "Keni dhene numer negativ"
     except:
        return "Nuk keni dhene numer te plote"
     x = 0
     for i in range (1, n):
         if(math.gcd(n,i) == 1):
             x += 1
     return "Numri i numrave me te vegjel dhe relativisht te thjeshte me %d eshte %d" %(n, x)

def pitagora(a, b):
    try:
        a = float(a)
        b = float(b)
    except:
        return "Argumentet e dhena nuk jane numra"
    if(a<0 or b<0):
            return "Keni japur brinje negative"
    return str(math.pow(a,2) + math.pow(b,2))

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def handle_request(data, conn):
    try:
        request = data.split()
        response = ""
        if request[0] == "IPADRESA":
            response = ipAdresa()
        elif request[0] == "NUMRIIPORTIT":
            response = porti()
        elif request[0] == "BASHKETINGLLORE":
            response = bashketingllore(request)
        elif request[0] == "PRINTIMI":
            response = printimi(request)
        elif request[0] == "EMRIIKOMPJUTERIT":
            response = emri_i_kompjuterit()
        elif request[0] == "KOHA":
            response = koha()
        elif request[0] == "LOJA":
            response = loja()
        elif request[0] == "FIBONACCI":
            response = str(fibonacci(request[1]))
        elif request[0] == "KONVERTIMI":
            response = str(konvertimi(request[1], request[2]))
        elif request[0] == "TOTIENT":
            response = totient(request[1])
        elif request[0] == "PITAGORA":
            response = pitagora(request[1], request[2])
        else:
            response = "Kerkese invalide"
        conn.sendall(str.encode(response))
    except:
        response = "Ka ndodhur nje gabim, provoni perseri"
        conn.sendall(str.encode(response))
    
def client_thread(conn):
    while True:
        data = conn.recv(128).decode()
        if not data:
            break
        handle_request(data, conn)
    conn.close()

host = 'localhost'
port = 12000
s = socket(AF_INET, SOCK_STREAM)

s.bind((host, port))
s.listen(5)
print("Serveri eshte gati per kerkesa")



while True:
    conn, addr = s.accept()
    print("Lidhur me " + addr[0] + ":" + str(addr[1]))
    start_new_thread(client_thread, (conn,))

s.close()

