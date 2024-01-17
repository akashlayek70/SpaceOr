
import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
#Player
pygame 

running = True
#Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #RGB =Red Green Blue
    screen.fill((200,150,100))
    pygame.display.update()







