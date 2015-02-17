#!/usr/bin/python
import RPi.GPIO as GPIO              # import RPi.GPIO module    
from Adafruit_I2C import Adafruit_I2C
  
# choose BOARD or BCM  
GPIO.setmode(GPIO.BCM)               # BCM for GPIO numbering  
  
# Set up Inputs  
GPIO.setup(4, GPIO.IN,  pull_up_down=GPIO.PUD_UP)   # input with pull-up   

# Configure ChronoDot SQW
chronodot = Adafruit_I2C(0x68)
chronodot.write8(0x0E,192)
result = chronodot.readU8(0x0E)
print (result)
