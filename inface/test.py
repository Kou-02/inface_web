from playsound import playsound
import os

cwd = os.getcwd()
music = os.path.join(cwd,'done.mp3')
playsound(music)