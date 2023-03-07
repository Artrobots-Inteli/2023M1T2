from machine import Pin

internal_led = Pin(2, Pin.OUT)

internal_led.value(1)
