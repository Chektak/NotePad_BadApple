#pip install to-ascii
#pip install pynput
#pip install subprocess

from toascii import VideoConverter
from pynput.mouse import Button, Controller
import time
import subprocess as sp
import os

videoFileName = "../badapple.mp4"
txtFileName = "BadTxt.txt"
gradient = "high"
videoScale = 0.4
a = 0.0
asciiFrameLength = 0.0
asciiVideoHeight = 0.0
fps = 30
spf = 1 / fps

#Create a text file
try:
    f = open(txtFileName, "r")
except:
    f = open(txtFileName, "w")
    f.close()

f = open(txtFileName, "r+")
header = f.readline()
print("_videoFileName=" + str(videoFileName) + "_videoScale=" + str(videoScale) + "_gradient="+str(gradient) + "_fps=" + str(fps))
if(header == "_videoFileName=" + str(videoFileName) + "_videoScale=" + str(videoScale) + "_gradient="+str(gradient) + "_fps=" + str(fps)+"\n") :
    print("It has already been converted to ASCII art.")
    f.readline()
    asciiFrameLength = int(f.readline())
    f.readline()
    asciiVideoHeight = float(f.readline())
else :
    v = VideoConverter(videoFileName, videoScale, 2.0, gradient)
    print("Converting video...")
    v.convert()
    print("Video Conversion Complete")

    print("Notepad write Start")
    asciiFrameLength = len(v.ascii_frames)
    asciiVideoHeight = v._height * videoScale

    f.write("_videoFileName="+str(videoFileName) + "_videoScale=" + str(videoScale)+ "_gradient="+str(gradient)+"_fps="+str(fps))
    f.write("\nasciiFrameLength=\n"+str(asciiFrameLength))
    f.write("\nasciiVideoHeight=\n"+str(asciiVideoHeight))
    a = 0.0
    while a < asciiFrameLength:
        c = str(v.ascii_frames[int(a)])
        f.write('\n[-]\n'+c+'\n\n\n\n\n\n\n\n\n\n\n\n\n')
        a += 1
    print("Notepad write Complete")
        
f.close()

#sp.Popen(videoFileName, stdout=sp.PIPE, shell=True)
#time.sleep(2)
sp.Popen(["notepad.exe", txtFileName], stdout=sp.PIPE, shell=True)
os.system("pause")
print("start the badapple")
time.sleep(5)

a = 0.0
aDelta = 0.0
delta = 0.0
delay = 0.0
sleepStart = 0.0
sleepError = 0.0
mouse = Controller()
mouse.scroll(0, -2) #skip header(Scroll function scrolls in a 1:3 line ratio)
while a < asciiFrameLength:
    start = time.time()
    mouse.scroll(0, -int((asciiVideoHeight + 15)/3*aDelta)) #scroll to next frame(Scroll function scrolls in a 1:3 line ratio)
    print("Now frame : " + str(int(a)) + " delta : " + str(delta))
    aDelta = 1 + 30 * (0 if delay >= 0 else -delay)
    a += aDelta
    delay = spf - delta 
    delay -= sleepError #Correct the time error of the time.sleep function

    delta = time.time() - start
    
    sleepStart = time.time()
    time.sleep(delay if delay >= 0 else 0)
    sleepError = time.time() - delay - sleepStart