# https://wokwi.com/projects/358939421562468353
from machine import Pin

button1 = Pin(22, Pin.IN, Pin.PULL_UP)
button2 = Pin(23, Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)


def or_gate(value1, value2):
    return value1 or value2


def and_gate(value1, value2):
    return value1 and value2


def xor_gate(value1, value2):
    return value1 != value2


def not_gate(value):
    return not value


def nand_gate(value1, value2):
    return not_gate(and_gate(value1, value2))


def nor_gate(value1, value2):
    return not_gate(or_gate(value1, value2))


while True:
    button1_value = not button1.value()
    button2_value = not button2.value()

    led.value(xor_gate(button1_value, button2_value))
