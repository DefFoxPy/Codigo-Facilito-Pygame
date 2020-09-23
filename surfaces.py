"""
Crea una segunda superficie y dibuja un rectangulo sobre ella
"""
import pygame
import sys

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Superficies')

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

# Crea la segunda superficie y le damos color
surface2 = pygame.Surface((200, 200))
surface2.fill(green)
# Ajusta la segunda superficie en el centro de la pantalla
rect = surface2.get_rect()
rect.center = (width / 2, height / 2) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    surface.blit(surface2, (100, 100))

    # dibuja sobre la segunda superficie
    pygame.draw.rect(surface2, red, (100, 50, 80, 40))

    pygame.display.update()
