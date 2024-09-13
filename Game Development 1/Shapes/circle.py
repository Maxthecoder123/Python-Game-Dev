import pgzrun
import random

TITLE = 'Circle'
WIDTH = 300
HEIGHT = 300

def draw():

    radius = 10
    r = 0
    g = 120
    b = 150
    for i in range(20):
        screen.draw.circle((150,150),radius,(r,g,b))
        radius +=5
        r += 5
        b -= 5










pgzrun.go()