from playsound import playsound
from PIL import Image
#optional to run if playsound doesn't wanna work
#import pygame

def play():
    """Play a Christmas song in the background while we see trump dance to it
    Parameters:
        None
    Return:
        None
    """
    playsound("christmas.mp3")
    #pygame.mixer.music.load("christmas.mp3")
    #pygame.mixer.music.play()