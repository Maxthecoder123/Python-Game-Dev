import pgzrun
import os
import random

os.environ['SDL_VIDEO_CENTERED'] = '1'

TITLE = "Gallaga Game"
WIDTH = 1200
HEIGHT = 1000

bullets = []
enemies = []
power_up_balls = []  # New list to track power-up balls

moveDirection = 1
moveDown = False

player = Actor("plr")
player.pos = (WIDTH/2, HEIGHT-100)

player.dead = False
player.countdown = 90
score = 0

col = random.randint(8, 10)
rows = random.randint(4, 6)
for x in range(col):
    for y in range(rows):
        enemy = Actor("eny")
        enemy.pos = (80 + 80 * x, 80 + 80 * y)
        enemies.append(enemy)

totalScore = (col*rows)*10

power_up_active = False
power_up_duration = 300  # Adjust as needed (in update frames)

power_up_ball = Actor("power_up_ball")
power_up_ball.scale = 0.5  # Adjust the scale as needed

def on_key_down(key):
    global bullets, player, power_up_active
    if player.dead == False:
        if key == keys.SPACE:
            bullet = Actor("bullet")
            bullet.pos = (player.x, player.y - 40)
            bullets.append(bullet)

            if power_up_active:
                # Shoot an additional bullet when power-up is active
                bullet2 = Actor("bullet")
                bullet2.pos = (player.x + 15, player.y - 40)
                bullets.append(bullet2)

def gameover():
    global WIDTH, HEIGHT
    screen.draw.text("Game Over", (WIDTH/2, HEIGHT/2))

def gamecomplete():
    global WIDTH, HEIGHT
    screen.draw.text("You Win!", (WIDTH/2, HEIGHT/2))

def displayScore():
    global WIDTH, HEIGHT, score
    screen.draw.text("Score: " + str(score), (100, 100))

def update():
    global player, bullets, enemies, WIDTH, HEIGHT, moveDirection, moveDown, score, totalScore, power_up_active, power_up_duration

    # Player Movement
    if player.dead == False:
        if keyboard.left and player.x > 40:
            player.x -= 10
        if keyboard.right and player.x < WIDTH-40:
            player.x += 10

    # Bullet Movement
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10

    # Enemy Movement
    if (len(enemies) > 0) and ((enemies[-1].x > WIDTH - 80) or (enemies[0].x < 80)):
        moveDirection = moveDirection * -1  # This will reverse direction
        moveDown = True
    for enemy in enemies:
        enemy.x += 3 * moveDirection
        if moveDown == True:
            for enemy in enemies:
                enemy.y += 80
            moveDown = False
        if enemy.y > HEIGHT:
            gameover()
            enemies.remove(enemy)
        for bullet in bullets:
            if enemy.colliderect(bullet):
                score += 10
                # Drop power-up ball with a higher chance (5%)
                if random.random() < 0.05:
                    power_up_ball = Actor("power_up_ball")
                    power_up_ball.pos = (enemy.x, enemy.y)
                    power_up_balls.append(power_up_ball)
                enemies.remove(enemy)
                bullets.remove(bullet)
                if (len(enemies) == 0) and (score == totalScore):
                    gamecomplete()
        if enemy.colliderect(player):
            player.dead = True
    if player.dead:
        player.countdown -= 1
    if player.countdown == 0:
        player.dead = False
        player.countdown = 90

    # Power-up Ball Movement
    for power_up_ball in power_up_balls:
        if power_up_ball.y >= HEIGHT:
            power_up_balls.remove(power_up_ball)
        else:
            power_up_ball.y += 2  # Adjust the falling speed

    # Check if player collects a power-up ball
    for power_up_ball in power_up_balls:
        if player.colliderect(power_up_ball):
            power_up_balls.remove(power_up_ball)
            power_up_active = True

    # Update power-up duration
    if power_up_active:
        power_up_duration -= 1
        if power_up_duration == 0:
            power_up_active = False
            power_up_duration = 300  # Reset the duration when it runs out

def draw():
    global bullets, enemies, player, power_up_balls

    screen.clear()
    screen.fill((0, 0, 255))

    if player.dead == False:
        player.draw()
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    for power_up_ball in power_up_balls:
        power_up_ball.draw()

    if (len(enemies) == 0):
        if (score == totalScore):
            gamecomplete()
        else:
            gameover()
    displayScore()

pgzrun.go()