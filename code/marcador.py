import pygame 

class Marcador(pygame.sprite.Sprite):
	def __init__(self,pos,size,name):
		super().__init__()
		self.image = pygame.Surface((size,size),pygame.SRCALPHA)
		# self.image.fill('red')
		self.rect = self.image.get_rect(topleft = pos)
		self.name = name

	def update(self,x_shift):
		self.rect.x += x_shift
  
  
# bricklayer_parkour/graphics/marcador/nada.png