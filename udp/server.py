from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverAddress = ('localhost', serverPort)
serverSocket.bind(serverAddress)
print ("The server is ready to receive")

def concat(str1, str2):
    return str1 + str2

def compare(str1, str2):
    return 'True' if (str1 == str2) else 'False'

def substring(string, start, end):
    return string[int(start):int(end)]

def contains(str1, str2):
    return 'True' if (str2 in str1) else 'False'

def replace_char(string, char1, char2):
    return string.replace(char1, char2)

def switch(request):
    if (request[0] == 'CONCATENAR'): return concat(*request[1:])
    elif (request[0] == 'COMPARAR'): return compare(*request[1:])
    elif (request[0] == 'SUBSTRING'): return substring(*request[1:])
    elif (request[0] == 'CONTEM'): return contains(*request[1:])
    elif (request[0] == 'SUBSTITUIR'): return replace_char(*request[1:])
    else: return '[ERROR] INVALID METHOD'

while 1:
    data, address = serverSocket.recvfrom(4096)
    if data:
            data = data.decode('utf-8').split()
            sent = serverSocket.sendto(switch(data).encode('utf-8'), address)
