import Tkinter
from tkFileDialog import askopenfilename,askdirectory
import os,os.path

class simpleApp_TK(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent=parent
		self.initialize()


	def initialize(self):
		self.grid()
		global entryText,var1
		entryText=""
		entryText=Tkinter.StringVar()

		self.var1=Tkinter.IntVar()

		label=Tkinter.Label(self,anchor="center",fg="black",bg="white",text="choose music and play :D")
		label.grid(column=0,row=1,columnspan=2,sticky="EW")

		self.entry=Tkinter.Entry(self,textvariable=entryText)
		self.entry.grid(column=0,row=3,sticky="EW")
		self.entry.focus_set()

		button=Tkinter.Button(self,text=u"Browse for musics...",command=self.OnButtonClick)
		button.grid(column=1,row=3,sticky="EW")

		label1=Tkinter.Label(self,anchor="center",fg="black",bg="white",text="choose your role yeah~")
		label1.grid(column=0,row=5,columnspan=2,sticky="EW")

		rb1=Tkinter.Radiobutton(self,text="player",value=1,variable=self.var1)
		rb2=Tkinter.Radiobutton(self,text="wireless speaker(forwarder) ",value=2,variable=self.var1)
		rb3=Tkinter.Radiobutton(self,text="wireless speaker(last hop) ",value=3,variable=self.var1)
		rb1.grid(column=0,row=8,padx=50,columnspan=2,sticky="EW")
		rb2.grid(column=0,row=9,padx=50,columnspan=3,sticky="EW")
		rb3.grid(column=0,row=10,padx=50,columnspan=3,sticky="EW")

		

		
		
		button1=Tkinter.Button(self,text=u"Play",command=self.playMusic)
		button1.grid(column=3,row=5)
		button1.place(relx=0.5,rely=0.6,anchor="center")



		self.grid_columnconfigure(0,weight=1)
		self.resizable(False,False)


	
	def OnButtonClick(self):
			mPath=askopenfilename()
			# print mPath
			mFilename=os.path.basename(mPath)
			# print mFilename
			entryText.set(mFilename)
		
	def playMusic(self):
		if self.var1.get()==1:
			os.system('python client.py '+self.entry.get())
		elif self.var1.get()==2:
			os.system('python forwarder.py')
		else:
			os.system('python server.py')	

        	        

if __name__=="__main__":
	app=simpleApp_TK(None)
	app.title('Wireless speaker')
	app.geometry('{}x{}'.format(300,300))
	app.mainloop()

