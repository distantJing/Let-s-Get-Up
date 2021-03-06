import pygame as pg
import os.path
import time
import sys



def paly(music_list, volume=0.8):
    freq = 44100    # audio quality
    bitsize = -16   # unsigned 16 bit
    channels = 2    # 1 is mono, 2 is stereo
    buffer = 2048   # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bitsize, channels, buffer)

    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    for music_file in music_list:
        try:
            pg.mixer.music.load(music_file)
            print("Music file {} loaded!".format(music_file))
        except pg.error:
            print("File {} not found! ({})".format(music_file, pg.get_error()))
            return
        pg.mixer.music.play()

def stop():
    pg.mixer.stop()