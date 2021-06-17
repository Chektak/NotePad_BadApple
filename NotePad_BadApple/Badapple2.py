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

os.system("chcp 437")


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

isBadApple = videoFileName.endswith("badapple.mp4")
consoleVideo = None
consoleVideoScale = 0.1
if(isBadApple) :
    consoleVideo = VideoConverter(videoFileName, consoleVideoScale, 2.0, gradient)
    consoleVideo.convert()
os.system("more /c")
print(consoleVideo.ascii_frames[int(1000)].rstrip("\n")) 

sp.Popen(["notepad.exe", txtFileName], stdout=sp.PIPE, shell=True)
os.system("pause")
print("start the badapple")



sp.Popen(videoFileName, stdout=sp.PIPE, shell=True)
#time.sleep(1.35)
time.sleep(1.2)

#At this time, you need to place the mouse cursor over the notepad to play Notepad Bad Apple.

a = 0.0
aDelta = 0.0
aError = 0.0
delta = 0.0
delay = 0.0
sleepStart = 0.0
sleepError = 0.0
mouse = Controller()
mouse.scroll(0, -2) #skip header(Scroll function scrolls in a 1:3 line ratio)

isBlackConsole = True
while a < asciiFrameLength:
    start = time.time()

    # Console black and white transition
    
    if a >= 5360 and not isBlackConsole : #nitori 	 b
        print("\n")
    elif a >= 444 :
        #print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        #os.system("cls")
        print(consoleVideo.ascii_frames[int(a)].rstrip("\n")) 
    else :
        os.system("title BadApple.exe")
        print("Now frame : " + str(int(a)) + " delta : " + str(delta))

    if   not isBlackConsole and a >= 5410 : 
        os.system("color 0f")           #nitori 	    b
        isBlackConsole = not isBlackConsole
    elif isBlackConsole     and a >= 4640 and a < 5410: 
        os.system("color f0")           #aya		    w
        isBlackConsole = not isBlackConsole
    elif not isBlackConsole and a >= 4260 and a < 4640 : 
        os.system("color 0f")           #yukari         b
        isBlackConsole = not isBlackConsole
    elif isBlackConsole     and a >= 3770 and a < 4260 : 
        os.system("color f0")           #momizi         w
        isBlackConsole = not isBlackConsole
    elif not isBlackConsole and a >= 3675 and a < 3770 : 
        os.system("color 0f")           #reisen		    b
        isBlackConsole = not isBlackConsole
    elif isBlackConsole     and a >= 3650 and a < 3675 : 
        os.system("color f0")           #tewi		    w
        isBlackConsole = not isBlackConsole
    elif not isBlackConsole and a >= 3625 and a < 3647 : 
        os.system("color 0f")           #yakumo ran     b
        isBlackConsole = not isBlackConsole
    elif isBlackConsole     and a >= 3320 and a < 3625 : 
        os.system("color f0")           #kaguya	        w
        isBlackConsole = not isBlackConsole

    # elif not isBlackConsole and a >= 2490 and a < 3322: 
    #     os.system("color 0f")         #shiki	        b
    #     isBlackConsole = not isBlackConsole
    # elif not isBlackConsole and a >= 1755 and a < 3320: 
    #     os.system("color 0f")           #youmu	        b
    #     isBlackConsole = not isBlackConsole
    elif not isBlackConsole and a >= 1715 and a < 3320: 
        os.system("color 0f")           #youmu	        b
        isBlackConsole = not isBlackConsole
    elif isBlackConsole     and a >= 1685 and a < 1715 : 
        os.system("color f0")           #flandre 	    w 
        isBlackConsole = not isBlackConsole
    elif not isBlackConsole and a >= 1260 and a < 1685 : 
        os.system("color 0f")           #sakuya	        b   
        isBlackConsole = not isBlackConsole
    elif isBlackConsole     and a >= 823 and a < 1260 : 
        os.system("color f0")           #Patchouli      w
        isBlackConsole = not isBlackConsole
    elif not isBlackConsole and a >= 444 and a < 823 : 
        os.system("color 0f")           #Marisa 	    b	
        isBlackConsole = not isBlackConsole 

    mouse.scroll(0, -int((asciiVideoHeight + 6)/3)) #scroll to next frame(Scroll function scrolls in a 1:3 line ratio)
    if(aError >= 1) :#frame error correction
        mouse.scroll(0, -int((asciiVideoHeight + 6)/3) * int(aError))
        aError -= int(aError)
    #aDelta = 1 #+ 30 * (0 if delay >= 0 else -delay)
    aError += (0 if delay >= 0 else -delay) / 30
    #a += aDelta
    a += 1
    delay = spf - delta 
    delay -= sleepError #Correct the time error of the time.sleep function

    delta = time.time() - start
    
    sleepStart = time.time()
    time.sleep(delay if delay >= 0 else 0)
    sleepError = time.time() - delay - sleepStart

#print("NotePadApple End")