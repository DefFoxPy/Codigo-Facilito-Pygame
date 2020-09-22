"""
Representa un rectangulo con la clase Rect y lo dibuja en pantalla con la funcion pygame.draw.rect
"""
import pygame
import sys

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rectangulos')

white = (255, 255, 255)
red = (115, 38, 80)

rect = pygame.Rect(100, 150, 120, 60)   # Crea el rectangulo
rect.center = (width // 2, height // 2) # Coloca el rectangulo en el centro de la pantalla 

print(rect.x)
print(rect.y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    pygame.draw.rect(surface, red, rect) # dibuja el rectangulo en la pantalla

    pygame.display.update()
