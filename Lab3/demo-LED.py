from time import sleep
import pifacedifitalio as pfd
pfd.init()

while(True):
  pfd.digital_write(0, 1)
  sleep(1)
  pfd.digital_write(1, 1)
  sleep(1)
  pfd.digital_write(2, 1)
  sleep(1)
  pfd.digital_write(3, 1)
  sleep(1)
  pfd.digital_write(4, 1)
  sleep(1)
  pfd.digital_write(5, 1)
  sleep(1)
  pfd.digital_write(6, 1)
  sleep(1)
  pfd.digital_write(7, 1)
  sleep(1)
  pfd.digital_write(7, 0)
  sleep(1)
  pfd.digital_write(6, 0)
  sleep(1)
  pfd.digital_write(5, 0)
  sleep(1)
  pfd.digital_write(4, 0)
  sleep(1)
  pfd.digital_write(3, 0)
  sleep(1)
  pfd.digital_write(2, 0)
  sleep(1)
  pfd.digital_write(1, 0)
  sleep(1)
  pfd.digital_write(0, 0)
  sleep(1)
