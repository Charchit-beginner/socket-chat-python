import socket
import threading
from tkinter import *
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(),5500))




def recv_msg():
    while True:
        try:
            message = client.recv(1024*2).decode("utf-8")
            print(message)
        except:
            print("error")
            client.close()
            break
def write():
    while True:
        message = input("")
        client.send(message.encode("utf-8"))


rec_thread = threading.Thread(target=recv_msg)
rec_thread.start()
send_thread = threading.Thread(target=write)
send_thread.start()
