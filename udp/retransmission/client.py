from socket import *
from threading import Thread
from queue import Queue

def wait_response(queue):
    data, server = clientSocket.recvfrom(4096)
    queue.put(data.decode('utf-8'))

def connect(function, args):
    new_connection = Thread(target=function, args=(args, ))
    new_connection.start()
    new_connection.join(timeout=2)

serverName = "localhost"
serverPort = 15000
clientSocket = socket(AF_INET, SOCK_DGRAM)
serverAddress = (serverName, serverPort)

confirmations = Queue()
responses = Queue()
print('We\'re online, Houston! - ', serverPort)

while True:
    sentence = input("Input: ")
    clientSocket.sendto(sentence.encode('utf-8'), serverAddress)
    
    while(not confirmations.qsize()):
        connect(wait_response, confirmations)

    if confirmations.qsize():
        while(not responses.qsize()):
            print('[INFO] Waiting for response!')
            connect(wait_response, responses)
        response = confirmations.get()
        if response == 'RECEIVED':
            print('[YASS] Received ACK from server\n')
            if responses.qsize():
                result = responses.get()
                if result and result != 'RECEIVED':
                    print('[YASS] The answer is: {}\n'.format(result))
                else:
                    print('[ERROR] Result not received')
            else:
                print('[ERROR] Result not received')
        else:  
            print('[ERROR] ACK not received')

clientSocket.close()