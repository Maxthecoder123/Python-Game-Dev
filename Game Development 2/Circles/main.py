import pygame

pygame.init() # Initialising the pygame library

screen_size = (600,600)
blue = (0,0,255) 

screen = pygame.display.set_mode(screen_size) # Creating the screen
screen.fill(blue)

pygame.display.update()


class Circles():
    def __init__(self, radius, colour, pos, width):
        self.radius = radius
        self.colour =  colour
        self.pos = pos
        self.width = width
        self.circleSurface = screen

    def draw(self):
        self.drawCircle = pygame.draw.circle(self.circleSurface, self.colour, self.pos, self.radius, self.width)
    
    def increase(self,radius):
        self.radius += radius
        self.drawCircle = pygame.draw.circle(self.circleSurface, self.colour, self.pos, self.radius, self.width)

        

# Creating object out of a class
c1 = Circles(25,(255,0,0),(300,300),5)
c2 = Circles(35,(0,255,0),(100,100),4)



while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            c1.draw()
            c2.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            c1.increase(10)
            pygame.display.update()


    
    
