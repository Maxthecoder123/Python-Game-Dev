import pgzrun
import random

# Screen
WIDTH = 400
HEIGHT = 400
TITLE = "Click Game"

# Global Variables
message = "Click on the Robber to catch him"
score = 0

# Actors with scaled images
good_guy_actor = Actor("good_guy_actor.png") 
bad_guy_actor = Actor("bad_guy_actor.png")  

def draw():
    screen.fill("blue")  

    # Display actors
    good_guy_actor.draw()
    bad_guy_actor.draw()

    # Display Message and Score
    screen.draw.text(message, center=(200, 370), color="white", fontsize=30)
    screen.draw.text(f"Score: {score}", topright=(370,20), color="white")

def location():
    good_guy_actor.x = random.randint(30, WIDTH - 30)
    good_guy_actor.y = random.randint(30, HEIGHT - 30)
    bad_guy_actor.x = random.randint(30, WIDTH - 30)
    bad_guy_actor.y = random.randint(30, HEIGHT - 30)

# Predefined Function
def on_mouse_down(pos):
    global score
    if good_guy_actor.collidepoint(pos):
        score -= 1
    elif bad_guy_actor.collidepoint(pos):
        score += 1
    location()

location()  # Set initial positions of actors
pgzrun.go()