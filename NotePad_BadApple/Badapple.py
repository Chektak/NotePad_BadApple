#pip install to-ascii
#pip install pynput
#pip install subprocess

from toascii import VideoConverter
from pynput.mouse import Button, Controller
import time
import subprocess as sp
import os

videoFileName = "C:/Users/dbstn/Desktop/PythonBadApple/badapple.mp4"
txtFileName = "BadApple.txt"
gradient = "high"
videoScale = 0.15
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
    f.close()
    f = open(txtFileName, "w+")
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
        f.write('\n[-]\n'+c+'\n\n\n\n')
        a += 1
    print("Notepad write Complete")
        
f.close()

#sp.Popen(videoFileName, stdout=sp.PIPE, shell=True)
#time.sleep(2)

isBadApple = videoFileName.endswith("badapple.mp4")
isPlayingConsoleWhiteApple = False
isPlayingConsoleBlackApple = False
consoleVideo = None
consoleVideoScale = 0.1
if(isBadApple) :
    consoleVideo = VideoConverter(videoFileName, consoleVideoScale, 2.0, gradient)
    consoleVideo.convert()
sp.Popen(["notepad.exe", txtFileName], stdout=sp.PIPE, shell=True)

os.system("pause")
print("start the badapple")



sp.Popen(videoFileName, stdout=sp.PIPE, shell=True)
time.sleep(0.8)

#At this time, you need to place the mouse cursor over the notepad to play Notepad Bad Apple.

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
    mouse.scroll(0, -int((asciiVideoHeight + 6)/3*aDelta)) #scroll to next frame(Scroll function scrolls in a 1:3 line ratio)
    if (isBadApple == True and a > 3327) :
        if not isPlayingConsoleWhiteApple :
            isPlayingConsoleWhiteApple = True
            os.system("color 70") #colsole white
            os.system("console.exe is being controlled by a bad apple")
            #os.system("mode con:cols=" + str(int(140)) + " lines" + str(int(9000)))
        
        if (not isPlayingConsoleBlackApple and a > 5370) :
            print("\n")
            if a > 5410 :
                os.system("color 07") #colsole basic
                isPlayingConsoleBlackApple = True
        else :
            #os.system("cls")
            print("Now frame : " + str(int(a)) + " delta : " + str(delta))
            #print("\n"+consoleVideo.ascii_frames[int(a)])
    else :
        if a <= 3290:
            print("Now frame : " + str(int(a)) + " delta : " + str(delta))
        else :
            print("\n")
    aDelta = 1 + 30 * (0 if delay >= 0 else -delay)
    a += aDelta
    delay = spf - delta 
    delay -= sleepError #Correct the time error of the time.sleep function

    delta = time.time() - start
    
    sleepStart = time.time()
    time.sleep(delay if delay >= 0 else 0)
    sleepError = time.time() - delay - sleepStart

#print("NotePadApple End")