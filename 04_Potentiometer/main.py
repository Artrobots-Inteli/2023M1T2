# https://wokwi.com/projects/359747406102207489

from machine import Pin, ADC

potentiometer = ADC(Pin(15, Pin.IN))

while True:
    value = potentiometer.read()/40.95
    print(f'valor: {value:.2f}')
