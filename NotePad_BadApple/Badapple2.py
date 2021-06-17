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
consoleVideo = None
consoleVideoScale = 0.1
if(isBadApple) :
    consoleVideo = VideoConverter(videoFileName, consoleVideoScale, 2.0, gradient)
    consoleVideo.convert()
sp.Popen(["notepad.exe", txtFileName], stdout=sp.PIPE, shell=True)

os.system("pause")
print("start the badapple")



sp.Popen(videoFileName, stdout=sp.PIPE, shell=True)
time.sleep(1.35)

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

consoleState = 0
while a < asciiFrameLength:
    start = time.time()
    mouse.scroll(0, -int((asciiVideoHeight + 6)/3)) #scroll to next frame(Scroll function scrolls in a 1:3 line ratio)
    if(aError >= 1) :#frame error correction
        mouse.scroll(0, -int((asciiVideoHeight + 6)/3) * int(aError))
        aError -= int(aError)
    if a >= 386:
        if a >= 436 :
            #os.system("cls")
            if consoleState == 0 :
                #os.system("color 70") #colsole white
                os.system("color 0f") #colsole black
                consoleState = 1
            else:
                if(a >= 800):
                    if(consoleState == 1):
                        os.system("color f0") #colsole white
                        consoleState = 2
                    else :
                        if(a >= 1255) :
                            if(consoleState == 2):
                                os.system("color 0f") #colsole black(basic)
                                consoleState = 3
                            else:
                                if(a >= 1680) :
                                    if(consoleState == 3):
                                        os.system("color f0") #colsole white
                                        consoleState = 4
                                    else :
                                        if (a >= 2445) :
                                            if (a >= 2495) :
                                                if consoleState == 4 :
                                                    os.system("color 0f") #colsole black(basic)
                                                    consoleState = 5
                                                else :
                                                    if (a >= 3277) :
                                                        if (a >= 3327) :
                                                            if (consoleState == 5) :
                                                                os.system("color f0") #colsole white
                                                                consoleState = 6
                                                            else :
                                                                if (a >= 5360) :
                                                                    if(a >= 5410) :
                                                                        if (consoleState == 6) :
                                                                            os.system("color 0f") #colsole black
                                                                            consoleState = 7
                                                                        else :
                                                                            print(consoleVideo.ascii_frames[int(a)].rstrip("\n")) 
                                                                    else :
                                                                        print("\n")
                                                                else :
                                                                   #print(consoleVideo.ascii_frames[int(a)].rstrip("\n")) 
                                                                   print("Now frame : " + str(int(a)) + " delta : " + str(delta))
                                                        else :
                                                            #print("\n")
                                                            print(consoleVideo.ascii_frames[int(a)].rstrip("\n"))
                                                            #print("Now frame : " + str(int(a)) + " delta : " + str(delta))
                                                    else :
                                                        print(consoleVideo.ascii_frames[int(a)].rstrip("\n"))
                                                        #print("Now frame : " + str(int(a)) + " delta : " + str(delta))
                                            else :
                                                print("\n")
                                                #print(consoleVideo.ascii_frames[int(a)].rstrip("\n"))
                                                #print("Now frame : " + str(int(a)) + " delta : " + str(delta))
                                        else :
                                            print(consoleVideo.ascii_frames[int(a)].rstrip("\n"))
                                            #print("Now frame : " + str(int(a)) + " delta : " + str(delta))
                                else :
                                    print(consoleVideo.ascii_frames[int(a)].rstrip("\n"))       
                        else :
                            print(consoleVideo.ascii_frames[int(a)].rstrip("\n"))
                else :
                    print(consoleVideo.ascii_frames[int(a)].rstrip("\n"))
        else :
            print("\n")
    else :
        print("Now frame : " + str(int(a)) + " delta : " + str(delta))

    #aDelta = 1 #+ 30 * (0 if delay >= 0 else -delay)
    aError += 30 * (0 if delay >= 0 else -delay)
    #a += aDelta
    a += 1
    delay = spf - delta 
    delay -= sleepError #Correct the time error of the time.sleep function

    delta = time.time() - start
    
    sleepStart = time.time()
    time.sleep(delay if delay >= 0 else 0)
    sleepError = time.time() - delay - sleepStart

#print("NotePadApple End")