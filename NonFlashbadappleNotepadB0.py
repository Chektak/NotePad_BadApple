#pip install to-ascii
#pip install pynput
#pip install subprocess

from toascii import VideoConverter
from pynput.mouse import Button, Controller
import time
import subprocess as sp
import os
videoFileName = "badapple.mp4"
txtFileName = "BadTxt.txt"
videoScale = 0.1
v = VideoConverter(videoFileName, videoScale, 2.0, "high")
print("Converting video...")
v.convert()
print("Video Conversion Complete")

print("Notepad write Start")
f = open(txtFileName, "w")
a = 0.0
b = len(v.ascii_frames)
spf = 1 / 30
while a < b:
    c = str(v.ascii_frames[int(a)])
    f.write('\n[-]\n'+c+'\n\n\n\n\n\n\n\n\n\n\n\n\n')
    a += 1
f.close()
print("Notepad write Complete")

print("start the badapple")
#sp.Popen(videoFileName, stdout=sp.PIPE, shell=True)
#time.sleep(2)
sp.Popen(["notepad.exe", txtFileName], stdout=sp.PIPE, shell=True)
time.sleep(0.2)

a = 0.0
aDelta = 0.0
delta = 0.0
delay = 0.0
sleepStart = 0.0
sleepError = 0.0
asciiVideoHeight = v._height * videoScale
mouse = Controller()
while a < b:
    start = time.time()
    mouse.scroll(0, -int((asciiVideoHeight + 15)/3*aDelta)) #Scroll function scrolls in a 1:3 line ratio
    print("Now frame : " + str(int(a)) + " delta : " + str(delta))
    aDelta = 1 + 30 * (0 if delay >= 0 else -delay)
    a += aDelta
    delay = spf - delta 
    delay -= sleepError #Correct the time error of the time.sleep function

    delta = time.time() - start
    
    sleepStart = time.time()
    time.sleep(delay if delay >= 0 else 0)
    sleepError = time.time() - delay - sleepStart