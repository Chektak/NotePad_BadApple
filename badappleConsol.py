from toascii import VideoConverter
import os
import time

v = VideoConverter('badapple.mp4', 0.15, 2.0, "high", True)
v.convert()

a = 0
b = len(v.ascii_frames)

f = open("BadTxt.txt", "w")

v.view()
while a < b:
      f = open("BadTxt.txt", "w")
      c = str(v.ascii_frames[a])
      f.write(c+'\n[-]')
      a += 1
      f.close()
	

f.close()