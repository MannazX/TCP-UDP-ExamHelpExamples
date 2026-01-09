from socket import *
import ssl

PORT = 24440
SERVER_NAME = "localhost"

clientSocket = socket(AF_INET, SOCK_DGRAM)
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
secureSocket = context.wrap_socket(clientSocket)
secureSocket.connect((SERVER_NAME, PORT))

while True:
    request = input("Client Input here: ")
    secureSocket.send(request.encode())
    response = secureSocket.recv(1024).decode()
    print("Response From Server: ", response)
    if response.lower() == "exit":
        print("Client Terminated!")
        break
    
secureSocket.close()