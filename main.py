from tkinter import Button, Label, Tk
from info import downloadMedia

app = Tk()

app.geometry('400x600')

title = Label(app , text = "Youtube Downloader" , 
              fg = "white" ,
              bg = "red",
              font = ('cortana' , 18 , 'bold')
              )
title.pack()

mp3 = Button(app ,
             text = "Download mp3" ,
             fg = "white" , 
             bg = "blue",
             font = ('cortana' , 13 , 'bold'),
             command = lambda: downloadMedia('mp3')
             )
mp3.pack()

mp4 = Button(app , 
             text = "Download mp4" , 
             fg = "white" , 
             bg = "green",
             font = ('cortana' , 13 , 'bold'),
             command = lambda: downloadMedia('mp4')
             )
mp4.pack()

app.mainloop()
