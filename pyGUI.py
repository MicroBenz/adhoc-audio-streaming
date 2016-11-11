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
		global entryText
		entryText=""
		entryText=Tkinter.StringVar()
		self.entry=Tkinter.Entry(self,textvariable=entryText)
		self.entry.grid(column=0,row=0,sticky="EW")
		self.entry.focus_set()

		button=Tkinter.Button(self,text=u"Browse for musics...",command=self.OnButtonClick)
		button.grid(column=1,row=0,sticky="EW")

		
		button1=Tkinter.Button(self,text=u"Play",command=self.playMusic)
		button1.grid(column=3,row=3)
		button1.place(relx=0.5,rely=0.5,anchor="center")
		


		self.grid_columnconfigure(0,weight=1)
		self.resizable(False,False)


	
	def OnButtonClick(self):
			# self.withdraw()
			# currdir=os.getcwd()
			# tempdir = askdirectory(parent=self, initialdir=currdir, title='Please select a directory')
			path=askopenfilename()
			filename=os.path.basename(path)
			entryText.set(filename)
		
	def playMusic(self):
		os.system('python client.py '+self.entry.get())		

        	        

if __name__=="__main__":
	app=simpleApp_TK(None)
	app.title('Wireless speaker')
	app.geometry('{}x{}'.format(500,500))
	app.mainloop()
