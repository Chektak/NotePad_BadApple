import pyautogui
import time
import subprocess as sp

videoFileName = "badapple.mp4"
txtFileName = "BadTxt.txt"
videoScale = 0.1

print("start the badapple")
#os.system("badapple.mp4")
#time.sleep(0.01)
sp.Popen(["notepad.exe", txtFileName], stdout=sp.PIPE, shell=True)
time.sleep(1)

a = 0
b = 30000
aDelta = 0
delta = 0
spf = 1/30
# print("a : " + str(a) + "b : " + str(b) + "delta : " + str(delta))
while a < b:
     start = time.time()
     #pyautogui.scroll(-int(36 + 2 + 1) * aDelta)
     wheel(WHEEL_DOWN, -int(36 + 2 + 1) * aDelta)
     delta = start - time.time()
     delay = spf - delta
     time.sleep(delay if delay > 0 else 0)
     print("Now frame : " + str(int(a)) + "delta : " + str(delta))
     #pyautogui.keyDown("enter")
     aDelta = 1 + 30 * (0 if delay > 0 else -delay)
     a += aDelta