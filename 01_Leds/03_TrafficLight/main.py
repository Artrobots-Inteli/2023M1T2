# https://wokwi.com/projects/361070084642315265

from machine import Pin
from time import sleep

red = Pin(18, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(21, Pin.OUT)

while True:
    red.on()
    yellow.off()
    green.off()
    sleep(5)

    red.off()
    yellow.on()
    sleep(2)

    yellow.off()
    green.on()
    sleep(5)
