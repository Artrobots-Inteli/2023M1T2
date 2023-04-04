# https://wokwi.com/projects/360380674592066561

from machine import Pin, PWM
from time import sleep

servo = PWM(Pin(22, Pin.OUT))
servo.freq(50)

button1 = Pin(18, Pin.IN, Pin.PULL_UP)
button2 = Pin(19, Pin.IN, Pin.PULL_UP)


def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def set_servo_position(degrees):
    duty_cycle = map(degrees, 0, 180, 0.025, 0.12)
    servo.duty(int(duty_cycle*1024))


while True:
    if not button1.value():
        set_servo_position(0)
        sleep(0.5)

    if not button2.value():
        set_servo_position(180)
        sleep(0.5)
