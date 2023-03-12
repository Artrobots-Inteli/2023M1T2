from machine import Pin

# Cria um objeto que representa o pino 2 do ESP32
internal_led = Pin(2, Pin.OUT)

# Liga o LED interno (que está conectado no pino 2)
internal_led.on()
