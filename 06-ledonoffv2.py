from picozero import pico_led,LED
from time import sleep

pico_led.on()
sleep(1)
pico_led.off()
sleep(1)

firefly = LED(13) # Use GP13
while True:
    firefly.on()
    sleep(0.5)
    firefly.off()
    sleep(2.5)