import pygame
import sys

pygame.init()

width = 500
height = 600

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Evento de mouse")

white = (255, 255, 255)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			
			print(event.pos)

			if event.button == 1:
				print('Clic izquierdo')

			if event.button == 2:
				print('Clic centro')

			if event.button == 3:
				print('Clic derecho')

			if event.button == 4:
				print('Scroll arriba')

			if event.button == 5:
				print('Scroll abajo')


		if event.type == pygame.MOUSEBUTTONUP:
			#print('Botón liberado')
			pass

	surface.fill(white)
	pygame.display.update()