from pygame import mixer 
import pygame
import curses
import sys
import time

class Play:
    file = sys.argv[1]
    pygame.init()
    mixer.music.load(file)
    mixer.music.play(0) 

    def play(self):
        self.playing = True
        while True:
            stdscr= curses.initscr()
            curses.noecho()
            curses.cbreak()
            stdscr.addstr("press p to pause, press c to continue and press q to quit")
            x = stdscr.getkey()
            stdscr.clear()

            match x:

                case 'p':
                    if self.playing == True:
                        mixer.music.pause()
                        self.playing=False
                    else:
                        mixer.music.unpause()
                        self.playing=True

                case 'q':
                    mixer.music.stop()

                    curses.nocbreak()
                    stdscr.keypad(False)
                    curses.echo()
                    curses.endwin()

                    break

stuff = Play()
stuff.play()
