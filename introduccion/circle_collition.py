import pygame
import sys

pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode((width, height))

white = (255, 255, 255)

image1 = pygame.image.load('./images/medium_circle.png')
rect1 = image1.get_rect()
rect1.center = (width // 2, height // 2)

surface1 = pygame.Surface((rect1.width, rect1.height), pygame.SRCALPHA)
surface1.fill((0, 0, 0, 50))
rect2 = surface1.get_rect()
rect2.center = rect1.center


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill(white)
	screen.blit(image1, rect1)
	screen.blit(surface1, rect2)
	pygame.display.update()