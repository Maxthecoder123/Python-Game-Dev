import pygame
import time

pygame.init()

HEIGHT = 326
WIDTH = 308


screen = pygame.display.set_mode((WIDTH,HEIGHT)) # Creating the screen
pygame.display.set_caption("Animation")

fr1 = pygame.image.load("Frame1.png")

while True:

    screen.fill("white")
    screen.blit(fr1,(0,0))
    
    pygame.display.update()

    time.sleep(0.1)

    fr2 = pygame.image.load("Frame2.png")

    screen.fill("white")
    screen.blit(fr2,(0,0))
    
    pygame.display.update()

    time.sleep(0.1)

    fr3 = pygame.image.load("Frame3.png")

    screen.fill("white")
    screen.blit(fr3,(0,0))
    
    pygame.display.update()

    time.sleep(0.1)

    fr4 = pygame.image.load("Frame4.png")

    screen.fill("white")
    screen.blit(fr4,(0,0))
    
    pygame.display.update()

    time.sleep(0.1)

    fr5 = pygame.image.load("Frame 5.png")

    screen.fill("white")
    screen.blit(fr5,(0,0))
    
    pygame.display.update()

    time.sleep(0.1)

    fr6 = pygame.image.load("Frame6.png")

    screen.fill("white")
    screen.blit(fr6,(0,0))
    
    pygame.display.update()

    time.sleep(0.1)