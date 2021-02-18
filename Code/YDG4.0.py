from tkinter import *
import os
import sys

def convertlink(link1):
	if "?list" in link1:
		s = link1.find("?list")
		s = s + 6
	elif "&list" in link1:
		s = link1.find("&list")
		s = s + 6
	if "&index" in link1:
		e = link1.find("&index")
	elif "&t" in link1:
		e = link1.find("&t")
	else:
		e = len(link1)
	link2 = "https://www.youtube.com/playlist?list="+link1[s:e]
	return link2

#root of the window
root = Tk()
root.title('YoutubeDownloader 4.0 by CrazyMeowl')

#Create a lable widget
Credit = Label(root, text="YouTube Downloader -=- Written By Meowl")#.grid(row = 0,column = 0)
LNintructrion = Label(root, text="Enter video name or paste your link")
Numintruction = Label(root, text="Enter the number of video (playlist)")
Clearspace1 = Label(root, text="	")
Clearspace2 = Label(root, text="	")
Clearspace3 = Label(root, text="	")
Format = Label(root, text="Format: ")

##shoving it onto the screen
Credit.grid(row = 0,column = 0)
LNintructrion.grid(row = 2,column = 0)
Numintruction.grid(row = 4,column = 0)
Clearspace1.grid(row = 1,column = 0)
Clearspace2.grid(row = 0,column = 1)
Clearspace3.grid(row = 6,column = 0)
Format.grid(row = 3,column = 2)
#LinkOrNameTextBox
LNTextBox = Entry(root,width = 50, borderwidth = 4)
LNTextBox.grid(row = 3,column = 0)
Numtextbox = Entry(root,width = 50, borderwidth = 4)
Numtextbox.grid(row = 5,column = 0)
Numtextbox.insert(0,"1")

#Format Row
FORMATrow = 2

form = [0]
#function to do when click button
res = [0]
def mp3(form):
	formtext = Label(root, text="mp3  Selected")
	formtext.grid(row = FORMATrow + 1,column = 3)
	form.append(0)

def mp4(form):
	formtext = Label(root, text="mp4  Selected")
	formtext.grid(row = FORMATrow + 1,column = 3)
	form.append(1)

def webm(form):
	formtext = Label(root, text="webm Selected")
	formtext.grid(row = FORMATrow + 1,column = 3)
	form.append(2)

def p480(res):
	restext = Label(root, text="480p Selected")
	restext.grid(row = FORMATrow + 4,column = 4)
	res.append(0)
def p720(res):
	restext = Label(root, text="720p Selected")
	restext.grid(row = FORMATrow + 4,column = 4)
	res.append(1)
def p1080(res):
	restext = Label(root, text="1080p Selected")
	restext.grid(row = FORMATrow + 4,column = 4)
	res.append(2)
def k2(res):
	restext = Label(root, text="  2K Selected  ")
	restext.grid(row = FORMATrow + 4,column = 4)
	res.append(3)
def k4(res):
	restext = Label(root, text="  4K Selected  ")
	restext.grid(row = FORMATrow + 4,column = 4)
	res.append(4)

def StartDownload(form):
	i = len(form)-1
	#print(form[i])
	j = len(res)-1
	#print(res[j])
	Error = 0
	LN = LNTextBox.get()
	#LN = "https://www.youtube.com/playlist?list=UUM9KEEuzacwVlkt9JfJad7g"
	N =  Numtextbox.get()
	YOU = "youtube-dl -i "
	log = "--download-archive DownloadList.txt "
	FORMAT = ""
	resolution = ""
	outFolder = "-o Downloaded/%(title)s.%(ext)s "
	#examplelink = "https://www.youtube.com/watch?v=QnDWIZuWYW0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=2"
	if len(LN) == 0 :
		WarningLN = Label(root, text="Warning: You haven't enter the link or name box!!")
		WarningLN.grid(row = 6, column = 0)
	else:							   #Warning: You haven't enter the link or name box!!
		Clearspace4 = Label(root, text="                                                                                       ")
		Clearspace4.grid(row = 6,column = 0)
		try:
			int(N)
			num = N
			PlaylistEnd = "--playlist-end "+num+" "
			Clearspace5 = Label(root, text="                                                                                ")
			Clearspace5.grid(row = 7,column = 0)
			#start if no alert
			Status = Label(root, text="-=-=-=-=- Processing -=-=-=-=-")
			Status.grid(row = 6, column = 0)
			#FORMAT
			if form[i] == 0:
				form1 = "mp3"
			if form[i] == 1:
				form1 = "mp4"
				if res[j] == 0:
					resolution = "135"
				if res[j] == 1:
					resolution = "136"
				if res[j] == 2:
					resolution = "137"
				if res[j] == 3:
					resolution = "138"
				if res[j] == 4:
					resolution = "138"
			if form[i] == 2:		
				form1 = "webm"
				if res[j] == 0:
					resolution = "244"
				if res[j] == 1:
					resolution = "247"
				if res[j] == 2:
					resolution = "248"
				if res[j] == 3:
					resolution = "271"
				if res[j] == 4:
					resolution = "313"


			#this part is for Format(mp3,mp4,webm)
			if "mp4" in form1:
				if int(resolution) <= 1080:
					FORMAT = "--format "+resolution+"+140 "
				else:
					if int(resolution) < 1280:
						ErrorMP4 = "Error: MP4 may not available in " + resolution + "p"
					elif int(resolution) == 1280:
						ErrorMP4 = "Error: MP4 may not available in 2K"
					elif int(resolution) == 1920:
						ErrorMP4 = "Error: MP4 may not available in 4K"
					print(ErrorMP4)
					Status = Label(root, text=ErrorMP4)
					Status.grid(row = 6, column = 0)
					Error = 1
			elif "webm" in form1:
				FORMAT = "--format "+resolution+"+251 "	
			elif "mp3" in form1:
				FORMAT = "--extract-audio --audio-format mp3 "

			#this part is for LN
			if "youtube.com" in LN and "list" in LN:
				LN = convertlink(LN)
				FINAL = YOU + log + PlaylistEnd + FORMAT + outFolder + LN
			elif "youtube.com" in LN:
				LN = LN
				FINAL = YOU + log + FORMAT + outFolder + LN
			else:
				search = "\"ytsearch"+num+":"+LN+"\""
				FINAL = YOU + log + FORMAT + outFolder + search
			if Error == 0:
				print(FINAL)
				run = os.system(FINAL)
				#print(run)
				if run == 0:
					print('-=-=-=-=- D O N E -=-=-=-=-')
					Status = Label(root, text="-=-=-=-=- D O N E -=-=-=-=-")
				else:
					print('-=-=-=-=- ERROR:1 -=-=-=-=-')
					Status = Label(root, text="-=-=-=-=- ERROR:1 -=-=-=-=-")
				Status.grid(row = 6, column = 0)
				#done if no alert
		except:
			WarningN = Label(root, text="Warning: Please enter number to number box")
			WarningN.grid(row = 7, column = 0)
	
		
REStext = Label(root, text="Resolution").grid(row = FORMATrow + 2,column = 2)
VIDtext = Label(root, text="for Video").grid(row = FORMATrow + 2,column = 3)
Onlytext = Label(root, text="Only").grid(row = FORMATrow + 2,column = 4)
#default form is audio
mp3(form)
#button 
mp4Button = Button(root, text="mp4",width = 15, command = lambda : mp4(form)).grid(row = FORMATrow,column = 3)
#VidButton.grid(row = 2,column = 0)
mp3Button = Button(root, text="mp3",width = 15, command = lambda : mp3(form)).grid(row = FORMATrow,column = 2)
#myButton.grid(row = 2,column = 0)
webmButton = Button(root, text="webm",width = 15, command = lambda : webm(form)).grid(row = FORMATrow,column = 4)

p480Button = Button(root, text="480p",width = 15, command = lambda : p480(res)).grid(row = FORMATrow+3,column = 2)
p720Button = Button(root, text="720p",width = 15, command = lambda : p720(res)).grid(row = FORMATrow+3,column = 3)
p1080Button = Button(root, text="1080p",width = 15, command = lambda : p1080(res)).grid(row = FORMATrow+3,column = 4)
k2Button = Button(root, text="2K",width = 15, command = lambda : k2(res)).grid(row = FORMATrow+4,column = 2)
k4Button = Button(root, text="4K",width = 15, command = lambda : k4(res)).grid(row = FORMATrow+4,column = 3)






DownloadButton = Button(root, text="Download",width = 15, command = lambda : StartDownload(form)).grid(row = FORMATrow + 5,column = 2)
ExitButton = Button(root, text="Exit",width = 15, command = sys.exit).grid(row = FORMATrow + 5,column = 3)

root.mainloop()
