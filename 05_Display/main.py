# https://wokwi.com/projects/361072889249847297

from machine import Pin
from time import sleep

common = Pin(13, Pin.OUT)
common.on()

leds = [
    Pin(27, Pin.OUT), # A
    Pin(26, Pin.OUT), # B
    Pin(32, Pin.OUT), # C
    Pin(33, Pin.OUT), # D
    Pin(25, Pin.OUT), # E
    Pin(14, Pin.OUT), # F
    Pin(12, Pin.OUT)  # G
]


while True:
    for seg in leds:
        seg.off()
        sleep(0.1)

    for seg in leds:
        seg.on()
        sleep(0.1)
