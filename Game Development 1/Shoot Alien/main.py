import pgzrun
import random

#Screen
WIDTH = 400
HEIGHT = 400
TITLE = "Shoot Alien"

#Global Variable
message = "Click on the Alien"

#Actor is a built it object in pgzero
bob = Actor("bob")

def draw():
    screen.fill(color="blue")

    #Displaying an actor
    bob.draw()

    #Displaying Message
    screen.draw.text(message,center=(200,20),color=("white"),fontsize=30)

#Userdefined Function
def location():
    bob.x = random.randint(30,WIDTH-30)
    bob.y = random.randint(30,HEIGHT-30)

#Predefined Function
def on_mouse_down(pos):
    #Calling global variable
    global message
    #To check if the mouse is clicked on a Actor
    if bob.collidepoint(pos):
        location()
        message = "You hit him!"
    else:
        message = "You missed, try again"


pgzrun.go()