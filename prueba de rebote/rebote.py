"""
Se simulará el rebote de una pelota
"""
import pygame

pygame.init()

ANCHO = 500
LARGO = 500

BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

GRAVEDAD = 1.2
VELOCIDAD = 5
SALTO = -40

class Jugador(pygame.sprite.Sprite):
	
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface((20, 20))
		self.image.fill(AZUL)

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.rect.bottom = y

		self.pos_y = self.rect.bottom
		self.velocidad = 0 

		self.poder_saltar = True

	def update(self):
		self.velocidad += GRAVEDAD
		self.pos_y += self.velocidad + 0.5 * GRAVEDAD

		self.rect.bottom = self.pos_y

	def saltar(self):
		if self.poder_saltar:
			self.velocidad = SALTO
			self.poder_saltar = False

	def validar_plataforma(self, plataforma):
		result = pygame.sprite.collide_rect(self, plataforma)

		if result:
			self.rebote()
			self.pos_y = plataforma.rect.top

	def rebote(self):
		self.velocidad = self.velocidad * -0.75  


class Plataforma(pygame.sprite.Sprite):

	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface((ANCHO, 30))
		self.image.fill(VERDE)

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y


pantalla = pygame.display.set_mode((ANCHO, LARGO))

reloj = pygame.time.Clock()

hecho = False

plataforma = Plataforma(0, LARGO - 30)
jugador = Jugador(30, LARGO - 30)

lista_elementos = pygame.sprite.Group()

lista_elementos.add(plataforma)
lista_elementos.add(jugador)

while not hecho:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			hecho = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_s:
				jugador.saltar()

	# update
	lista_elementos.update()
	jugador.validar_plataforma(plataforma)

	pantalla.fill(BLANCO)
	lista_elementos.draw(pantalla)
	pygame.display.update()

	reloj.tick(60)

pygame.quit()