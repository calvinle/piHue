from phue import Bridge #Library for Phillips Hue
from time import sleep
import RPi.GPIO as GPIO
import time
import random

mic = 11
light = 7
#GPIO.setup(light, GPIO.IN)
#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(mic, GPIO.IN)
GPIO.setwarnings(False)

b = Bridge('192.168.0.18')
pi = b[1] #The third light bulb connectd to Bridge. 0 throws error
pi2 = b[2]
pi3 = b[3]
pi.xy = [0.3146, 0.3303]
pi2.xy = [0.3146, 0.3303]
pi3.xy = [0.3146, 0.3303]
def rc_time (light):
    count = 0
    
    GPIO.setup(light, GPIO.OUT)
    GPIO.output(light, GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.setup(light, GPIO.IN)
    
    while (GPIO.input(light) == GPIO.LOW):
        count += 1
    print(count)
    return count


def callback(mic):
    print ("Sound Detected!")
    #if GPIO.input(light) == 0 and pi.on == False: #if no light detected and lightbulb is off
      #  pi.on = True #turn on lightbulb
    
    #if GPIO.input(light) == 1 and pi.on == True:  #if light detected and lightbulb is on
      #  pi.on = False #turn off lightbulb
    if pi.on == True:
        pi.xy = [random.random(), random.random()]
    if pi2.on == True:
        pi2.xy = [random.random(), random.random()]
    if pi3.on == True:
        pi3.xy = [random.random(), random.random()]

    time.sleep(3)
    pi.xy = [0.3146, 0.3303]
    pi2.xy = [0.3146, 0.3303]
    pi3.xy = [0.3146, 0.3303]
    
GPIO.add_event_detect(mic, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(mic, callback)

    
try:
    while True:
        if (rc_time(light) > 0):
            pi.on = True
            pi2.on = True
            pi3.on = True
        
        if (rc_time(light) == 0):
            pi.on = False
            pi2.on = False
            pi3.on = False
        
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()