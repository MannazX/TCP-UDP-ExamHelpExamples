from socket import *
import threading
import json

## NB: Run server script before client

PORT = 24440
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', PORT)) # Bind socket to port
serverSocket.listen(1) # Allows for 1 client to listen on server
bikeList = []
print("Server is ready to receive")

# {"command":"add", "input":{"id":1,"brand":"Centurion","color":"Black","size":24}}
# {"command":"all"}
# {"command":"update", "input":{"id":1,"brand":"Centerion","color":"Red","size":21}}
# {"command":"delete", "id":1}

def jsonBikeService(connectionSocket):
    while True:
        message = connectionSocket.recv(1024).decode().strip() # Recieves message from client as string
        if message == "exit":
            print("Exiting Service")
            break
        try:
            msg = json.loads(message)
            
            if msg["command"] == "add" and len(msg) == 2: # Checks that add command is split into a list of length 2
                try:
                    newBike = msg["input"] # Loads the argument in as a json object
                    bikeList.append(newBike) # Adds object to list
                    outMessage = "New Bike Created\n"
                    connectionSocket.send(outMessage.encode()) # Response back to client
                except json.decoder.JSONDecodeError:
                    print("The argument type is invalid - json format is required")
                    break
            elif msg["command"] == "all": # Input is not split
                if len(bikeList) == 0: # Checks if list is empty
                    outMessage = "List is empty\n"
                    connectionSocket.send(outMessage.encode())
                for bike in bikeList:
                    outMessage += json.dumps(bike) + "\n" 
                    connectionSocket.send(outMessage.encode()) # Returns all bikes in list with new line at the end
            elif msg["command"] == "update" and len(msg) == 2:
                try:
                    found = False
                    newBike = msg["input"]
                    for bike in bikeList:
                        if bike["id"] == newBike["id"]:
                            found = True
                            bikeList[bikeList.index(bike)] = newBike # Set element at 
                            outMessage = f"Item at id with {bike["id"]} updated\n"
                            connectionSocket.send(outMessage.encode())
                    if not found:
                        outMessage = "The id in the argumnent object is not found in the list\n"
                        connectionSocket.send(outMessage.encode())
                except json.decoder.JSONDecodeError:
                    print("The argument type is invalid - json format is required")
                    break
            elif msg["command"] == "delete" and len(msg) == 2:
                try:
                    bikeId = int(msg["id"])
                    found = None
                    for bike in bikeList:
                        if bike["id"] == bikeId:
                            found = bike
                    if found:
                        bikeList.remove(found)
                        outMessage = f"Item at id with {bikeId} deleted\n"
                        connectionSocket.send(outMessage.encode())
                    else:
                        outMessage = f"Item with {bikeId} not found"
                        connectionSocket.send(outMessage.encode())
                except ValueError:
                    print("The argument type is invalid - must be parseable to an int")
        except json.decoder.JSONDecodeError:
            print("Incorrect input format - json format required")
            break
                
while True:
    connectionSocket, addr = serverSocket.accept() # Opens server socket
    print(f"Connection established with {addr}") # Connection message with address
    threading.Thread(target=jsonBikeService, args=(connectionSocket,)).start() # Starts thread for service via connection socket
    break