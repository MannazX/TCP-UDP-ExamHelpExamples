import requests

### NB: Your exam task will not be anything in this format, so only use this as a reference for how you may build your own 
###     Solution. I would suggest not building functions in every case as requests often are easily integrated into the solution

BASE_URL = "http://localhost:####/api/Bicycles" ## or azure web link if on azure

BIKE_DICT = {
    "brand" : "Centurion",
    "color" : "Black",
    "size" : 24
}

def requestGet(id = None):
    if id != None:
        response = requests.get(f"{BASE_URL}/{id}", json=BIKE_DICT)
        
        if response.status_code == 200:
            print(f"Get Successful - {response.status_code}")
            print("\n")
            print(response.json())
        if response.status_code == 204:
            print(f"No content was found - {response.status_code}")
    else:
        response = requests.get(BASE_URL, json=BIKE_DICT)
        if response.status_code == 200:
            print(f"Get Successful - {response.status_code}")
            print("\n")
            print(response.json())
        if response.status_code == 204:
            print(f"No content was found - {response.status_code}")

def requestPost():
    response = requests.post(BASE_URL, json=BIKE_DICT)

    if response.status_code == 201:
        print(f"Post Successful - {response.status_code}")
        print("\n")
        print(response.json())
    elif response.status_code == 400:
        print(f"Bad request was made - {response.status_code}")
    
def requestPut(id):
    response = requests.put(f"{BASE_URL}/{id}", json=BIKE_DICT)
    
    if response.status_code == 200:
        print(f"Put Successful - {response.status_code}")
        print("\n")
        print(response.json())
    elif response.status_code == 400:
        print(f"Bad request was - {response.status_code}")
        
def requestDelete(id):
    response = requests.delete(f"{BASE_URL}/{id}")
    
    if response.status_code == 200:
        print(f"Delete Successful - {response.status_code}")
        print("\n")
        print(response.json())
    if response.status_code == 404:
        print(f"Item was not found - {response.status_code}")

cmd = input().strip().split()
if cmd[0].lower() == "get":
    if len(cmd) == 2:
        requestGet(int(cmd[1]))
    else:
        requestGet()
if cmd[0].lower() == "post":
    requestPost()
if cmd[0].lower() == "put":
    if len(cmd) == 2:
        requestPut(int(cmd[1]))
    else:
        print("An id parameter is required")
if cmd[0].lower() == "delete":
    if len(cmd) == 2:
        requestDelete(int(cmd[1]))
    else:
        print("An id parameter is required")