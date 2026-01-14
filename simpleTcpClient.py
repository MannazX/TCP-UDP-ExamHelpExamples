# computer networks TCPClient, page 191
from socket import *

serverport = 24440
servername = "localhost"

clientSocket = socket(AF_INET, SOCK_STREAM) ## TCP setup with Socket Steam
clientSocket.connect((servername, serverport))
while True:
  
  request = input('Enter request: ')
  clientSocket.send(request.encode())
  response = clientSocket.recv(1024).decode()
  print(f'Response from server: {response}')
  if request.lower() == 'exit':
      print('Exiting client.')
      break
    
clientSocket.close()