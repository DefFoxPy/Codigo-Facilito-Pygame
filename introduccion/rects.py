"""
Representa un rectangulo con la clase Rect y lo dibuja en pantalla con la funcion pygame.draw.rect

Cambio:
  *Crea un segundo rectangulo mediante una tupla

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
green = (0, 255, 0)

rect = pygame.Rect(100, 150, 120, 60)  
rect.center = (width // 2, height // 2)

print(rect.x)
print(rect.y)

rect2 = (100, 100, 80, 40) # segunda forma de crear un rectangulo

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    pygame.draw.rect(surface, red, rect)
    pygame.draw.rect(surface, green, rect2)

    pygame.display.update()
