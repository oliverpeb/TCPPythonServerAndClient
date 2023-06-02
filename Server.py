from socket import *
import concurrent.futures
import json

serverPort = 55772
serverName = 'localhost'
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print('Server is ready to listen')


def handleClient(connectionSocket, addr):
    print(addr[0])
    keep_communicating = True

    while keep_communicating:
        sentence = connectionSocket.recv(1024).decode()
        y = json.loads(sentence)
        print('Received:', y)

        # Check if the webcam is in 16/9 format
        height = y["Height"]
        width = y["Width"]
        if height / 9 == width / 16:
            response = "yes"
        else:
            response = "no"

        # Send the response back to the client
        connectionSocket.send(response.encode())

        keep_communicating = False  # Set to False to terminate the loop and close the connection
        connectionSocket.close()


with concurrent.futures.ThreadPoolExecutor() as executor:
    while True:
        connectionSocket, addr = serverSocket.accept()
        executor.submit(handleClient, connectionSocket, addr)
