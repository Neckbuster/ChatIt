from tkinter import *
import socket
import threading
def send():
	s.send(msg.get().encode())
	newline=Label(screen1,text="").pack()
	sent=Label(screen1,text=msg.get()).pack()
	SendMsg.delete(0,END)

def clproc():
	while(1):
		#print("Executed")
		recv_msg=s.recv(1024)
		msgr=Label(screen1,text="Host: "+recv_msg.decode()).pack()
def client():
	global s
	s=socket.socket()
	host=hostadr.get()
	port=8000
	#us_name=input(str("Enter your user name: "))
	s.connect((host,port))
	print("THIS IS CLIENT")
	global screen1
	screen1=Toplevel(wel_screen)
	screen1.title("Client Connected...")
	screen1.geometry("500x500")
	#screen1.configure(background="grey")
	instr=Label(screen1,text="Enter EXIT to Quit").pack()
	newline=Label(screen1,text="").pack()
	newline=Label(screen1,text="").pack()
	print("This is client2")
	thread=threading.Thread(target=clproc)
	thread.daemon=True
	thread.start()
	global msg,SendMsg
	msg=StringVar()
	SendMsg=Entry(screen1,textvar=msg)
	SendMsg.pack()
	Btn=Button(screen1,text="Send",command=send).pack()
	screen1.mainloop()
def WelCome():
	global hostadr,wel_screen
	wel_screen=Tk()
	wel_screen.title("CHAT IT")
	wel_screen.geometry("500x500")
	wel_label=Label(text="WELCOME TO CHAT IT",bg="black",fg="white",font=("calibri",20)).pack()
	new_line=Label(text="").pack()
	hostAdr=Label(text="Enter Host Address: ").pack()
	hostadr=StringVar()
	adrs=Entry(textvar=hostadr).pack()
	conn_btn=Button(text="Connect",height=4,width=10,bg="red",command=client).pack()
	new_line=Label(text="").pack()
	new_line=Label(text="").pack()
	credit=Label(text="Developed by Niket Singh").pack()
	wel_screen.mainloop()

WelCome()