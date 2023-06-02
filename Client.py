from socket import *
import json

serverName = 'localhost'
serverPort = 55772
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Prompt the user to enter webcam data
webcam_id = int(input("Enter webcam ID: "))
webcam_brand = input("Enter webcam brand: ")
webcam_height = int(input("Enter webcam height: "))
webcam_width = int(input("Enter webcam width: "))

# Create a dictionary representing the webcam
webcam = {
    "id": webcam_id,
    "brand": webcam_brand,
    "Height": webcam_height,
    "Width": webcam_width
}

# Convert the dictionary to a JSON string
sentence = json.dumps(webcam)

clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From server:', modifiedSentence.decode())

clientSocket.close()
