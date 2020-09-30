import pygame
import sys

pygame.init()

width = 500
height = 600

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Evento de mouse")

white = (255, 255, 255)
red = (255, 0, 0)

font = pygame.font.Font('freesansbold.ttf', 48)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	pos_x, pos_y = pygame.mouse.get_pos()
	message = 'pos x: {} pos y: {}'.format(pos_x, pos_y)

	text = font.render(message, True, red)
	rect = text.get_rect()
	rect.center = (width // 2, height // 2)

	surface.fill(white)
	surface.blit(text, rect)
	pygame.display.update()