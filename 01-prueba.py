from machine import Pin
import time

# Define the onboard LED pin (usually pin 25 for Raspberry Pi Pico)
led = Pin("LED", Pin.OUT)

while True:
    led.value(1)  # Turn the LED on
    time.sleep(1) # Wait for 1 second
    led.value(0)  # Turn the LED off
    time.sleep(1) # Wait for 1 second
