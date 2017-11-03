from socket import *
serverName = '52.187.23.76'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
while True:
    # socket_list = [
    message = input('Input lowercase sentence:')
    # no need to attach IP and port
    clientSocket.send(message.encode())
    modifiedMessage = clientSocket.recv(2048)
    if modifiedMessage == b'remote server shutdown':
        print('Remote session shutdown as requested.')
        break
    print(modifiedMessage.decode())
    input()

clientSocket.close()
print('Client closed.')
