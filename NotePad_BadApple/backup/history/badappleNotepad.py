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
      
      c = str(v.ascii_frames[a])
      f.write(c+'\n[-]')
      
      f.flush()
      os.system ("BadTxt.txt")
      time.sleep(spf - (start - time.time()))
      f.truncate(f.tell()) # tell returns current position of file read/write pointer
      a += 1
      os.system ("taskkill/f/im notepad.exe")
print("End")
	

f.close()