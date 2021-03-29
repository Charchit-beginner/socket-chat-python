import socket
from _thread import *
import sys

server = socket.gethostname()
port = 5500

# (socket.gethostbyname(),1234

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.bind((server,port))
except socket.error as e:
    print(e)


s.listen() # in this parameter in int and it tells how many can connect
print("waiting for connection, server started")


def threaded_c(conn):    # runs in the background and this will run in the while loop
    
    
    reply = ""
    while True:
        inp = input("Enter msg")
        conn.send(str.encode(inp))
        try:
            data = conn.recv(2048*4455)
            reply = data.decode("utf-8")
            if not data:
                print("disconnected")
                break
            else:
                print("received : ",reply)
            
        except :
            break
    print("Lost connection")
    conn.close()
while True:
    conn,addr = s.accept() # it accept the incoming connection and store it and conn is object and addr is ip adress
    print("connected to:" , addr)

    start_new_thread(threaded_c,(conn,))
