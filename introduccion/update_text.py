import pygame
import sys

pygame.init()

width = 500
height = 400

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tiempo')

white = (255, 255, 255)
red = (255, 0, 0)

font = pygame.font.Font('freesansbold.ttf', 48)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	seconds = pygame.time.get_ticks() // 1000

	surface.fill(white)

	text = font.render(str(seconds), True, red)
	rect = text.get_rect()
	rect.center = (width / 2, height / 2) 

	surface.blit(text, rect)

	pygame.display.update()