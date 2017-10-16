from time import sleep
import pifacedigitalio as pfd
pfd.init()

while(True):
  pfd.digital_write(0, 1)
  pfd.digital_write(1, 1)
  sleep(1)
  pfd.digital_write(0, 0)
  pfd.digital_write(1, 0)
  sleep(1)
  
