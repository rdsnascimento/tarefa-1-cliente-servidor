from socket import *
serverName='192.168.0.108'
serverPort= 12
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message=raw_input( 'Enter the lower case letters: ' )
clientSocket.send(message)
modifiedMessage = clientSocket.recv(1024)
print 'From Server:', modifiedMessage 
clientSocket.close()
