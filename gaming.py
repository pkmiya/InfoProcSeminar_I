from sense_hat import SenseHat
sense = SenseHat()
import time

sense.clear()
while True:
    for x in range(0, 255):
        sense.clear(255, x, 0) #red to yellow
    for x in range(0, 255):
        sense.clear(255-x, 255, 0) #yellow to green
    for x in range(0, 255):
        sense.clear(0, 255, x) #green to sky-blue
    for x in range(0, 255):
        sense.clear(0, 255-x, 255) #sky-blue to blue
    for x in range(0, 255):
        sense.clear(x, 0, 255) #blue to purple
    for x in range(0, 255):
        sense.clear(255, 0, 255-x) #purple to red