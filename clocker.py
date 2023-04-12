import time
import os
from os import system as shell
from pygame import mixer
mixer.init()
clear = lambda: shell("clear || cls")
def main():
    print("\033[31m\033[")
    for l in "Hello! Enter the number of seccond after which the alarm should go off":
        print(l, end="", flush=True)
        time.sleep(0.04)
    clear()
    seccond = float(input("Enter the number of seconds>>"))
    for u in "Okay, wait...":
        print(u, end="", flush=True)
        time.sleep(0.04)
    time.sleep(seccond)
    mixer.music.load("clock.mp3")
    mixer.music.play()
    while True:
        clear()
        print("WAKE UP!!!!")
        time.sleep(13)
        mixer.music.play()
main()
