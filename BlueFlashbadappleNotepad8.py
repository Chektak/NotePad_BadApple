#pip install toascii
#pip install pywinauto

from toascii import VideoConverter
import time
import os
from pywinauto import application


v = VideoConverter('badapple.mp4', 0.15, 2.0, "high", True)

print("Converting video...")
v.convert()
print("Video Conversion Complete")

a = 0.0
b = len(v.ascii_frames)

print("Notepad write Start")

fileName = "BadTxt.txt"

app = application.Application().start(r"notepad.exe")
app['Notepad'].wait('ready')

#app['Notepad'].menu_select("File->PageSetup")

#main_dlg = app.window(title='BadApple - Notepad')
main_dlg = app.UntitledNotepad
main_dlg.print_control_identifiers()

#main_dlg.wait('visible')
spf = 1 / 30
delta = 0
os.system("badapple.mp4")
while a < b:
      start = time.time()
      print("Now frame : " + str(int(a)) + "delta : " + str(delta))
      app['Notepad']['Edit'].set_edit_text(v.ascii_frames[int(a)])
      delta = time.time() - start
      delay = spf - delta
      time.sleep(delay if delay > 0 else 0)
      a += 1 + 30 * (0 if delay > 0 else -delay)

print("End")
