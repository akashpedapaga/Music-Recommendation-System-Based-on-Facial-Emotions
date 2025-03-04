import os
import pickle
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from pygame import mixer
import cv2
from deepface import DeepFace
import matplotlib.pyplot as plt
import random

class Playe(tk.Frame):
        def __init__(self, dominantemotion , master=None):
                super().__init__(master)
                self.master = master
                self.pack()
                mixer.init()
                self.dominantemotion=dominantemotion
                print(self.dominantemotion)
            
                """if os.path.exists('songs.pickle'):
                        with open('songs.pickle', 'rb') as f:
                                self.playlist = pickle.load(f)
                else:
                        self.playlist=[]"""
                self.playlist=[]
                self.current = 0
                self.paused = True
                self.played = False



                self.create_frames()
                self.track_widgets()
                self.control_widgets()
                self.tracklist_widgets()
                self.retrieve_songs()

        def create_frames(self):
                self.track = tk.LabelFrame(self, text='Song Track',
                                        font=("times new roman",15,"bold"),
                                        bg="grey",fg="white",bd=5,relief=tk.GROOVE)
                self.track.config(width=410,height=300)
                self.track.grid(row=0, column=0, padx=10)

                self.tracklist = tk.LabelFrame(self, text=f'PlayList - {str(len(self.playlist))}',
                                                        font=("times new roman",15,"bold"),
                                                        bg="grey",fg="white",bd=5,relief=tk.GROOVE)
                self.tracklist.config(width=190,height=400)
                self.tracklist.grid(row=0, column=1, rowspan=3, pady=5)

                self.controls = tk.LabelFrame(self,
                                                        font=("times new roman",15,"bold"),
                                                        bg="white",fg="white",bd=2,relief=tk.GROOVE)
                self.controls.config(width=410,height=80)
                self.controls.grid(row=2, column=0, pady=5, padx=10)

        def track_widgets(self):
                self.canvas = tk.Label(self.track, image=img)
                self.canvas.configure(width=400, height=240)
                self.canvas.grid(row=0,column=0)

                self.songtrack = tk.Label(self.track, font=("times new roman",16,"bold"),
                                                bg="white",fg="dark blue")
                self.songtrack['text'] = 'VFSTR MP3 Player'
                self.songtrack.config(width=30, height=1)
                self.songtrack.grid(row=1,column=0,padx=10)

        def control_widgets(self):

                self.prev = tk.Button(self.controls, image=prev)
                self.prev['command'] = self.prev_song
                self.prev.grid(row=0, column=1)

                self.pause = tk.Button(self.controls, image=pause)
                self.pause['command'] = self.pause_song
                self.pause.grid(row=0, column=2)

                self.next = tk.Button(self.controls, image=next_)
                self.next['command'] = self.next_song
                self.next.grid(row=0, column=3)

                self.volume = tk.DoubleVar(self)
                self.slider = tk.Scale(self.controls, from_ = 0, to = 10, orient = tk.HORIZONTAL)
                self.slider['variable'] = self.volume
                self.slider.set(8)
                mixer.music.set_volume(0.8)
                self.slider['command'] = self.change_volume
                self.slider.grid(row=0, column=4, padx=5)


        def tracklist_widgets(self):
                self.scrollbar = tk.Scrollbar(self.tracklist, orient=tk.VERTICAL)
                self.scrollbar.grid(row=0,column=1, rowspan=5, sticky='ns')

                self.list = tk.Listbox(self.tracklist, selectmode=tk.SINGLE,
                                         yscrollcommand=self.scrollbar.set, selectbackground='sky blue')
                self.enumerate_songs()
                self.list.config(height=22)
                self.list.bind('<Double-1>', self.play_song)

                self.scrollbar.config(command=self.list.yview)
                self.list.grid(row=0, column=0, rowspan=5)

        def retrieve_songs(self):
                self.songlist = []
                if(self.dominantemotion=='angry'):
                        directory = r'C:\Users\Akash\Desktop\songs\Angry'
                elif(self.dominantemotion=='sad'):
                        directory = r'C:\Users\Akash\Desktop\songs\Sad'
                elif(self.dominantemotion=='happy'):
                        directory = r'C:\Users\Akash\Desktop\songs\Happy'
                elif(self.dominantemotion=='neutral'):
                        directory = r'C:\Users\Akash\Desktop\songs\Neutral'
                elif(self.dominantemotion=='fear'):
                        directory = r'C:\Users\Akash\Desktop\songs\Fear'

                #filedialog.askdirectory()
                for root_, dirs, files in os.walk(directory):
                        for file in files:
                                if os.path.splitext(file)[1] == '.mp3':
                                        path = (root_ + '/' + file).replace('\\','/')
                                        self.songlist.append(path)
                self.playlist = self.songlist
                random.shuffle(self.playlist)
                self.tracklist['text'] = f'PlayList - {str(len(self.playlist))}'
                self.list.delete(0, tk.END)
                self.enumerate_songs()
                self.play_song()
        def enumerate_songs(self):
                for index, song in enumerate(self.playlist):
                        self.list.insert(index, os.path.basename(song))


        def play_song(self, event=None):
                if event is not None:
                        self.current = self.list.curselection()[0]
                        for i in range(len(self.playlist)):
                                self.list.itemconfigure(i, bg="white")

                print(self.playlist[self.current])
                mixer.music.load(self.playlist[self.current])
                self.songtrack['anchor'] = 'w'
                self.songtrack['text'] = os.path.basename(self.playlist[self.current])

                self.pause['image'] = play
                self.paused = False
                self.played = True
                self.list.activate(self.current)
                self.list.itemconfigure(self.current, bg='sky blue')

                mixer.music.play()

        def pause_song(self):
                if not self.paused:
                        self.paused = True
                        mixer.music.pause()
                        self.pause['image'] = pause
                else:
                        if self.played == False:
                                self.play_song()
                        self.paused = False
                        mixer.music.unpause()
                        self.pause['image'] = play

        def prev_song(self):
                if self.current > 0:
                        self.current -= 1
                        self.list.itemconfigure(self.current + 1, bg='white')
                else:
                        self.current = 0
                self.play_song()

        def next_song(self):
                if self.current < len(self.playlist) - 1:
                        self.list.itemconfigure(self.current, bg='white')
                        self.current += 1
                else:
                        self.current = 0
                        self.list.itemconfigure(len(self.playlist) - 1, bg='white')
                self.play_song()



        def change_volume(self, event=None):
                self.v = self.volume.get()
                mixer.music.set_volume(self.v / 10)

# ----------------------------- Main -------------------------------------------
def getemotion():
        while True:
            print("Type 'OK' to capture image")
            if(input()=="OK" or "ok" or "oK" or "Ok"):
                ret,img=cam.read()
                k=DeepFace.analyze(img,actions=['emotion'])
                plt.imshow(img)
                plt.show(block=False)
                plt.pause(2)
                plt.close()
                return k['dominant_emotion']
                break
cam=cv2.VideoCapture(0)
dominantemotion=getemotion()

root = tk.Tk()
root.geometry('600x400')
root.wm_title('VFSTR Music Recommendation System')

img = PhotoImage(master=root,file='images/music.gif')
next_ = PhotoImage(master=root,file = 'images/next.gif')
prev = PhotoImage(master=root,file='images/previous.gif')
play = PhotoImage(master=root,file='images/play.gif')
pause = PhotoImage(master=root,file='images/pause.gif')

app = Playe(dominantemotion, master=root)
app.mainloop() 
