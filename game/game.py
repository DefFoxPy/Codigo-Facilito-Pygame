import os
import pygame
import sys
import random

from .config import *
from .platform import Platform
from .player import Player
from .wall import Wall
from .coin import Coin

class Game:
	def __init__(self):
		pygame.init()

		self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption(TITLE)

		self.running = True
		self.playing = True

		self.clock = pygame.time.Clock()

		self.font = pygame.font.match_font(FONT)

		self.dir = os.path.dirname(__file__)
		self.dir_sounds = os.path.join(self.dir, 'sources/sounds')

	def start(self):
		self.new()

	def new(self):
		self.score = 0
		self.level = 0
		self.generate_elements()
		self.run()

	def generate_elements(self):
		self.platform = Platform()
		self.player = Player(100, self.platform.rect.top - 200)

		self.sprites = pygame.sprite.Group()
		self.walls = pygame.sprite.Group()
		self.coins = pygame.sprite.Group()

		self.sprites.add(self.platform)
		self.sprites.add(self.player)

		self.generate_walls()

	def generate_walls(self):

		last_position = WIDTH + 100

		if not len(self.walls) > 0: # si no existen osbtaculos
			
			for w in range(0, MAX_WALLS):
				left = random.randrange(last_position + 200, last_position + 400)
				wall = Wall(left, self.platform.rect.top)
				last_position = wall.rect.right

				self.walls.add(wall)
				self.sprites.add(wall)

			self.level += 1
			self.generate_coin()

	def generate_coin(self):

		last_position = WIDTH + 100

		for c in range(0, MAX_COINS):
			pos_x = random.randrange(last_position + 180, last_position + 300)
			coin = Coin(pos_x, 150)
			last_position = coin.rect.right

			self.coins.add(coin)
			self.sprites.add(coin)

	def run(self):
		while self.running:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()
			

	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
				pygame.quit()
				sys.exit()

		key = pygame.key.get_pressed()

		if key[pygame.K_SPACE]:
			self.player.jump()

	def draw(self):
		self.surface.fill(BLACK)
		self.draw_text()
		self.sprites.draw(self.surface)
		pygame.display.flip()

	def update(self):

		if not self.playing:
			return

		self.sprites.update()

		self.player.validate_platform(self.platform)

		wall = self.player.collide_with(self.walls)
		if wall:
			if self.player.collide_bottom(wall):
				self.player.skid(wall)
			else:
				self.stop()

		coin = self.player.collide_with(self.coins)
		if coin:
			self.score += 1
			coin.kill()

			sound = pygame.mixer.Sound(os.path.join(self.dir_sounds, 'coin.wav'))
			sound.play()

		self.update_elements(self.walls)
		self.update_elements(self.coins)

		self.generate_walls()

	def update_elements(self, elements):
		for element in elements:
			if not element.rect.right > 0:
				element.kill()

	def stop(self):
		self.player.stop()
		self.stop_elements(self.walls)

		self.playing = False

		sound = pygame.mixer.Sound(os.path.join(self.dir_sounds, 'lose.wav'))
		sound.play()


	def stop_elements(self, elements):
		for element in elements:
			element.stop()

	def draw_text(self):
		self.display_text(str('Score: {}'.format(self.score)), 36, WHITE, WIDTH // 2, TEXT_POSY)
		self.display_text(str('Level: {}'.format(self.level)), 36, WHITE, 60, TEXT_POSY)

		if not self.playing:
			self.display_text('Perdiste', 60, WHITE, WIDTH // 2, HEIGHT // 2)
			self.display_text('Preciona r para jugar de nuevo', 30, WHITE, WIDTH // 2, 100)		

	def display_text(self, text, size, color, pos_x, pos_y):
		font = pygame.font.Font(self.font, size)
		
		text = font.render(text, True, color)
		rect = text.get_rect()
		rect.midtop = (pos_x, pos_y)

		self.surface.blit(text, rect)