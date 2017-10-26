from socket import *
from datetime import datetime
serverPort = 12000
# The changed SOCKET TYPE, first diffenrence compared to UDP socket
welcomeSocket = socket(AF_INET, SOCK_STREAM)
welcomeSocket.bind(('', serverPort))
welcomeSocket.listen(1) # This line doesn't exist in UDP serverSocket
print ("The server is ready to receive")
connectionSocket = None
while True:
    # create a new connection socket from welcoming socket to handle specific client request
    if not connectionSocket:
        connectionSocket, clientAddress = welcomeSocket.accept() 
    # read bytes from socket (but not address like UDP)
    message = connectionSocket.recv(2048)
    print('Received message-> ', message,
          ' from client: ', clientAddress,
          ' at ', str(datetime.now()))

    if message == b'quit': # the send function replaced sendto function in UDP
        print("Server shut down due to remote request at ", str(datetime.now()))
        connectionSocket.send('remote server shutdown'.encode())
        break

    modifiedMessage = message.decode().upper()
    connectionSocket.send(modifiedMessage.encode())

connectionSocket.close()
