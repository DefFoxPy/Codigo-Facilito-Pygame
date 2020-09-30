"""  """
import pygame
import sys

pygame.init()

width = 400
height = 400

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Colisión")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 255, 0)

font = pygame.font.Font(None, 40)

rect1 = pygame.Rect(0, 0, 100, 80)
rect1.center = (width // 2, height // 2)

rect2 = pygame.Rect(0, 0, 100, 80)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.init()
			sys.exit()

	rect2.center = pygame.mouse.get_pos()

	message = ''

	if rect1.colliderect(rect2):
		sound = pygame.mixer.Sound('./sounds/coin.wav')
		sound.play()
		message = 'Existe colisión'

	text = font.render(message, True, black)
	rect_text = text.get_rect()
	rect_text.midtop = (width // 2, 50)

	surface.fill(white)
	pygame.draw.rect(surface, red, rect1)
	pygame.draw.rect(surface, blue, rect2)
	surface.blit(text, rect_text)
	pygame.display.update()