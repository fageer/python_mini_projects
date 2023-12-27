from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import threading


root = Tk()
root.title("Youtube Download")
root.geometry("600x400")
root.resizable(FALSE, FALSE)


#my functions
def browse():
    directory = filedialog.askdirectory(title="Save Vedio")
    folderlink.delete(0, "end")
    folderlink.insert(0, directory)


def download_yt():
    status.config(text="Status: Downloading...")
    link = ytlink.get()
    folder = folderlink.get()
    YouTube(link, on_complete_callback=done).streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(folder)


def done(stream=None, chunk=None, file_handle=None, remaining=None):
    status.config(text="Status: Done.")


#youtube logo
ytlogo = PhotoImage(file="youtube download app/images/youtube.png").subsample(2)

yttitle = Label(root, image=ytlogo)
yttitle.place(relx=0.5, rely=0.25, anchor="center")


#youtube link
ytlabel = Label(root, text="Youtube Link:")
ytlabel.place(x=25, y=150)

ytlink = Entry(root, width=60)
ytlink.place(x=140, y=150)


#download folder
folderlabel = Label(root, text="Download Folder:")
folderlabel.place(x=25, y=183)

folderlink = Entry(root, width=50)
folderlink.place(x=140, y=183)


#browse button
browse = Button(root, text="Browse", command=browse)
browse.place(x=455, y=180)


#download button
download = Button(root, text="Download", command=threading.Thread(target=download_yt).start)
download.place(x=280, y=220)


#status bar
status = Label(root, text="Status: Ready.", font="inter 10 italic", fg="black", bg="white", anchor="w")
status.place(rely=1, anchor="sw", relwidth=1)


root.mainloop()
