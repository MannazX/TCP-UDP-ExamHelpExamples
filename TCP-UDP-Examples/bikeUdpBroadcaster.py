from socket import *
import json
import random
import time

BROADCAST_IP = '255.255.255.255'
PORT = 42000

# Setter socket op til Broadcast
socket_sender = socket(AF_INET, SOCK_DGRAM)
socket_sender.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# Lister med muligheder at vælge i mellem
bike_names = ["Centurion", "Kildemoes", "Raleigh"]
bike_color = ["Black", "Red", "Blue", "White"]

def bike_data():
    """Skaber et datapunkt, bikeName, bikeColor bliver tilfældigt valgt med random.choice 
    size bliver valgt som en tilfældig integer indenfor 10 og 35."""
    
    bike_obj = {
        "bikeName": random.choice(bike_names),
        "bikeType": random.choice(bike_color),
        "size": random.randint(10, 35)
    }
    return bike_obj

for _ in range(25):
    bike_obj = bike_data() # Datapunkt der skal broadcastes
    message = json.dumps(bike_obj) # Konverteres til JSON streng
    print(f"Broadcaster Sending: {message}")
    socket_sender.sendto(message.encode(), (BROADCAST_IP, PORT)) # Sendes gennem Broadcast Ip via Port 42000
    time.sleep(2)


socket_sender.close()
