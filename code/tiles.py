import pygame 

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,size):
		super().__init__()
		self.image = pygame.image.load('graphics/bg/dirt.png').convert_alpha()
		self.image = pygame.transform.scale(self.image, (32,32))
		# self.image.fill('grey')
		self.rect = self.image.get_rect(topleft = pos)
		self.name = 'tile'

	def update(self,x_shift):
		self.rect.x += x_shift