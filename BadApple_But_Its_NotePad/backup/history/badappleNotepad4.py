from toascii import VideoConverter
import time
import subprocess as sp

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

spf = 1 / 60
while a < b:
      start = time.time()
      print("Now frame : " + str(a))
      f.seek(0, 0)
      f.truncate() # file clear
      c = str(v.ascii_frames[a])
      f.write(c+'\n[-]')
      
      f.flush()
      notePadProcess = sp.Popen([programName, fileName], stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
      #print(notePadProcess.poll())
      #os.system ("BadTxt.txt")
      
      #notePadProcess.wait()
      #while notePadProcess.poll() is None:
             #time.sleep(0.5)
      
      time.sleep(spf - (start - time.time()))
      notePadProcess.terminate()
      a += 1
      
print("End")
	

f.close()
#os.system ("taskkill/f/im notepad.exe")