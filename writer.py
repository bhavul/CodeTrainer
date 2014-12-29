import csv
from Tkinter import *
import os.path

#################################### BASIC CONFIGURATION ###########################################
idFileAddress = "IDWise"
tagFileAddress = "TagWise"
####################################################################################################


class Application(Frame):

	def __init__(self,master):						#You just have to do this initialization function or constructor. Same to same.
		Frame.__init__(self,master)
		self.grid()
		self.create_entry_widgets()

	def create_entry_widgets(self):														#This'll put all the things on place.

		self.IDLabel = Label(self, text="ID/Name :")									#Defining a label.
		self.IDLabel.grid(row=3, column=1, columnspan=1, sticky=E,pady = 10,padx=10)	#3rd row, 1st column. It's width will be of 1 column only. Try to push it to the right(East). Give a vertical padding of 10pixels. Give a horizontal padding of 10px as well.

		self.IDEnter = Entry(self)
		self.IDEnter.grid(row=3,column=2,columnspan=1,sticky=W)
		self.IDEnter.focus()															#focus this thing. So, when it opens, it directly has cursor blinking in IDLabel box. :)

		self.TagLabel = Label(self, text="Labels :")									
		self.TagLabel.grid(row=4, column=1, columnspan=1, sticky=E,pady=10,padx=10)		

		self.TagsEnter = Entry(self)
		self.TagsEnter.grid(row=4,column=2,columnspan=1,sticky=W)
		self.TagsEnter.bind("<FocusIn>",self.msgDisappear)								#so, whenever we have a focus on Tags Entry, msgDisappear is called.


		self.submit_button = Button(self,text="Submit",command=self.enterData)			#command tells what function is called on click of submit button.
		self.submit_button.grid(row=5,column=1,columnspan=2,sticky=W+E,padx=10)			#sticky=W+E tells it to stretch in both left and right direction.

		self.text = Text(self,width=30, height=1)
		self.text.grid(row=10, column=1, columnspan=2, sticky=W+E,pady=30,padx=10)

	def msgDisappear(self,*args):
		self.text.tag_config("successText",background="white")							#we've defined successText as whatever appears on the message box. Now, make it's background white.
		self.text.delete(0.0,END)														#and delete whatever was there in it starting from 0th line 0th character till the end.


	def enterData(self,*args):
		if not os.path.exists(idFileAddress):
			file = open(idFileAddress,"wb")
			file.close()
		if not os.path.exists(tagFileAddress):
			file = open(tagFileAddress,"wb")
			file.close()
		fileByID = open(idFileAddress,"rb")													#as soon as Enter is clicked or submit button is pressed, file is opened.
		cByID = csv.reader(fileByID)													#csv parser csv reader.

		fileByTag = open(tagFileAddress,"rb")												#opening tagWise file.
		cByTag = csv.reader(fileByTag)


		dictIDwise = {}
		for row in cByID:
			dictIDwise[row[0]] = row[1:]												#so, if you added "1502:display,network,array", you can have such a dictionary entry for it.

		# print dictIDwise

		dictTagwise = {}
		for row in cByTag:
			dictTagwise[row[0]] = row[1:]

		fileByID.close()																#closing the file opener as reader, so we can write such a file.
		fileByTag.close()

		########### FOR IDWise FILE ##########################################
		if self.IDEnter.get().strip() in dictIDwise.keys():										#if the ID already exists in the dictionary (the whole file that was read), then this is duplicate n so, show error message.
			# print "Sorry, an entry for this already exists."
			self.text.insert(0.0,"Sorry, an entry already exists.")
			self.text.tag_add("successText","1.0",END)
			self.text.tag_config("successText",background="red",foreground="white")
		else:																			#entry corresponding to this ID doesn't exist. 
			fileByIDw = open(idFileAddress,"wb")												#open it in writing mode. Note: this clears all content of the file first.		
			cByIDw = csv.writer(fileByIDw)												#csv writer.
			dictIDwise[self.IDEnter.get().strip()] = self.TagsEnter.get().split(',')			
			for key,value in dictIDwise.items():
				temp = value
				temp.insert(0,key)
				cByIDw.writerow(temp)
			fileByIDw.close()
			self.text.insert(0.0,"Successfully entered. :)")
			self.text.tag_add("successText","0.0",END)									#define a tag named 'successText' that covers everything in msg box.
			self.text.tag_config("successText",background="green",foreground="white")

			########## FOR TagWise FILE ###########################################
			allTagsEntered = self.TagsEnter.get().split(',')
			# print allTagsEntered
			allTagsEntered = map(str.strip,allTagsEntered)
			# print allTagsEntered
			fileByTagw = open(tagFileAddress,"wb")
			cByTagw = csv.writer(fileByTagw)
			# print "dictTagWise : "+str(dictTagwise)
			for tag in allTagsEntered:
				if tag in dictTagwise.keys():
					list = dictTagwise[tag]
					list.append(self.IDEnter.get())
					dictTagwise[tag] = list
				else:
					dictTagwise[tag] = [self.IDEnter.get()]
			for key,value in dictTagwise.items():
				temp2 = value
				temp2.insert(0,key)
				cByTagw.writerow(temp2)

			fileByTagw.close()
		

		self.IDEnter.delete(0, END)			#don't try 0.0. That doesn't work. 0 works.
		self.TagsEnter.delete(0,END)		#We can directly use END since we've used from Tkinter import *
		self.IDEnter.focus()				#Will restore focus to the Id entry box after clearing so we can type again.



root = Tk()								#a necessary step
root.title("CodeTrainer-Writer")		#this'll be title of your main application
app = Application(root)					#Making a frame of it?
root.bind('<Return>', app.enterData)	#So that we don't have to 'click' submit button
root.geometry("270x220")				#looks good?	
root.mainloop()							#so it keeps looking for events.