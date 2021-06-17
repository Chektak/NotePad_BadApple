#pip install to-ascii
#pip install pywinauto

from toascii import VideoConverter
import time
import os
from pywinauto import application
from pywinauto import mouse

mouse.scroll((0, 1), 1000)
      #app['Notepad']['Edit'].set_edit_text(v.ascii_frames[int(a)])
      #delta = time.time() - start
      #delay = spf - delta
      #time.sleep(delay if delay > 0 else 0)
      #a += 1 + 30 * (0 if delay > 0 else -delay)

print("End")
