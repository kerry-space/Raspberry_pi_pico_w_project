from machine import Pin
import time 

#create button object and led 
led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP)    #Create button object from Pin13 , Set GP13 to input

def short_blink(led):
    led.value(1)
    time.sleep(0.2)  
    led.value(0)
    time.sleep(0.2)  


def long_blink(led):
    led.value(1)
    time.sleep(0.6)  
    led.value(0)
    time.sleep(0.2)  

def send_sos(num_of_sos):
    for _ in range(num_of_sos):
        #short blink
        for _ in range(3):
            short_blink(led)
        #long blink
        for _ in range(3):
            long_blink(led)
        #short blink
        for _ in range(3):
            short_blink(led)
        
        #delay
        time.sleep(1)

            
try:
    while True:
        #check if  Button is pressed
        if not button.value():
            send_sos(1)
        else:
            led.value(0)
except:
    pass
        