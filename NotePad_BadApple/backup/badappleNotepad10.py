#pip install toascii
#pip install pywinauto

from toascii import VideoConverter
import time
import subprocess as sp
import pyautogui

videoFileName = "badapple.mp4"
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
prevA = 0
tmp = 0
delta = 0
print("a : " + str(a) + "b : " + str(b) + "delta : " + str(delta))
while a < b:
    start = time.time()
    print("Now frame : " + str(int(a)) + "delta : " + str(delta))

    tmp = 0
    while tmp <= a - prevA : 
       pyautogui.press("enter")
       tmp += 1
    prevA = a
    delta = time.time() - start
    delay = spf - delta
    time.sleep(delay if delay > 0 else 0)
    
    a += 1 + 30 * (0 if delay > 0 else -delay)


    