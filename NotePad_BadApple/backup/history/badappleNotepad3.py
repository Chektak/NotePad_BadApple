from toascii import VideoConverter
import time
import os

v = VideoConverter('badapple.mp4', 0.1, 2.0, "high")
print("Converting video...")
v.convert()
print("Video Conversion Complete")

a = 0
b = len(v.ascii_frames)

print("Notepad write Start")
f = open("BadTxt.txt", "w")

spf = 1 / 60
while a < b:
      start = time.time()
      f.seek(0, 0)
      f.truncate() # file clear
      c = str(v.ascii_frames[a])
      f.write(c+'\n[-]')
      
      f.flush()
      os.system ("BadTxt.txt")
      time.sleep(spf - (start - time.time()))
      a += 1
      
print("End")
	

f.close()
os.system ("taskkill/f/im notepad.exe")