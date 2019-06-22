from tkinter import *
import socket
import threading
def send():
	conn.send(msg.get().encode())
	newline=Label(text="").pack()
	sent=Label(text=msg.get()).pack()
	SendMsg.delete(0,END)

def hsrecieve():
	while(1):
		#print("Executed")
		recv_msg=conn.recv(1024)
		msgr=Label(text="client: "+recv_msg.decode()).pack()
def host_it():
	global screen1_host,msg,SendMsg
	screen1_host=Tk()
	print("Tkinter on")
	screen1_host.title("Host Connected...")
	screen1_host.geometry("500x500")
	instr=Label(text="Enter EXIT to Quit").pack()
	newline=Label(text="").pack()
	newline=Label(text="").pack()
	msg=StringVar()
	SendMsg=Entry(textvar=msg)
	SendMsg.pack()
	Btn=Button(text="Send",command=send).pack()
	thread=threading.Thread(target=hsrecieve)
	thread.daemon=True
	thread.start()
	screen1_host.mainloop()
def WelCome():
	global conn
	s=socket.socket()
	host=socket.gethostname()
	print(host)
	port=8000
	s.bind((host,port))
	s.listen(2)
	print("WAITING FOR CONNECTION...")

	conn,adr=s.accept()
	print("Connected to address ",adr)
	host_it()
	'''global wel_screen_host
	wel_screen_host=Tk()
	wel_screen_host.title("CHAT IT")
	wel_screen_host.geometry("500x500")
	wel_label=Label(text="WELCOME TO CHAT IT",bg="black",fg="white",font=("calibri",20)).pack()
	new_line=Label(text="").pack()
	host_btn=Button(text="HOST",height=4,width=10,bg="red",command=host)
	host_btn.pack()
	new_line=Label(text="").pack()
	new_line=Label(text="").pack()
	credit=Label(text="Developed by Niket Singh").pack()
	wel_screen_host.mainloop()
'''
WelCome()