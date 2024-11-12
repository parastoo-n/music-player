import pygame
import customtkinter as ctk
from tkinter import Listbox, END, TclError

pygame.mixer.init()


app = ctk.CTk()
app.title("music player")
app.geometry("400x500")



current_song = ""
volume = 0

songs = ["music/Reza-Bahram.mp3", "music/Reza.b-kash.mp3", "music/Shaho.h-Disan.mp3", "music/Amin Rostami Joonam.mp3", "music/Reza Bahram Hame Raftand.mp3"]
song_listbox = Listbox(app)
for song in songs:
    song_listbox.insert(END, song)
song_listbox.pack(pady=20)


#DEF

def play_music():
    global current_song
    try:
        selected_song = song_listbox.get(song_listbox.curselection())
        pygame.mixer.music.load(selected_song)
        pygame.mixer.music.play()
        current_song = selected_song
        update_song_label()
        app.after(int(pygame.mixer.Sound(selected_song).get_length() * 1000), next_song) 
    except TclError:
           print("no song selected")

def stop_music():
    pygame.mixer.music.stop()
    global current_song
    current_song = ""
    update_song_label()

def next_song():
    try:
        current_index = song_listbox.curselection()[0]
    except IndexError:
        current_index = -1
    next_index = (current_index + 1) % song_listbox.size()
    song_listbox.selection_clear(0, END)
    song_listbox.select_set(next_index)
    song_listbox.event_generate("<<ListboxSelect>>")
    play_music()


def previous_song():
    try:
        current_index = song_listbox.curselection()[0]
    except IndexError:
        current_index = -1
    next_index = (current_index + 1) % song_listbox.size()
    song_listbox.selection_clear(0, END)
    song_listbox.select_set(next_index)
    song_listbox.event_generate("<<ListboxSelect>>")
    play_music()

def set_volume(val):
    global volume
    volume = float(val)  
    pygame.mixer.music.set_volume(volume)

def update_song_label():
    song_label.configure(text=f"is playing: {current_song}")

#btn

play_button = ctk.CTkButton(app, text="play",fg_color="#603d6e",hover_color="#846262",  command=play_music)
play_button.pack(pady=5)

stop_button = ctk.CTkButton(app, text="stop",fg_color="#603d6e",hover_color="#846262",  command=stop_music)
stop_button.pack(pady=5)

next_button = ctk.CTkButton(app, text="next",fg_color="#603d6e",hover_color="#846262",  command=next_song)
next_button.pack(pady=5)

prev_button = ctk.CTkButton(app, text="previous",fg_color="#603d6e",hover_color="#846262",  command=previous_song)
prev_button.pack(pady=5)

#LABEL

song_label = ctk.CTkLabel(app, text="", font=("Helvetica",  12, "bold"))
song_label.pack(pady=10)

#Slider Volum

volume_slider = ctk.CTkSlider(app, from_=0, to=1, command=set_volume)
volume_slider.set(volume) 
volume_slider.pack(pady=20)

app.mainloop() 