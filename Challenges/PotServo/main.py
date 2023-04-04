# https://wokwi.com/projects/360563278073027585

from machine import Pin, PWM, ADC

servo = PWM(Pin(23, Pin.OUT))
servo.freq(50)

pot = Pin(4, Pin.IN)
pot = ADC(pot)


def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def set_servo_position(degrees):
    duty_cycle = map(degrees, 0, 180, 0.025, 0.12)
    servo.duty(int(duty_cycle*1024))


while True:
    pot_value = map(pot.read(), 0, 4095, 0, 180)
    print(pot_value)
    set_servo_position(pot_value)