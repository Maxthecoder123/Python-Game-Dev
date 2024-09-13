import pgzrun
import random
import time

TITLE = "Fireman Race"
WIDTH = 600
HEIGHT = 600

# Actors
fireman1 = Actor("fireman1")
fireman2 = Actor("fireman2")
asteroid = Actor("fire")

# Global Variables
score1 = 0
score2 = 0
gameover = False
instruction_screen = True  # Add an instruction screen variable
instruction_start_time = 0  # Variable to track the start time of the instruction screen

fireman1.x = random.randint(20, WIDTH - 20)
fireman1.y = random.randint(20, HEIGHT - 20)
fireman2.x = random.randint(20, WIDTH - 20)
fireman2.y = random.randint(20, HEIGHT - 20)

def draw():
    global gameover, instruction_screen

    if instruction_screen:
        show_instructions()
        return

    screen.blit("wood_background", (0, 0))
    screen.draw.text("Red: " + str(score1), topleft=(20, 20), color=("white"), fontsize=20)
    screen.draw.text("Blue: " + str(score2), topleft=(480, 20), color=("white"), fontsize=20)
    fireman1.draw()
    fireman2.draw()
    asteroid.draw()

    if gameover:
        screen.fill("blue")
        screen.draw.text("GAME OVER!", center=(300, 300), color=("green"), fontsize=20)
        screen.draw.text("Red Score: " + str(score1), center=(300, 330), color=("green"), fontsize=20)
        screen.draw.text("Blue Score: " + str(score2), center=(300, 360), color=("green"), fontsize=20)

def location():
    asteroid.x = random.randint(20, WIDTH - 20)
    asteroid.y = random.randint(20, HEIGHT - 20)

def update():
    global score1, score2, gameover, instruction_screen, instruction_start_time

    if instruction_screen:
        if not instruction_start_time:
            instruction_start_time = time.time()
        # Show instructions for 10 seconds
        if time.time() - instruction_start_time >= 10:
            instruction_screen = False
            instruction_start_time = 0
    elif not gameover:
        if keyboard.w:
            fireman1.y -= 5
        if keyboard.a:
            fireman1.x -= 5
        if keyboard.s:
            fireman1.y += 5
        if keyboard.d:
            fireman1.x += 5

        if keyboard.up:
            fireman2.y -= 5
        if keyboard.left:
            fireman2.x -= 5
        if keyboard.down:
            fireman2.y += 5
        if keyboard.right:
            fireman2.x += 5

        if fireman1.colliderect(asteroid):
            location()
            score1 += 1

        if fireman2.colliderect(asteroid):
            location()
            score2 += 1

def timesup():
    global gameover
    gameover = True

def show_instructions():
    screen.clear()
    screen.blit("space_background", (0, 0))
    instructions = [
        "Welcome to Space Race!",
        "Player 1 (Red): Use WASD to move",
        "Player 2 (Blue): Use arrow keys to move",
        "Collect asteroids to score points",
        "The game lasts for 60 seconds",
        "Press any key to start..."
    ]
    y = 100
    for line in instructions:
        screen.draw.text(line, topleft=(100, y), color=("white"), fontsize=20)
        y += 30

# Timer
clock.schedule(timesup, 60.0)

pgzrun.go()




