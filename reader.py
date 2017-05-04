import csv
from Tkinter import *
import os.path

#################################### BASIC CONFIGURATION ###########################################
idFileAddress = "/home/bhavul/Dropbox/Programming/Practice/IDWise"
tagFileAddress = "/home/bhavul/Dropbox/Programming/Practice/TagWise"
####################################################################################################


class Application(Frame):

	def __init__(self,master):						#You just have to do this initialization function or constructor. Same to same.
		Frame.__init__(self,master)
		self.grid()
		self.create_entry_widgets()

	def create_entry_widgets(self):														#This'll put all the things on place.

		self.TagLabel = Label(self, text="Search by tags:")									#Defining a label.
		self.TagLabel.grid(row=3, column=1, columnspan=1, sticky=E,pady = 10,padx=10)	#3rd row, 1st column. It's width will be of 1 column only. Try to push it to the right(East). Give a vertical padding of 10pixels. Give a horizontal padding of 10px as well.

		self.TagEnter = Entry(self)
		self.TagEnter.grid(row=3,column=2,columnspan=1,sticky=W)
		self.TagEnter.focus()															#focus this thing. So, when it opens, it directly has cursor blinking in IDLabel box. :)

		self.IDLabel = Label(self, text="Search by ID:")									
		self.IDLabel.grid(row=4, column=1, columnspan=1, sticky=E,pady=10,padx=10)		

		self.IDEnter = Entry(self)
		self.IDEnter.grid(row=4,column=2,columnspan=1,sticky=W)
		# self.IDEnter.bind("<FocusIn>",self.msgDisappear)								#so, whenever we have a focus on Tags Entry, msgDisappear is called.


		self.submit_button = Button(self,text="Submit",command=self.enterData)			#command tells what function is called on click of submit button.
		self.submit_button.grid(row=5,column=1,columnspan=2,sticky=W+E,padx=10)			#sticky=W+E tells it to stretch in both left and right direction.

		self.text = Text(self,width=30, height=5)
		self.text.grid(row=10, column=1, columnspan=2, sticky=W+E,pady=30,padx=10)

	def enterData(self,*args):
		if not os.path.exists(idFileAddress):
			print "IDWise file not found."
			sys.exit()
		if not os.path.exists(tagFileAddress):
			print "TagWise file not found."
			sys.exit()

		self.text.delete(0.0,END)	
		
		if(self.TagEnter.get().strip() != ""):
			print "in tag one"
			fileByTag = open(tagFileAddress,"rb")												#opening tagWise file.
			cByTag = csv.reader(fileByTag)			
			for row in cByTag:
				if row[0].strip() == self.TagEnter.get().strip():
					self.text.insert("0.0",row[1:])
					self.TagEnter.delete(0,END)
			fileByTag.close()

		elif(self.IDEnter.get().strip() != ""):
			print "in ID one"
			fileByID = open(idFileAddress,"rb")													#as soon as Enter is clicked or submit button is pressed, file is opened.
			cByID = csv.reader(fileByID)													#csv parser csv reader.
			for row in cByID:
				print row
				if row[0].strip() == self.IDEnter.get().strip():
					self.text.insert("0.0",row[1:])
			fileByID.close()
		else:
			print "Fatal error. Report as an issue what produced this bug on github please. Thank you. Program will now exit."
			fileByTag.close()
			fileByID.close()
			sys.exit()

				

		self.IDEnter.delete(0, END)			#don't try 0.0. That doesn't work. 0 works.
		self.TagEnter.delete(0,END)			#We can directly use END since we've used from Tkinter import *


root = Tk()								#a necessary step
root.title("CodeTrainer-Reader")		#this'll be title of your main application
app = Application(root)					#Making a frame of it?
root.bind('<Return>', app.enterData)	#So that we don't have to 'click' submit button
root.geometry("300x270")				#looks good?	
root.mainloop()							#so it keeps looking for events.