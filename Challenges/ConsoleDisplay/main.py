# https://wokwi.com/projects/361072220290829313

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

numbers = [
    [0, 1, 2, 3, 4, 5],     # 0
    [1, 2],                 # 1
    [0, 1, 6, 4, 3],        # 2
    [0, 1, 6, 2, 3],        # 3
    [5, 6, 1, 2],           # 4
    [0, 5, 6, 2, 3],        # 5
    [0, 5, 6, 2, 3, 4],     # 6
    [0, 1, 2],              # 7
    [0, 1, 2, 3, 4, 5, 6],  # 8
    [0, 1, 2, 3, 5, 6],     # 9
]

while True:
    number = input('Digite um número: ')

    for digit in number:
        try:
            digit = int(digit)
        except ValueError:
            print(f'{digit} não é um número...')
            break

        for led in leds:
            led.on()

        for led in numbers[digit]:
            leds[led].off()

        sleep(0.5)
