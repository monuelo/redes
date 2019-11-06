from socket import *

serverName = "localhost"
serverPort = 6789

clientSocket = socket(AF_INET, SOCK_DGRAM)
serverAddress = (serverName, serverPort)
try:
    sentence = input('Input: ')

    sent = clientSocket.sendto(sentence.encode('utf-8'), serverAddress)
    data, server = clientSocket.recvfrom(4096)
    print("From Server:", data.decode('utf-8'))
finally:
    clientSocket.close()
