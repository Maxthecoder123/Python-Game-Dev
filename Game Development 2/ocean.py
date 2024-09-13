import pygame
pygame.init()
pygame.display.set_caption("Submarine in the Sea")

# Setup screen
screen_width = 612
screen_height = 360
screen = pygame.display.set_mode([screen_width,screen_height])

# Define player class as a sprite

# We will make the player start at 0,0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("submarine.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(70,100))
        self.rect = self.image.get_rect()
    # Function is to move it
    def update(self,pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)
        
        # Keeps player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 250:
            self.rect.bottom = 250
    
    # End of the class

# Sprite group
sprites = pygame.sprite.Group()

# Game Loop

def startgame():
    # Creating player object
    player = Player()
    # Add player to sprite group
    sprites.add(player)
    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            # Get the set of keys pressed and check for user input
            pressed_keys = pygame.key.get_pressed()
            # Update player position based on the user input
            player.update(pressed_keys)
            # Update the display
            screen.blit(pygame.image.load("backgroundsea.png"),(0,0))
            sprites.draw(screen)
            pygame.display.update()

startgame()


