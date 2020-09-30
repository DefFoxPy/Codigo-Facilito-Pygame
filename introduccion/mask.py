import pygame
import sys

pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode((width, height))

white = (255, 255, 255)
black = (0, 0, 0)

image1 = pygame.image.load('./images/medium_circle.png')
rect1 = image1.get_rect()
rect1.center = (width // 2, height // 2)
mask_circle = pygame.mask.from_surface(image1)

image2 = pygame.image.load('./images/small_rectangle.png')
rect2 = image2.get_rect()
mask_rect = pygame.mask.from_surface(image2)

font = pygame.font.Font('freesansbold.ttf', 36)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	rect2.center = pygame.mouse.get_pos()

	message = ''

	offset = (rect2.x - rect1.x, rect2.y - rect1.y)
	if mask_circle.overlap(mask_rect, offset):
		message = 'Colision'

	text = font.render(message, True, black)
	text_rect = text.get_rect()
	text_rect.midtop = (width // 2, 30) 

	screen.fill(white)
	screen.blit(text, text_rect)
	screen.blit(image1, rect1)
	screen.blit(image2, rect2)
	pygame.display.update()