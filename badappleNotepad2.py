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


spf = 1 / 60
while a < b:
      start = time.time()
      f = open("BadTxt.txt", "w")
      c = str(v.ascii_frames[a])
      f.write(c+'\n[-]')
      f.close()
      os.system ("BadTxt.txt")
      time.sleep(spf - (start - time.time()))
      a += 1
      os.system ("taskkill/f/im notepad.exe")
print("End")
	

