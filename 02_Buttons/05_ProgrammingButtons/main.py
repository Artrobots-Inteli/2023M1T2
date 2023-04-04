# https://wokwi.com/projects/359051497111099393

from machine import Pin

# Cria um objeto do tipo Pin para o pino 22 em modo ENTRADA
button1 = Pin(22, Pin.IN, Pin.PULL_UP)

while True:
    # Lê o valor do botão e armazena na variável button1_value
    button1_value = button1.value()
    # Imprime o valor do botão
    print(button1_value)
