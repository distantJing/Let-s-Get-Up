import os

import pygame as pg
import os.path
import time
import sys

def play_music_list(music_list, volume = 0.8):
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
        while pg.mixer.music.get_busy():
            # check if playback has finished
            # print("Playing"+ music_file+"----status: " + time.strftime('%M:%S', time.localtime(pg.mixer.music.get_pos()/1000)))
            sys.stdout.write("Playing"+ music_file+"----status: " + time.strftime('%M:%S', time.localtime(pg.mixer.music.get_pos()/1000))+"\r")
            time.sleep(1)


def play_music(music_file,volume = 0.8):
    freq = 44100    # audio quality
    bitsize = -16   # unsigned 16 bit
    channels = 2    # 1 is mono, 2 is stereo
    buffer = 2048   # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bitsize, channels, buffer)

    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pg.error:
        print("File {} not found! ({})".format(music_file, pg.get_error()))
        return
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        # check if playback has finished
        # print("Playing"+ music_file+"----status: " + time.strftime('%M:%S', time.localtime(pg.mixer.music.get_pos()/1000)))
        sys.stdout.write("Playing"+ music_file+"----status: " + time.strftime('%M:%S', time.localtime(pg.mixer.music.get_pos()/1000))+"\r")
        time.sleep(1)


def music():

    music_dir = "C:/Users/82557/Music"
    play_list = []
    for item in os.listdir(music_dir):
        full_path = os.path.abspath(os.path.join(music_dir,item))
        if os.path.isdir(full_path):
            break
        else:
            if item.endswith('.mp3'):
                # play_music(full_path,0.5)
                play_list.append(full_path)
    play_music_list(play_list)   




if __name__ == "__main__":
    r, w = os.pipe()
    processid = os.fork()
    if processid:
        # parent process
        os.close(w)
        r = os.fdopen(r)
        print("parent reading ")
        str = r.read()
        print("text = ",str)
        sys.exit(0)
    else:
        # child process
        os.close(r)
        w = os.fdopen(w,'w')
        print("child writing")
        w.write("Text written by child...")
        w.close()
        print("child closing")
        sys.exit(0)
 

