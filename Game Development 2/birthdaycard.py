import pygame
import time

pygame.init()

HEIGHT = 600
WIDTH = 600


screen = pygame.display.set_mode((WIDTH,HEIGHT)) # Creating the screen
pygame.display.set_caption("Birthday Card")

bg = pygame.image.load("bg.jpg")

while True:
    font = pygame.font.SysFont("Times New Roman",50)
    text1 = font.render("Happy",True,(0,0,0))
    text2 = font.render("Birthday",True,(0,0,0))

    screen.fill("white")
    screen.blit(bg,(0,0))
    screen.blit(text1,(250,200))
    screen.blit(text2,(200,300))

    pygame.display.update()

    time.sleep(2)

    confetti = pygame.image.load("confetti.jpg")

    font = pygame.font.SysFont("Times New Roman",40)
    text1 = font.render("Wish you a bright future ahead!",True,(0,0,0))

    screen.fill("white")
    screen.blit(confetti,(0,0))
    screen.blit(text1,(60,80))

    pygame.display.update()

    time.sleep(2)

    cake = pygame.image.load("cake.jpg")

    font = pygame.font.SysFont("Times New Roman",40)
    text1 = font.render("A present for you!",True,(0,0,0))

    screen.fill("white")
    screen.blit(cake,(0,0))
    screen.blit(text1,(60,80))

    pygame.display.update()

    time.sleep(2)