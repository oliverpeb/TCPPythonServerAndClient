from socket import *
import json

serverName = 'localhost'
serverPort = 55772
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Create a dictionary representing the webcam
webcam = {
    "id": 1,
    "brand": "Logitech",
    "Height": 1080,
    "Width": 1920
}

# Convert the dictionary to a JSON string
sentence = json.dumps(webcam)

clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From server:', modifiedSentence.decode())

clientSocket.close()
