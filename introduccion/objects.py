"""
Método pygame.draw argumentos
1) Donde se pintará la figura
2) De qué color será la figura

ejemplo:
pygame.draw.rect(superficie, color, rectanglo)
pygame.draw.circle(superficie, color, (centro_x, centro_y), radio)
pygame.draw.line(superficie, color, (punto_a), (punto_b), grosor)
"""
import pygame
import sys

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Dibujar Objetos')

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    pygame.draw.rect(surface, red, (100, 100, 80, 40))

    pygame.draw.circle(surface, green, (200, 300), 100)

    pygame.draw.line(surface, blue, (100, 100), (200, 300), 2)

    pygame.display.update()