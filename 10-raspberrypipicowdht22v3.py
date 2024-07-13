"""
Conexiones del DHT22 a la Raspberry Pi Pico W

    Pin de datos del DHT22 -> Conéctalo a un pin GPIO de la Pico (por ejemplo, GP16).
    Pin VCC del DHT22 -> Conéctalo al pin de 3.3V de la Pico.
    Pin GND del DHT22 -> Conéctalo a un pin GND de la Pico.
    Resistencia de pull-up (10kΩ) entre el pin de datos y el pin VCC. SOLO NECESARIO SI NO TIENES PLACA EN EL SENSOR. SI TIENES PLACA NO ES NECESARIO.
"""

import machine
import time
import dht

# Configuración del pin donde está conectado el sensor DHT22
dht_pin = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
sensor = dht.DHT22(dht_pin)

while True:
    try:
        # Medir la temperatura y la humedad
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()

        # Imprimir los valores leídos
        print('Temperatura: {:.2f} C'.format(temp))
        print('Humedad: {:.2f} %'.format(hum))

    except OSError as e:
        print('Error al leer el sensor: {}'.format(e))

    # Esperar 2 segundos antes de la siguiente lectura
    time.sleep(2)