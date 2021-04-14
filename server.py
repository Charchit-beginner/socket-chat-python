import socket
from _thread import *
import sys

server = socket.gethostname() 
port = 5500

# (socket.gethostbyname(),1234

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    s.bind((server,port))
except socket.error as e:
    print(e)


s.listen() # in this parameter in int and it tells how many can connect
print("waiting for connection, server started")

clients = []
addrs = []

def brodcast(msg):
    for client in clients :
        client.send(str.encode(msg))

def threaded_c(client):    # runs in the background and this will run in the while loop
    while True:
        try:
            msg = client.recv(1023).decode("utf-8")
            # print(f"{addrs[clients.index(client)]}")
            brodcast(msg)
            
        except Exception as e:
            index = clients.index(client)
            print(e)
            clients.remove(client)
            client.close()
            
    print("Lost connection")
    
def recieve():
    while True:
        client,addr = s.accept() # it accept the incoming connection and store it and conn is object and addr is ip adress
        print("connected to:" , addr)


        # conn.send("")
        clients.append(client)
        addrs.append(addr)
        start_new_thread(threaded_c,(client,))
        brodcast(f"{addr} connected to the server\n")
        client.send(str.encode("you are connected to the server\n"))
        print(clients)
    


recieve()
