from phue import Bridge #Library for Phillips Hue
from time import sleep #Time library
import RPi.GPIO as GPIO
import time
import random

mic = 11    #Mic connected to physical pin 11
light = 7   #Light sensor connected to physical pin 7
GPIO.setmode(GPIO.BOARD)    #Mode of pin layout
GPIO.setup(mic, GPIO.IN)    #Set up pin
GPIO.setwarnings(False)     #Warnings are bullshit

b = Bridge('192.168.0.18')  #My bridge is at this IP. Must press button
pi = b[1]   #The first light bulb connectd to Bridge. 0 throws error
pi2 = b[2]
pi3 = b[3]
pi.xy = [0.3146, 0.3303]    #Initial RSV values
pi2.xy = [0.3146, 0.3303]
pi3.xy = [0.3146, 0.3303]

def rc_time (light):        #Light function
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

    if pi.on == True:           #Lightbulb has to actually be on
        pi.xy = [random.random(), random.random()]  #Change to random color
    if pi2.on == True:
        pi2.xy = [random.random(), random.random()]
    if pi3.on == True:
        pi3.xy = [random.random(), random.random()]

    time.sleep(3)
    pi.xy = [0.3146, 0.3303]    #Change back to initial value
    pi2.xy = [0.3146, 0.3303]
    pi3.xy = [0.3146, 0.3303]
    
GPIO.add_event_detect(mic, GPIO.BOTH, bouncetime=300)   #Ask me later
GPIO.add_event_callback(mic, callback)

    
try:
    while True:
        if (rc_time(light) > 0):    #If light function detects no light from sensor
            pi.on = True            #Turn on ALL lightbulbs
            pi2.on = True
            pi3.on = True
        
        if (rc_time(light) == 0):   #Else if light function detects light
            pi.on = False           #Turn off ALL lightbulbs
            pi2.on = False
            pi3.on = False
        
except KeyboardInterrupt:           #If keyboard inputs anything, stop program
    pass
finally:
    GPIO.cleanup()                  #idk??
