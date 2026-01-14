from socket import *
import json

PORT = 24440

socketReciever = socket(AF_INET, SOCK_DGRAM) ## UDP Socket - Uses Datagram
socketReciever.bind(('', PORT))
print(f"Listening for UDP messages on port {PORT}")

# Example test via SocketTest 
# {"id":1,"brand":"Centurion","color":"Black","size":24}

while True:
    message, clientAdd = socketReciever.recvfrom(3000) ## Buffer can read at most 3000 bits - Don't include this comment in your exam solution :)
    try:
        message_object = json.loads(message.decode())
        print(f"Object Received: {message_object}")
    except json.decoder.JSONDecodeError:
        print("Object sent is in incorrect format")