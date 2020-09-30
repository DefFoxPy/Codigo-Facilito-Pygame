import pygame
import sys

pygame.init()

width = 500
heigth = 500

screen = pygame.display.set_mode((width, heigth))
pygame.display.set_caption('Eventos de teclado')

white = (255, 255, 255)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:

			if event.key ==	pygame.K_LEFT or event.key == pygame.K_a:
				print('Izquierda')	

			if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				print('Derecha')

			if event.key == pygame.K_UP or event.key == pygame.K_w:
				print('Arriba')

			if event.key == pygame.K_DOWN or event.key == pygame.K_s:
				print('Abajo')

		if event.type == pygame.KEYUP:
			pass

	screen.fill(white)
	pygame.display.update()