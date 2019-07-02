import socket
import threading
import time
import sys
import pickle

#Server properties
IP = "localhost"
PORT = 4445

#   --> create TCP socket initialize it with IP and PORT
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((IP,PORT))
serverSocket.listen()
print("Listening for incomming connections..")

#Global list to keep track of all connected sockets
clientList = []

def handler(c,a): #Connection and address
    stamp = 0
    while True:
        try:
            data = c.recv(512)
            data = pickle.loads(data) #Deserialize data
        except:
            pass
        if data:
            print(data, " || " ,stamp)
            stamp += 1
        if stamp == 12:
            print("\n\n\nClosing socket")
            clientList.remove(c)
            c.close
            break

        data = pickle.dumps(data) #Serialize data
        for client in clientList: #Send for every socket in clientList, Data
            try:
                client.send(data)
            except Exception as e:
                print(e, "\n")

#   --> Accept connections on the socket, and start a thread for each
while True:
    c, a = serverSocket.accept()
    cThread = threading.Thread(target=handler, args=(c,a))
    cThread.daemon = True
    cThread.start()
    clientList.append(c)
    print(clientList[-1])
