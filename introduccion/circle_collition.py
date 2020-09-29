import pygame
import sys
import math

pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode((width, height))

white = (255, 255, 255)
black = (0, 0, 0)

font = pygame.font.Font(None, 40)

image1 = pygame.image.load('./images/medium_circle.png')
rect1 = image1.get_rect()
rect1.center = (width // 2, height // 2)

image2 = pygame.image.load('./images/medium_circle.png')
rect2 = image2.get_rect()
rect2.center = rect1.center

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	message = ''

	rect1.center = pygame.mouse.get_pos()

	# determina la distancia entre los centros de los circulos
	dist = math.hypot(rect1.x - rect2.x, rect1.y - rect2.y)

	# distancia menor a la suma de los radios
	if dist < (64 + 64): 
		message = 'Existe una colisión'

	text = font.render(message, True, black)
	text_rect = text.get_rect()
	text_rect.midtop = (width // 2, 50)

	screen.fill(white)
	screen.blit(image1, rect1)
	screen.blit(image2, rect2)
	screen.blit(text, text_rect)
	pygame.display.update()