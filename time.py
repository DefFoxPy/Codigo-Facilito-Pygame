import pygame
import sys

pygame.init()

width = 500
height = 400

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tiempo')

white = (255, 255, 255)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	time = pygame.time.get_ticks() // 1000 # segundos
	print(time)

	surface.fill(white)
	pygame.display.update()