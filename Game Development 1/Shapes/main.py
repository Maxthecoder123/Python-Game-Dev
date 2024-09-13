import pgzrun
import random

# Screen
TITLE = 'Shapes'
WIDTH = 300
HEIGHT = 300

# The function that renders the final output on the screen
def draw():
    # First Rectange
    width = WIDTH
    height = HEIGHT - 200
    r = 255
    g = 0
    b = random.randint(125,255)

    for i in range(20):
        # Creating rectangle
        rect = Rect((0,0),(width,height))
        rect.center = (150,150)

        # Displaying rectange
        screen.draw.rect(rect,(r,g,b))

        width -= 10
        height += 10
        r -= 5
        g += 5







# Runs the code
pgzrun.go()



