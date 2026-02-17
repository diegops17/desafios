import pygame
from playsound3 import playsound

'''
pygame.mixer.init()
pygame.mixer.music.load('_dbz.mp3')
pygame.mixer_music.play()

while pygame.mixer.get_busy():
    pygame.time.Clock().tick(10)
'''


from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("_dbz.mp3")
play(song)

