import pygame
import customtkinter as ctk


pygame.mixer.init()


app = ctk.CTk()
app.title("music player")
app.geometry("400x500")


#DEF

def play_music():
    pass

def stop_music():
    pass

def next_song():
    pass

def previous_song():
    pass


#btn

play_button = ctk.CTkButton(app, text="play",fg_color="#603d6e",hover_color="#846262",  command=play_music)
play_button.pack(pady=5)

stop_button = ctk.CTkButton(app, text="stop",fg_color="#603d6e",hover_color="#846262",  command=stop_music)
stop_button.pack(pady=5)

next_button = ctk.CTkButton(app, text="next",fg_color="#603d6e",hover_color="#846262",  command=next_song)
next_button.pack(pady=5)

prev_button = ctk.CTkButton(app, text="previous",fg_color="#603d6e",hover_color="#846262",  command=previous_song)
prev_button.pack(pady=5)

app.mainloop() 