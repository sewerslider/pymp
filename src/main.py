#!/usr/bin/env python
from pygame import mixer 
import sys

file = sys.argv[1]

mixer.init() 

mixer.music.load(file)

mixer.music.play() 

while True: 
 
    query = input("control: ") 

    match query:
        case 'p':
            mixer.music.pause()      
        case 'c':
            mixer.music.unpause()
        case 'q':
            mixer.music.stop() 
            break
        case _:
            print("何")
