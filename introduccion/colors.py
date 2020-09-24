"""
Creación de colores mediante la clase Color o mediante una tupla

link para buscar codigo de colores en RGB
https://www.webfx.com/web-design/hex-to-rgb/
"""
import pygame
import sys

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Colores')

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

my_color = (200, 90, 130)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(my_color)
    pygame.display.update()
