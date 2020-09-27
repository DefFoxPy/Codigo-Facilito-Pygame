import pygame
import sys

pygame.init()

width = 500
height = 600

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mover imagen")

white = (255, 255, 255)
red = (255, 0, 0)

image = pygame.image.load('./images/medium_circle.png')
rect = image.get_rect()
rect.center = (width // 2, height // 2)
	
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	pressed = pygame.key.get_pressed()

	if pressed[pygame.K_w]:
		rect.y -= 5

	if pressed[pygame.K_s]:
		rect.y += 5

	if pressed[pygame.K_a]:
		rect.x -= 5

	if pressed[pygame.K_d]:
		rect.x += 5

	# validacíones
	if rect.left < 0:
		rect.left = 0

	if rect.right > width:
		rect.right = width

	if rect.top < 0:
		rect.top = 0	

	if rect.bottom > height:
		rect.bottom = height

	surface.fill(white)
	surface.blit(image, rect)
	pygame.display.update()