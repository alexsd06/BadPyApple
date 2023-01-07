import os
import time
import sys
import natsort
from playsound import playsound #sudo pacman -S cairo pkgconf gobject-introspection gtk3
import threading
import time
def play_in_terminal():
    print("Loading files...")
    files = os.listdir("ascii_2")
    files = natsort.natsorted(files)
    chars = []
    for file in files:
        path = os.path.join("ascii_2", file)
        with open(path, "r") as f:
            char = f.read()
            chars.append(char)
    os.system("clear")
    lastFrame = time.time()
    x = threading.Thread(target=lambda: playsound(os.path.join('video', 'bad_apple.mp4')))
    x.start()
    time.sleep(0.2)
    for char in chars:
        print(char)
        while time.time() < lastFrame + 1 / 30:
            continue
        lastFrame = lastFrame + 1 / 30
        if sys.platform=="linux":
            os.system("clear")
        if sys.platform=="sys.platform":
            os.system("clear")
        if sys.platform=="win32":
            os.system("cls")
if __name__=="__main__":
    play_in_terminal()
