""" Mover una imagen con el mouse """
import pygame
import sys

pygame.init()

width = 400
height = 400

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mover imagen con el mouse")

white = (255, 255, 255)

image = pygame.image.load('./images/medium_circle.png')
rect = image.get_rect()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.init()
			sys.exit()

	rect.center = pygame.mouse.get_pos()

	surface.fill(white)
	surface.blit(image, rect)
	pygame.display.update()