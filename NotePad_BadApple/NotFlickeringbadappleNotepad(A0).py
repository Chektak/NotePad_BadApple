#pip install to-ascii
#pip install pyautogui
#pip install subprocess

from toascii import VideoConverter
import time
import subprocess as sp
import pyautogui

videoFileName = "../badapple.mp4"
txtFileName = "BadTxt.txt"

v = VideoConverter(videoFileName, 0.1, 2.0, "high")
print("Converting video...")
v.convert()
print("Video Conversion Complete")

print("Notepad write Start")
f = open(txtFileName, "w")
a = 0
b = len(v.ascii_frames)
spf = 1 / 30
while a < b:
     c = str(v.ascii_frames[a])
     f.write('[-]\n'+c+'\n')
     a += 1
f.close()
print("Notepad write Complete")

print("start the badapple")
sp.Popen(["notepad.exe", txtFileName], stdout=sp.PIPE, shell=True)
time.sleep(1)
pyautogui.hotkey("ctrl", "f")
pyautogui.write("[-]")
time.sleep(3)

a = 0
delta = 0
# print("a : " + str(a) + "b : " + str(b) + "delta : " + str(delta))
while a < b:
    start = time.time()
    pyautogui.press('enter', presses=int(30))
    delta = start - time.time()
    #time.sleep(1 - delta)
    print("Now frame : " + str(int(a)) + "delta : " + str(delta))
    #pyautogui.keyDown("enter")
    a += 30
