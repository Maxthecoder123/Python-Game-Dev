import pygame
import random
import time
from pygame.locals import *

def changeBackground(img):
    background = pygame.image.load(img)
    bg = pygame.transform.scale(background,(screen_width,screen_height))
    screen.blit(bg,(0,0))


# Initialise pygame
pygame.init()
pygame.display.set_caption("Pixel Run")
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

# Classes
class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pixelplayer.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()

class Recyclable(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image,(60,70))
        self.rect = self.image.get_rect()
class NonRecyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("danger.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()

# Recyclable items list
images = ['diamond.png','chest.png','diamond.png']

# Create sprite groups
item_list = pygame.sprite.Group()
allsprites = pygame.sprite.Group()
plastic_list = pygame.sprite.Group()

# Create items sprites at random location
for i in range(50):
    item = Recyclable(random.choice(images))
    item.rect.x = random.randrange(screen_width)
    item.rect.y = random.randrange(screen_height)
    item_list.add(item)
    allsprites.add(item)
for i in range(50):
    plastic = NonRecyclable()
    plastic.rect.x = random.randrange(screen_width)
    plastic.rect.y = random.randrange(screen_height)
    plastic_list.add(plastic)
    allsprites.add(plastic)

# Create player bin
player = Bin()
allsprites.add(player)

# Initialise essential variable
WHITE = (255,255,255)
RED = (255,0,0)
playing = True
score = 0
clock = pygame.time.Clock()
start_time = time.time()
myFont = pygame.font.SysFont("Times New Roman", 40)
timingFont = pygame.font.SysFont("Times New Roman", 70)
text = myFont.render("Score= "+str(0),True,WHITE)

# Main probram loop
while playing: 
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    timeEnlapsed = time.time()-start_time
    if timeEnlapsed >= 60:
        if score >35:                         
            changeBackground("winscreen.jpg") # Homework
        else:
            text = myFont.render("You Lose!", True, WHITE)
            changeBackground("losescreen.jpg") # Homework
        screen.blit(text,(250,40))
    else:
        changeBackground("pixelground.jpg")
        countDown = timingFont.render(str(60-int(timeEnlapsed)),True, RED)
        screen.blit(countDown, (800,10))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if player.rect.y>0:
                player.rect.y -= 5
        if keys[pygame.K_DOWN]:
            if player.rect.y<630:
                player.rect.y += 5
        if keys[pygame.K_LEFT]:
            if player.rect.x>0:
                player.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            if player.rect.x<850:
                player.rect.x += 5
        
        # Check for collision
        item_hit_list = pygame.sprite.spritecollide(player,item_list, True)#
        plastic_hit_list = pygame.sprite.spritecollide(player,plastic_list, True)#
        for item in item_hit_list:
            score += 1
            text = myFont.render("Score= "+str(score), True, WHITE)
        for plastic in plastic_hit_list:
            score -= 1
            text = myFont.render("Score= "+str(score), True, WHITE)
        screen.blit(text, (20,50))
        allsprites.draw(screen)
    pygame.display.update()
