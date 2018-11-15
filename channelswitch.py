#!/usr/bin/python
import os
from time import sleep
import RPi.GPIO as GPIO

sleep(5)

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

i=1

while True:
    if ( GPIO.input(26) == 1):
        print ("channel%s.m3u" % i)
        os.system('vlc --fullscreen /home/pi/channels/channel%s.m3u &' % i)
        i += 1
        if i > 4:
            i = 1
        else:
            i = i
        sleep(2)
    else:
        sleep(0.1)
    