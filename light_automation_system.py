#light automation system
from machine import Pin
from time import sleep
led1 = Pin(2,Pin.OUT)
led2 = Pin(4,Pin.OUT)
led3 = Pin(16,Pin.OUT)

while True:
    led1.on()
    sleep(1)
    led1.off()
    led2.on()
    sleep(1)
    led2.off()
    led3.on()
    sleep(1)
    led3.off()