from socket import *

serverName = "localhost"
serverPort = 24440
clientSocket = socket(AF_INET, SOCK_DGRAM) ## UDP setup with Socket Datagram

message = input("Send message: ")
clientSocket.sendto(message.encode(), (serverName, serverPort))
changedMsg, serverAdd = clientSocket.recvfrom(2048)
print((changedMsg.decode()))
clientSocket.close()