##import libraries

from tkinter import *           ## library to import graphics and create a window
from pytube import YouTube      ## library to access youtube

##setup widget
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("TS1-youtube video downloader")

##create label
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()


##Input link from the user
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

##Download youtube video
def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()
