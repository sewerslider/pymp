#!/usr/bin/env python
from pygame import mixer 
import sys

file = sys.argv[1]

mixer.init() 

mixer.music.load(file)

mixer.music.play() 

while True: 
 
    query = input("  ") 

    def f(input):
        match input:
            case ' ':
                mixer.music.pause()      
            case 'q':
                mixer.music.stop() 
            case _:
                print("何")
