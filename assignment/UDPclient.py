from socket import *
serverName = '10.0.0.4'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    message = input('Input lowercase sentence:')    
    clientSocket.sendto(message.encode(),(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    if modifiedMessage == b'remote server shutdown':
        print('remote server shutdown as requested.')
        break
    print(modifiedMessage. decode())
    input()
    
clientSocket.close()
print('Client closed.')
