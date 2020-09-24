"""
"""
import pygame
import sys

pygame.init()

width = 600
height = 600

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Imagenes')

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

image = pygame.image.load('./images/codi.png') # -> surface
rect = image.get_rect()
rect.center = (width / 2, height / 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)
    surface.blit(image, rect) # dibujando la imagen
    pygame.display.update()
