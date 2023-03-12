from machine import Pin
from time import sleep

# Cria um objeto que representa o pino 2 do ESP32
led = Pin(2, Pin.OUT)

# Loop infinito
while True:
    # Liga o LED
    led.on()
    # Aguarda 0.5 segundo
    sleep(0.5)
    # Desliga o LED
    led.off()
    # Aguarda 0.5 segundo
    sleep(0.5)
