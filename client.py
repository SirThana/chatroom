import socket
import sys
import time
import _thread
import pickle

#Server properties
IP = "localhost"
PORT = 4445
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP socket

#receiving function
def recv(threadSocket, p):
    while True:
        try:
            data = pickle.loads(threadSocket.recv(512))
            print(data)
        except:
            pass

#   --> Try to connect to the server
try:
    clientSocket.connect((IP,PORT))
    userID = input("Pick a user ID : ")
except:
    print("Couldn't connect")
    clientSocket.close()


#   --> Start the recv function on a thread
#   --> allows for prints to be pushed regardless of the state the program is in
_thread.start_new_thread(recv, (clientSocket, 0))

#   --> Keep asking for input, and send it to the server
while True:
    if clientSocket:
        x = input(">>")
        x += " || " + userID
        x = pickle.dumps(x) #Use pickle to serialize data
        if not x:
            print("Closing socket, No data to be sent")
            clientSocket.close()
            sys.close()
            break
        else:
            try:
                clientSocket.send(x)
            except:
                print("Closing socket, Couldn't send data")
                clientSocket.close()
    continue
