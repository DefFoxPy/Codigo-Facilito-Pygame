import pygame
import sys

pygame.init()

width = 500
height = 400

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sonido de fondo')

white = (255, 255, 255)
red = (255, 0, 0)

pygame.mixer.music.load('./sounds/Haggstrom.mp3')
pygame.mixer.music.set_volume(1.0) # float 0.0 - 1.0
pygame.mixer.music.play(-1, 0.0)

#pygame.mixer.music.rewind() # reiniciar
#pygame.mixer.music.pause() # pausar
#pygame.mixer.music.stop() # detener
#music.mixer.music.fadeuot(5000) # detener poco a poco

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	surface.fill(white)

	pygame.display.update()