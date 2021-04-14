import socket
import threading
from tkinter import *
from tkinter import scrolledtext
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(),5500))



class Client():
    def __init__(self):
        self.gui = False
        rec_thread = threading.Thread(target=self.recv_msg)
        rec_thread.start()
        send_thread = threading.Thread(target=self.write)
        send_thread.start()

    def write(self):

        self.root = Tk()
        self.root.configure(bg="lightgray")

        chat_label = Label(self.root,text="chat:")
        chat_label.pack()

        

        self.input_area = Text(self.root,height=10,width=100)
        self.input_area.pack()


        self.text_area = scrolledtext.ScrolledText(self.root)
        self.text_area.pack()
        self.text_area.config(state="disabled")

        self.send_btn = Button(self.root,text="send",command=self.send_chat)
        self.send_btn.pack()
        

        self.root.protocol("WM_DELETE_WINDOW",self.stop)

        self.gui = True
        self.root.mainloop()
    def recv_msg(self):
        while True:
            try:
                if self.gui:
                    msg = client.recv(1024*2)
                    self.text_area.config(state="normal")
                    self.text_area.insert("end",msg)
                    self.text_area.yview("end")
                    self.text_area.config(state="disabled")
            except ConnectionAbortedError:
                    break
            # except Exception as e:
            #     print(e)
            #     client.close()
        #     break

    def send_chat(self):
        
        msg = self.input_area.get("1.0","end")
        client.send(msg.encode("utf-8"))
        self.input_area.delete("1.0",END)

    def stop(self):
        self.root.destroy()
        client.close()



network = Client()