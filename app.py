# Music/WAV Player in Python3

from tkinter import *
# from PIL import Image, ImageTk
from pygame import mixer
from tkinter import filedialog as fd
from tkinter import messagebox as ms
from function import *
from imageloader import Imageloader
import time


#interface function
music_file = []
file_format = ['wav']
global running
running = False
global i
i = 0 #tracker of next and previous music

#for opening files
def openfile():
    playlist_box.delete(1.0, END)
    filename = fd.askopenfilenames()
    for files in filename:
        ext = files.split('.')[-1]
        if ext in file_format:
            music_file.append(files)
        else:
            ms.showinfo('Error',"Unrecognized format")
    for i in music_file:
        playlist_box.insert(1.0, i.split('/')[-1]+'\n')

#for showing current song being played
def show_notification():
    notify_label.configure(text=f"Playing {music_file[i].split('/')[-1]}")
    root.update()
    time.sleep(5)
    notify_label.configure(text='')
    root.update()

# play , pause, stop, next and previous functionalities

def play():
    mixer.init()
    wav_file = music_file[i]
    mixer.music.load(wav_file)
    mixer.music.play()
    show_notification()


def pause():
    global running
    if not running:
        mixer.music.pause()
        running = True
    else:
        mixer.music.unpause()
        running = False

def stop():
    mixer.music.stop()

# next music in the playlist
def next():
    mixer.init()
    global i
    i = i+1
    if i > len(music_file)-1:
        i = 0

    wav_file = music_file[i]
    mixer.music.load(wav_file)
    mixer.music.play()
    show_notification()

#previous music in the playlist
def previous():
    mixer.init()
    global i
    i = i-1
    if i < 0:
        i = 0

    wav_file = music_file[i]
    mixer.music.load(wav_file)
    mixer.music.play()
    show_notification()



# app interface
root = Tk()
root.geometry('500x650')
root.title('WAV Music Player')

# head frame
frame = Frame(root)
frame.pack(pady=10)

# playlist text box
playlist_box = Text(frame, width=50, height=4, fg='black', bg='white')
playlist_box.grid(row=1, column=0)


folder_icon = Imageloader.loadImage("images/folder.png", 50, 50)
player_icon = Imageloader.loadImage("images/icon1.png", 55, 55)
pause_icon = Imageloader.loadImage("images/player_pause.png", 50, 50)
stop_icon = Imageloader.loadImage("images/circle_red.png", 50, 50)
next_icon = Imageloader.loadImage("images/next.png", 50, 50)
previous_icon = Imageloader.loadImage("images/previous.png", 50, 50)
logo = Imageloader.loadImage("images/wave.png", 250, 250)

# filebrowser
filebrowser = Button(frame, image=folder_icon, borderwidth=0, command=openfile)
filebrowser.grid(row=1, column=1)

# buttons frame
button_frame = Frame(root)
button_frame.pack(pady=80)

# all buttons

previous_button = Button(button_frame, image=previous_icon,
                         borderwidth=0, command=previous)
previous_button.grid(row=0, column=0)

player_button = Button(button_frame, image=player_icon,
                       borderwidth=0, command=play)
player_button.grid(row=0, column=1)

pause_button = Button(button_frame, image=pause_icon,
                      borderwidth=0, command=pause)
pause_button.grid(row=0, column=2, padx=10)

stop_button = Button(button_frame, image=stop_icon,
                     borderwidth=0, command=stop)
stop_button.grid(row=0, column=3)

next_button = Button(button_frame, image=next_icon,
                     borderwidth=0, command=next)
next_button.grid(row=0, column=4,padx=10)


# logo frame

logo_frm = Frame(root)
logo_frm.pack(pady=5)

# logo
logo_label = Label(logo_frm, image=logo)
logo_label.grid(row=0, column=1)


# notification
notify_label = Label(logo_frm, fg='white')
notify_label.grid(row=1, column=1)

# key bindings event

root.bind('<Up>', increase_volume)
root.bind('<Down>', decrease_volume)

root.mainloop()
