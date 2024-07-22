from pygame import mixer
import pygame
import sys
from unicurses import *

class Play:
    file = sys.argv[1]
    pygame.init()
    mixer.music.load(file)
    mixer.music.play(0)

    def play(self):
        stdscr = initscr()
        noecho()
        cbreak()
        addstr("press p to pause, press c to continue and press q to quit")
        self.playing = True
        while True:
            x = getkey()
            clear()

            match x:

                case 'p':
                    if self.playing is True:
                        mixer.music.pause()
                        self.playing = False
                    else:
                        mixer.music.unpause()
                        self.playing = True

                case 'q':
                    mixer.music.stop()

                    nocbreak()
                    keypad(stdscr, 'yes')
                    echo()
                    endwin()

                    break

                case _:
                    string = "\nno\n"
                    addstr()

stuff = Play()
stuff.play()
