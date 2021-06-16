from pynput.mouse import Button, Controller
import time
import subprocess as sp

videoFileName = "badapple.mp4"
txtFileName = "BadTxt.txt"
videoScale = 0.1
mouse = Controller()

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
mouse.scroll(0, -int((36 + 3)/3)) #Scroll function scrolls in a 1:3 line ratio

start = time.time()
time.sleep(0.1)
ms = time.time() - start
start = time.time()
time.sleep(5)
s = time.time() - start
print("ms" + str(ms) + " s" + str(s))


#while a < b:
#     start = time.time()
#     #pyautogui.scroll(-int(36 + 2 + 1) * aDelta)
#     mouse.scroll(0, -int(36 + 2 + 1) * aDelta)
#     delta = start - time.time()
#     delay = spf - delta
#     time.sleep(delay if delay > 0 else 0)
#     print("Now frame : " + str(int(a)) + "delta : " + str(delta))
#     #pyautogui.keyDown("enter")
#     aDelta = 1 + 30 * (0 if delay > 0 else -delay)
#     a += aDelta