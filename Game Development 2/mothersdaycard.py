import pygame
import time

pygame.init()

HEIGHT = 600
WIDTH = 600


screen = pygame.display.set_mode((WIDTH,HEIGHT)) # Creating the screen
pygame.display.set_caption("Mother's Day Card")

bg = pygame.image.load("mother.jpg")

while True:
    font = pygame.font.SysFont("Times New Roman",50)
    text1 = font.render("Happy Mother's Day",True,(0,0,0))

    screen.fill("white")
    screen.blit(bg,(0,0))
    screen.blit(text1,(100,550))

    pygame.display.update()

    time.sleep(2)

    heart = pygame.image.load("heart.jpg")

    font = pygame.font.SysFont("Times New Roman",40)
    text1 = font.render("Wish you a bright future ahead!",True,(0,0,0))

    screen.fill("white")
    screen.blit(heart,(0,0))
    screen.blit(text1,(55,200))

    pygame.display.update()

    time.sleep(2)

    present = pygame.image.load("present.jpg")

    font = pygame.font.SysFont("Times New Roman",40)
    text1 = font.render("Here is a suprise!",True,(0,0,0))

    screen.fill("white")
    screen.blit(present,(0,0))
    screen.blit(text1,(100,550))

    pygame.display.update()

    time.sleep(2)

    flowers = pygame.image.load("flowers.jpg")

    font = pygame.font.SysFont("Times New Roman",40)
    text1 = font.render("A present for you!",True,(0,0,0))

    screen.fill("white")
    screen.blit(flowers,(0,0))
    screen.blit(text1,(100,550))

    pygame.display.update()

    time.sleep(2)

    