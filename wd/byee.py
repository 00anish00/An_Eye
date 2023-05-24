import pygame

def playsound(filepath):
    pygame.mixer.init()
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()

# Provide the path to your MP3 file
sfile = "wd\\Jai Shree Ram.mp3"

playsound(sfile)
