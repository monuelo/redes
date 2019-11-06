from socket import *
from threading import Thread
import time

# def concat(str1, str2):
#     return str1 + str2


# def compare(str1, str2):
#     return 'True' if (str1 == str2) else 'False'


# def substring(string, start, end):
#     return string[int(start):int(end)]


# def contains(str1, str2):
#     return 'True' if (str2 in str1) else 'False'


# def replace_char(string, char1, char2):
#     return string.replace(char1, char2)


# def switch(request):
#     if (request[0] == 'CONCATENAR'):
#         return concat(*request[1:])
#     elif (request[0] == 'COMPARAR'):
#         return compare(*request[1:])
#     elif (request[0] == 'SUBSTRING'):
#         return substring(*request[1:])
#     elif (request[0] == 'CONTEM'):
#         return contains(*request[1:])
#     elif (request[0] == 'SUBSTITUIR'):
#         return replace_char(*request[1:])
#     else:
#         return '[ERROR] INVALID METHOD'

def calculator(operation, n1, n2):
    result = '[ERROR] OPERAÇÃO NÃO REGISTRADA'
    n1 = int(n1)
    n2 = int(n2)
    if operation == 'ADD':
        result = n1 + n2
    elif operation == 'SUB':
        result = n1 - n2
    elif operation == 'MULT':
        result = n1 * n2
    elif operation == 'EXP':
        result = n1 ** n2
    elif operation == 'DIV' and n2 != 0:
        result = n1 / n2

    return result


def connection_handler():
    data, address = serverSocket.recvfrom(4096)
    if data:
        data = data.decode('utf-8').split()
        result = str(calculator(data[0], data[1], data[2])).encode('utf-8')
        ack = serverSocket.sendto('RECEIVED'.encode('utf-8'), address)
        time.sleep(2)
        sent = serverSocket.sendto(result, address)


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverAddress = ('localhost', serverPort)
serverSocket.bind(serverAddress)
print("The server is ready to receive")

while True:
    connection = Thread(target=connection_handler)
    connection.start()
    connection.join(timeout=1)

serverSocket.close()
