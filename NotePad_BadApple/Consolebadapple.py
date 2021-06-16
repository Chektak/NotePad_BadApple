#pip install to-ascii

from toascii import VideoConverter
import os
import time

v = VideoConverter('../badapple.mp4', 0.1, 2.0, "high", True)
print("Converting video...")
v.convert()
print("Video Conversion Complete")

v.view()
