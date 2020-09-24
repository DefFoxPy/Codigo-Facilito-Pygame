"""
Dibujar texto en pantalla

1. Obtener una fuente
2. Crear el texto
3. Dibujar el texto
"""
import pygame
import sys

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Texto')

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

font = pygame.font.Font('./roboto/Roboto-Italic.ttf', 48) # 1

text = font.render('¡Hola Mundo!', True, black) # 2
rect = text.get_rect()
rect.center = (width / 2, height / 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)
    surface.blit(text, rect) # 3
    pygame.display.update()
