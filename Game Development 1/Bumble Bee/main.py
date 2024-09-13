import pgzrun
import random

TITLE = "Bumble Bee Game"
WIDTH = 400
HEIGHT = 400

#Actors
bee = Actor("bee")
flower = Actor("flower")

#Global Variables
score = 0
gameover = False
bee.x = random.randint(20,WIDTH-20)
bee.y = random.randint(20,HEIGHT-20)
# Continuous function, runs for every frame
def draw():
    global score, gameover
    # Blit means copying the content of one surface to another
    screen.blit("background",(0,0))
    screen.draw.text("Score: "+str(score),topleft=(50,50),color=("black"),fontsize=20)

    # Drawing Actors on screen
    bee.draw()
    flower.draw()

    if gameover:
        screen.fill("blue")
        screen.draw.text("GAME OVER!",center=(200,200),color=("green"),fontsize=20)
        # String Concatenation is joining string with something
        screen.draw.text("Your score is: "+str(score),center=(200,250),color=("green"),fontsize=20)

def location():
    flower.x = random.randint(20,WIDTH-20)
    flower.y = random.randint(20,HEIGHT-20)

def update():
    global score
    
    if keyboard.w:
        bee.y -= 5
    if keyboard.a:
        bee.x -= 5
    if keyboard.s:
        bee.y += 5
    if keyboard.d:
        bee.x += 5


    if bee.colliderect(flower):
        location()
        score += 1
def timesup():
    global gameover
    gameover = True

# Timer
# When you want to call a function after certain amount of seconds we use clock.schedule
# The syntax is clock.schedule(funtion name, time in seconds)
clock.schedule(timesup,60.0)

pgzrun.go()