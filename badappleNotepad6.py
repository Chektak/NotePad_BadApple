#pip install pywinauto
#pip install toascii

from toascii import VideoConverter
import time
import subprocess as sp
import os
from pywinauto import application

v = VideoConverter('badapple.mp4', 0.1, 2.0, "high")
print("Converting video...")
v.convert()
print("Video Conversion Complete")

a = 0
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
spf = 1 / 60
while a < b:
      start = time.time()
      app['Notepad']['Edit'].set_edit_text("")
      print("Now frame : " + str(a))
      c = str(v.ascii_frames[a])
      #main_dlg.Edit.type_keys(c + "^A",
      #                  with_spaces=True,
      #                  with_newlines=True,
      #                  pause=0.5,
      #                  with_tabs=True)
      app['Notepad']['Edit'].set_edit_text(c)
      time.sleep(spf - (start - time.time()))
      a += 1
          
print("End")
	
f.close()