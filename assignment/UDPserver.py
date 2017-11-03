from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print('Received message-> ', message, ' from client at: ', clientAddress)
    if message == b'quit':
        print("Server shut down due to remote request.")
        serverSocket.sendto('remote server shutdown'.encode(), clientAddress)
        break
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)

serverSocket.close()
