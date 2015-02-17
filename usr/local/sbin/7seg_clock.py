#!/usr/bin/python

import time
import datetime
from Adafruit_7Segment import SevenSegment

# ===========================================================================
# Clock Example
# ===========================================================================
hourmin = SevenSegment(address=0x70)
secmilli = SevenSegment(address=0x71)
year = SevenSegment(address=0x72)
days = SevenSegment(address=0x73)

digits = [ 0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F, \
           0x77, 0x7C, 0x39, 0x5E, 0x79, 0x71 ]

dotdigits = [ 0xBF, 0x86, 0xDB, 0xCF, 0xE6, 0xED, 0xFD, 0x87, 0xFF, 0xEF, \
              0xF7, 0xFC, 0xA9, 0xDE, 0xF9, 0xF1 ]

print "Press CTRL+Z to exit"

# Activate Colon
hourmin.setColon(1)              
secmilli.setColon(0)              
days.setColon(0)
year.setColon(0)

# set Brightness
bright = 15
year.setBrightness(bright)
days.setBrightness(bright)
hourmin.setBrightness(bright)
secmilli.setBrightness(bright)


now = datetime.datetime.now()

#This part of the year won't change that often
year.writeDigit(0, int(now.year/1000))     # Millenia
year.writeDigit(1, int((now.year % 1000) / 100))          # Century
year.writeDigit(3, int((now.year % 100) / 10))     # Decade
year.writeDigitRaw(4, dotdigits[now.year % 10])          # Year
days.writeDigit(0, int(now.month / 10))     # Tens
days.writeDigitRaw(1, dotdigits[now.month % 10])          
days.writeDigit(0, int(now.month / 10))     # Tens
days.writeDigitRaw(1, dotdigits[now.month % 10])          
days.writeDigit(3, int(now.day / 10))   # Tens
days.writeDigit(4, now.day % 10)        # Ones
hourmin.writeDigit(0, int(now.hour / 10))     # Tens
hourmin.writeDigit(1, now.hour % 10)          # Ones
hourmin.writeDigit(3, int(now.minute / 10))   # Tens
hourmin.writeDigitRaw(4, dotdigits[now.minute % 10])          # Ones


# Continually update the time on a 4 char, 7-segment display
while(True):
  now = datetime.datetime.now()
  hour = now.hour
  minute = now.minute
  second = now.second

  # Set Year
  if(now.month==1 and now.day==1 and now.hour==0 and now.minute==0 and now.second==0):
      year.writeDigitRaw(4, dotdigits[now.year % 10])          # Year
  
  # Set month
  if(now.day==1 and now.hour==0 and now.minute==0 and now.second==0):
      days.writeDigit(0, int(now.month / 10))     # Tens
      days.writeDigitRaw(1, dotdigits[now.month % 10])          

  #Adjust brightness
  if((now.hour == 18 or now.hour == 5) and now.minute == 30 and now.second == 0):
    bright = 15
    year.setBrightness(bright)
    days.setBrightness(bright)
    hourmin.setBrightness(bright)
    secmilli.setBrightness(bright)

  elif((now.hour == 19 or now.hour == 5) and now.minute == 0 and now.second == 0):
    bright = 14
    year.setBrightness(bright)
    days.setBrightness(bright)
    hourmin.setBrightness(bright)
    secmilli.setBrightness(bright)

  elif((now.hour == 19 or now.hour == 4) and now.minute == 30 and now.second == 0):
    bright = 8
    year.setBrightness(bright)
    days.setBrightness(bright)
    hourmin.setBrightness(bright)
    secmilli.setBrightness(bright)

  elif((now.hour == 20 or now.hour == 4) and now.minute == 0  and now.second == 0):
    bright = 7
    year.setBrightness(bright)
    days.setBrightness(bright)
    hourmin.setBrightness(bright)
    secmilli.setBrightness(bright)

  elif((now.hour == 20 or now.hour == 3) and now.minute == 30 and now.second == 0):
    bright = 7
    year.setBrightness(bright)
    days.setBrightness(bright)
    hourmin.setBrightness(bright)
    secmilli.setBrightness(bright)

  elif((now.hour == 21 or now.hour == 3) and now.minute == 0 and now.second == 0):
    bright = 4
    year.setBrightness(bright)
    days.setBrightness(bright)
    hourmin.setBrightness(bright)
    secmilli.setBrightness(bright)

  elif((now.hour == 21 or now.hour == 2) and now.minute == 30 and now.second == 0):
    bright = 1
    year.setBrightness(bright)
    days.setBrightness(bright)
    hourmin.setBrightness(bright)
    secmilli.setBrightness(bright)

  elif((now.hour == 22 or now.hour == 2) and now.minute == 0 and now.second == 0):
    bright = 1
    year.setBrightness(bright)
    days.setBrightness(bright)
    hourmin.setBrightness(bright)
    secmilli.setBrightness(bright)

  elif((now.hour == 22 or now.hour == 1) and now.minute == 30 and now.second ==0 ):
    bright = 1
    year.setBrightness(bright)
    days.setBrightness(bright)
    hourmin.setBrightness(bright)
    secmilli.setBrightness(bright)

  elif((now.hour == 23 or now.hour == 1) and now.minute == 0 and now.second == 0):
    bright = 1
    year.setBrightness(bright)
    days.setBrightness(bright)
    hourmin.setBrightness(bright)
    secmilli.setBrightness(bright)

  elif((now.hour == 23 or now.hour == 0) and now.minute == 30 and now.second == 0):
    bright = 0
    year.setBrightness(bright)
    days.setBrightness(bright)
    hourmin.setBrightness(bright)
    secmilli.setBrightness(bright)

  elif(now.hour == 0 and now.minute == 0 and now.second == 0):
    bright = 0
    year.setBrightness(bright)
    days.setBrightness(bright)
    hourmin.setBrightness(bright)
    secmilli.setBrightness(bright)



  
  # Set day
  if(now.hour==0 and now.minute==0):
    days.writeDigit(3, int(now.day / 10))   # Tens
    days.writeDigit(4, now.day % 10)        # Ones

  # Set hours
  if(now.minute==0 and now.second==0):
    hourmin.writeDigit(0, int(hour / 10))     # Tens
    hourmin.writeDigit(1, hour % 10)          # Ones

  # Set minutes
  if(now.second==0):
    hourmin.writeDigit(3, int(minute / 10))   # Tens
#  hourmin.writeDigit(4, minute % 10)        # Ones
    hourmin.writeDigitRaw(4, dotdigits[minute % 10])          # Ones

  # Set seconds
  secmilli.writeDigit(0, int(second / 10))   # Tens
#  secmilli.writeDigit(1, second % 10)        # Ones
  secmilli.writeDigitRaw(1, dotdigits[second % 10])          # Ones


  now = datetime.datetime.now()
  milli = int(now.microsecond / 1000)
  secmilli.writeDigit(3, milli / 100)     # Tenths
  secmilli.writeDigit(4, (milli / 10) % 10)        # Hundredths
  
  # Wait one hundredth second
  time.sleep(0.01)
