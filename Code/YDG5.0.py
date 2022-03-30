from tkinter import *
import tkinter.messagebox
import os
import sys

version = "5.0"
#globalformat = "Null"

def btn_clicked():
	print("Button Clicked")
def hidden():
	tkinter.messagebox.showinfo(title=None, message="Thank you for testing out my code !!!")

def convert_URL(inURL):
	start_num = 1
	if "?list" in inURL:
		startOfId = inURL.find("?list")
		startOfId = startOfId + 6
	elif "&list" in inURL:
		startOfId = inURL.find("&list")
		startOfId = startOfId + 6
	if "&index" in inURL:
		endOfId = inURL.find("&index")
		start_num = int(inURL[endOfId+7])
		print(start_num)
	elif "&t" in inURL:
		endOfId = inURL.find("&t")
	else:
		endOfId = len(inURL)
	outURL = "https://www.youtube.com/playlist?list="+inURL[startOfId:endOfId]
	return outURL,start_num

class dtos():
	def __init__(self):
		self.lan = ""
		self.format = "mp3"
		self.num = "1"
		self.upper_res = ""
		self.lower_res = ""
		self.res_list = [360,480,720,1080,1440,2160,4320]
	def set_format(self,inFormat):
		self.format = inFormat

	def get_format(self):
		print(self.format)

	def set_resolution(self,inResolution):
		self.upper_res = inResolution
		for i in self.res_list:
			if i < int(inResolution):
				self.lower_res = str(i)
		#print(" Ures: " + self.upper_res + " Lres: " + self.lower_res)
	def __str__(self):
		self.string = "lan: " + self.lan + " number: " + self.num + " format: " + self.format  + " Ures: " + self.upper_res + " Lres: " + self.lower_res
		return self.string

	def download_check(self,action):
		if action == "download":
		
			#print("hehe")
			self.lan = lan_textbox.get()
			#print(self.lan)
			#Lan = "https://www.youtube.com/playlist?list=UUM9KEEuzacwVlkt9JfJad7g"
			self.num = num_textbox.get()
			#print(self.num)
			Error = 0
			YOU = "youtube-dl -i "
			log = "--download-archive DownloadList.txt "
			FORMAT = ""
			outFolder = "--output  Downloaded/%(title)s.%(ext)s "
			#examplelink = "https://www.youtube.com/watch?v=QnDWIZuWYW0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=2"
			if len(self.lan) == 0 :
				#print("LAN is not entered correctly")
				#Warning Box
				tkinter.messagebox.showwarning(title="Warning", message="Please input link or name in the text box !!!")
			else:                              #Warning: You haven't enter the link or name box!!
				#print("Entered LAN correctly")
				try:
					int(self.num)
					
					#start if no alert
					#print("-=-=-=-=- Processing -=-=-=-=-")
					
					#this part is for Format(mp3,mp4,webm)
					if "mp3" in self.format:
						FORMAT = "--extract-audio --audio-format mp3 "
					elif "mp4" in self.format:
						if self.lower_res == "":
							tkinter.messagebox.showwarning(title="Warning", message="Please select a resolution to download !!!")
							return 0
						#FORMAT = "--format bestvideo[height>"+ self.lower_res +"][height<="+ self.upper_res +"]"#[ext=mp4]+bestaudio[ext=m4a] "
						else:
							FORMAT = "--format \"bestvideo[height>"+ self.lower_res +"][height<="+ self.upper_res +"][ext=mp4]+bestaudio[ext=m4a]\" "
					elif "webm" in self.format:
						FORMAT = "--format \"bestvideo[height>"+ self.lower_res +"][height<="+ self.upper_res +"][ext=webm]+bestaudio[ext=webm]\" "

					#this part is for LN
					if ".com" in self.lan and "youtube" not in self.lan:
						FINAL = YOU + log + FORMAT + outFolder + self.lan
					elif "youtube.com" in self.lan and "list" in self.lan:
						self.lan,start_num = convert_URL(self.lan)

						PlaylistStart = "--playlist-start "+str(start_num)+" "
						end_num = start_num - 1 + int(self.num)
						PlaylistEnd = "--playlist-end "+str(end_num)+" "
						FINAL = YOU + log + PlaylistStart + PlaylistEnd + FORMAT + outFolder + self.lan

					elif "youtube.com" in self.lan:
						FINAL = YOU + log + FORMAT + outFolder + self.lan
					else:
						search = "ytsearch"+self.num+":"+self.lan+""
						#FINAL = YOU + log + FORMAT + outFolder + search
						FINAL = YOU + log + FORMAT + outFolder + search

					if Error == 0:
						print(FINAL)
						#######################################################################################
						run = os.system(FINAL)


						if run == 0:
							tkinter.messagebox.showinfo(title="Done", message="Download process is done")
							#print('-=-=-=-=- D O N E -=-=-=-=-')
						else:
							#print(run)
							#print('-=-=-=-=- ERROR:'+ str(run) + ' -=-=-=-=-')
							tkinter.messagebox.showerror(title="Error", message="Error : " + str(run))
							
				except Exception as bug:
					tkinter.messagebox.showwarning(title="Warning", message="Please input the number of video you want to download")
					#tkinter.messagebox.showerror(title="Error", message="Error : " + str(bug))
					#print(bug)

		elif action == "check":		
			self.lan = lan_textbox.get()
			if len(self.lan) == 0 :
				#print("LAN is not entered correctly")
				tkinter.messagebox.showwarning(title="Warning", message="Please input link or name in the text box !!!")
				pass
			else:                              #Warning: You haven't enter the link or name box!!
				if ".com" in self.lan:
					FINAL = "youtube-dl -F " + self.lan
					print(FINAL)
					run = os.system(FINAL)
					print(run)
				#print("Entered LAN correctly")
				else:
					FINAL = "youtube-dl -F ytsearch:" + self.lan
					print(FINAL)
					run = os.system(FINAL)
					print(run)
			
dto = dtos()

window = Tk()
window.iconbitmap("icon.ico")
window.title("YoutubeDownloader "+ version +" by CrazyMeowl")
window.geometry("1000x500")
window.configure(bg = "#fbd8dd")
canvas = Canvas(
	window,
	bg = "#fbd8dd",
	height = 500,
	width = 1000,
	bd = 0,
	highlightthickness = 0,
	relief = "ridge")
canvas.place(x = 0, y = 0)
#Background
background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
	543.0, 325.5,
	image=background_img)

#Exit
exit_img = PhotoImage(file = f"exit.png")
exit_button = Button(
	image = exit_img,
	borderwidth = 0,
	highlightthickness = 0,
	command = lambda:exit(),
	relief = "flat")

exit_button.place(
	x = 213, y = 429,
	width = 149,
	height = 43)
#Lan
lan_img = PhotoImage(file = f"lan.png")
lan_bg = canvas.create_image(
	242.5, 71.0,
	image = lan_img)

lan_textbox = Entry(
	bd = 0,
	bg = "#c87a7a",
	highlightthickness = 0)

lan_textbox.place(
	x = 40.0, y = 55,
	width = 405.0,
	height = 30)
#num
num_img = PhotoImage(file = f"num.png")
num_bg = canvas.create_image(
	169.0, 135.0,
	image = num_img)

num_textbox = Entry(
	bd = 0,
	bg = "#c87a7a",
	highlightthickness = 0)

num_textbox.place(
	x = 40.0, y = 119,
	width = 258.0,
	height = 30)
num_textbox.insert(0,"1")

#down
down_img = PhotoImage(file = f"down.png")
down_button = Button(
	image = down_img,
	borderwidth = 0,
	highlightthickness = 0,
	command = lambda:dto.download_check("download"),
	relief = "flat"
	)

down_button.place(
	x = 32, y = 428,
	width = 149,
	height = 43)
## RESOLUTION BUTTONS
#480p
b480_img = PhotoImage(file = f"480.png")
b480 = Button(
	image = b480_img,
	borderwidth = 0,
	highlightthickness = 0,
	command = lambda:dto.set_resolution("480"),
	relief = "flat")

b480.place(
	x = 555, y = 120,
    width = 88,
    height = 35)
#720p
b720_img = PhotoImage(file = f"720.png")
b720 = Button(
	image = b720_img,
	borderwidth = 0,
	highlightthickness = 0,
	command = lambda:dto.set_resolution("720"),
	relief = "flat")

b720.place(
	x = 650, y = 120,
    width = 88,
    height = 35)

b1080_img = PhotoImage(file = f"1080.png")
b1080 = Button(
	image = b1080_img,
	borderwidth = 0,
	highlightthickness = 0,
	command = lambda:dto.set_resolution("1080"),
	relief = "flat")

b1080.place(
	x = 745, y = 120,
    width = 151,
    height = 35)
#1440p
b1440_img = PhotoImage(file = f"1440.png")
b1440 = Button(
	image = b1440_img,
	borderwidth = 0,
	highlightthickness = 0,
	command = lambda:dto.set_resolution("1440"),
	relief = "flat")

b1440.place(
	x = 555, y = 170,
    width = 159,
    height = 37)
#2160p
b2160_img = PhotoImage(file = f"2160.png")
b2160 = Button(
	image = b2160_img,
	borderwidth = 0,
	highlightthickness = 0,
	command = lambda:dto.set_resolution("2160"),
	relief = "flat")

b2160.place(
	x = 725, y = 170,
    width = 145,
    height = 37)

b4320_img = PhotoImage(file = f"4320.png")
b4320 = Button(
    image = b4320_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:dto.set_resolution("4320"),
    relief = "flat")

b4320.place(
    x = 555, y = 220,
    width = 157,
    height = 39)

## FORMAT BUTTONS
#mp3
mp3_img = PhotoImage(file = f"mp3.png")
mp3_button = Button(
	image = mp3_img,
	borderwidth = 0,
	highlightthickness = 0,
	command = lambda:dto.set_format("mp3"),
	relief = "flat")

mp3_button.place(
	x = 552, y = 55,
	width = 74,
	height = 32)
#mp4
mp4_img = PhotoImage(file = f"mp4.png")
mp4_button = Button(
	image = mp4_img,
	borderwidth = 0,
	highlightthickness = 0,
	command = lambda:dto.set_format("mp4"),
	relief = "flat")

mp4_button.place(
	x = 632, y = 55,
	width = 74,
	height = 32)
#webm
webm_img = PhotoImage(file = f"webm.png")
webm_button = Button(
	image = webm_img,
	borderwidth = 0,
	highlightthickness = 0,
	command = lambda:dto.set_format("webm"),
	relief = "flat")

webm_button.place(
	x = 714, y = 55,
	width = 88,
	height = 32)

check_img = PhotoImage(file = f"check.png")
check_button = Button(
    image = check_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:dto.download_check("check"),
    relief = "flat")

check_button.place(
    x = 397, y = 387,
    width = 149,
    height = 43)

#hidden button
hidden_img = PhotoImage(file = f"hidden.png")
hidden_button = Button(
    image = hidden_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = hidden,
    relief = "flat")

hidden_button.place(
    x = 919, y = 417,
    width = 84,
    height = 84)

window.resizable(False, False)
window.mainloop()
