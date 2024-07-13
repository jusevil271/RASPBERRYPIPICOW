from picozero import RGBLED
from time import sleep

rgb = RGBLED(red = 1, green = 2, blue = 3)

def verde(): # Your first mood
    rgb.color = (0, 255, 0) # Your first colour

def rojo(): # Your second mood
    rgb.color = (255, 0, 0) # Your second colour
    
def azul(): # Your second mood
    rgb.color = (0, 0, 255) # Your second colour
    
while True:
    rojo()
    sleep(1)
    verde()
    sleep(1)
    azul()
    sleep(1)
    
