from toascii import VideoConverter
import time
import subprocess as sp
import os

v = VideoConverter('badapple.mp4', 0.1, 2.0, "high")
print("Converting video...")
v.convert()
print("Video Conversion Complete")

a = 0
b = len(v.ascii_frames)

print("Notepad write Start")

programName = "notepad.exe"
fileName = "BadTxt.txt"

f = open(fileName, "w")

spf = 1 / 20
while a < b:
      start = time.time()
      #if a % 10 == 1 :
      sp.call("taskkill /IM notepad.exe")
      print("Now frame : " + str(a))
      f.seek(0, 0)
      f.truncate() # file clear
      c = str(v.ascii_frames[a])
      f.write(c+'\n[-]')
      
      f.flush()
      notePadProcess = sp.Popen([programName, fileName], stdout=sp.PIPE, shell=True)

      time.sleep(spf - (start - time.time()))
      #sp.call("taskkill /IM notepad.exe")      

      #notePadProcess.kill()
      #notePadProcess.terminate()
      #os.killpg(os.getpgid(notePadProcess.pid), signal.SIGTERM)  # Send the signal to all the process groups
      a += 1

          
print("End")
	

f.close()
#os.system ("taskkill/f/im notepad.exe")