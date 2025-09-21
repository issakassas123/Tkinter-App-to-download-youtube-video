from tkinter import Button, Entry, Label, Tk

def downloadMedia(text: str):
    root = Tk()
    root.geometry('350x550')
    title = Label(root , 
                  text = f"Download {text} file here" ,
                  fg = "white",
                  bg = "blue" , 
                  font = ('cortana' , 15 , 'italic'))
    title.pack()
    
    Link = Label(root , 
                 text = "Paste your link here" ,
                 fg = "red",
                 font = ("cortana" , 12))
    Link.pack()
    
    entryLink = Entry(root ,
                      width = 22 ,
                      font = ('cortana' , 14))
    entryLink.pack()
    
    from pytube import YouTube
    
    def d():
        link = entryLink.get()
        video = YouTube(link)
        stream = video.streams
        if text == "mp3":
            stream = stream.get_audio_only()
        elif text == "mp4":
            stream = stream.get_highest_resolution()
        stream.download()
        
    download = Button(root ,
                      text = "Download" ,
                      fg = "white",
                      bg = "red",
                      font = ("cortana" , 15 , "bold"),
                      command = d
                   )
    download.pack()
    
