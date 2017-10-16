from time import sleep
import pifacedigitalio as p
p.init()

while(True):
  print("waiting")
  if(p.digital_read(2)):
    print("Switch 2 was pressed")
