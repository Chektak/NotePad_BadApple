#pip install toascii
#pip install pywinauto
#pip install clipboard

from toascii import VideoConverter
import time
import os
import pyautogui
import clipboard
v = VideoConverter('badapple.mp4', 0.1, 2.0, "high", True)

print("Converting video...")
v.convert()
print("Video Conversion Complete")

a = 0.0
b = len(v.ascii_frames)

print("Notepad write Start")

spf = 1 / 30
delta = 0


pyautogui.hotkey("win","r")
time.sleep(0.1)
pyautogui.write("notepad.exe")
pyautogui.press("enter")
time.sleep(1)
os.system("badapple.mp4")
pyautogui.hotkey("alt", "tab")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "z")

while a < b:
    start = time.time()
    print("Now frame : " + str(int(a)) + "delta : " + str(delta))
    #app['Notepad']['Edit'].set_edit_text(v.ascii_frames[int(a)])
    
    clipboard.copy(v.ascii_frames[int(a)])
    pyautogui.hotkey("ctrl", "v")
    
    delta = time.time() - start
    delay = spf - delta
    time.sleep(delay if delay > 0 else 0)
    a += 1 + 30 * (0 if delay > 0 else -delay)
    pyautogui.hotkey("ctrl", "z")
    
print("End")