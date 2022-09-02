import pygame, random 
from tiles import Tile 
from marcador import Marcador 
from settings import *
from gerador_mapas import *
from player import Player
from particles import ParticleEffect
from enemy import *
from obstaculos import *


# linha_lay = 0
# col_lay = 0
# lin_map = 0
# col_map = 0

class Level (pygame.sprite.Sprite):
	def __init__(self,layout,surface):
		super().__init__()
		#marcador
		self.linha_del = linha_del
		self.linha_add = linha_add
		self.primeira_vez = True
		self.obstaculos = pygame.sprite.Group()
		self.tempo_criacao_obj_caem = 5000
		self.itens_que_caem = []
		self.itens_que_caem.append(pygame.image.load('graphics/enemy_sprites/objetos_caem/Bloco0.png').convert_alpha())
		self.itens_que_caem.append(pygame.image.load('graphics/enemy_sprites/objetos_caem/Cimento0.png').convert_alpha())
		self.itens_que_caem.append(pygame.image.load('graphics/enemy_sprites/objetos_caem/Tijolo0.png').convert_alpha())
		self.agora = pygame.time.get_ticks()
  
		#gerar mapas
		# self.outros_mapas = outros_mapas
		
		# level setup
		self.display_surface = surface
		self.layout = layout
		self.setup_level(self.layout)
		self.world_shift = 0
		self.current_x = 0

		# dust 
		self.dust_sprite = pygame.sprite.GroupSingle()
		self.player_on_ground = False

	def create_jump_particles(self,pos):
		if self.player.sprite.facing_right:
			pos -= pygame.math.Vector2(10,5)
		else:
			pos += pygame.math.Vector2(10,-5)
		jump_particle_sprite = ParticleEffect(pos,'jump')
		self.dust_sprite.add(jump_particle_sprite)

	def get_player_on_ground(self):
		if self.player.sprite.on_ground:
			self.player_on_ground = True
		else:
			self.player_on_ground = False

	def create_landing_dust(self):
		if not self.player_on_ground and self.player.sprite.on_ground and not self.dust_sprite.sprites():
			if self.player.sprite.facing_right:
				offset = pygame.math.Vector2(10,15)
			else:
				offset = pygame.math.Vector2(-10,15)
			fall_dust_particle = ParticleEffect(self.player.sprite.rect.midbottom - offset,'land')
			self.dust_sprite.add(fall_dust_particle)

	def setup_level(self,layout):
		self.tiles = pygame.sprite.Group()
		self.player = pygame.sprite.GroupSingle()
		self.marcadores = pygame.sprite.Group()
		self.marcadores2 = pygame.sprite.Group()
		self.pas_b = pygame.sprite.Group()
		self.pas_a = pygame.sprite.Group()


		# while layout[linha_lay][col_lay][lin_map][col_map] <= layout[linha_lay][col_lay][lin_map][55]:
		# for l_index,l in enumerate (layout):
		# 	for c_index,c in enumerate (l):
		for c_index, c in enumerate (layout):
			for row_index,row in enumerate(c):
				for col_index,cell in enumerate(row):
					self.c_index = c_index
					x = col_index * tile_size + (tam_map * self.c_index)
					y = row_index * tile_size
					# print(layout[l_index][c_index]) # -- 56
					# print(len(layout)) # -- 2
					# print(layout)	# --- chega a bugar -- Printa muita coisa
					# print(len(l))   # --- 22
					# print(l)	# chega a bugar // recebe os mapas (0 e 1) 22 vezes (eu acho)
					# print(len(c))  # --- 56
					# print(c)		# --- recebe o mapa1 56 vezes
					# print(row)	# Recebe um mapa fininho
					# print(len(row))  # --- 1
					# print(row_index)	# --- 0 até 55
					# shift + tab --- tab inverso
					# print(l_index) --- mostra 111111 -- 0 a 1
					# print(c_index) --- em qual mapa está 22 vezes

					
					if cell == 'X':
						tile = Tile((x,y),tile_size)
						self.tiles.add(tile)
					if cell == 'P':
						player_sprite = Player((x,y),self.display_surface,self.create_jump_particles)
						self.player.add(player_sprite)
					if cell == 'M':
						marca = Marcador((x,y),tile_size,'ma')
						self.marcadores.add(marca)
					if cell == 'J':
						marca2 = Marcador((x,y),tile_size,'ja')
						self.marcadores2.add(marca2)
					if cell == 'E':
						tipo = random.randint(0,1)
						if tipo == 0:
							passaro_b = P_b((x,y),tile_size)
							self.pas_b.add(passaro_b)
						else:
							passaro_a = P_a((x,y+5),tile_size)
							self.pas_a.add(passaro_a)
					if cell == 'T':
						tramp = Trampolim((x,y),tile_size, 'tramp')
						self.obstaculos.add(tramp)

	def scroll_x(self):
		player = self.player.sprite
		player_x = player.rect.centerx
		direction_x = player.direction.x
		# if player_x < screen_width / 4 and direction_x < 0:
		# 	self.world_shift = 8
		# 	player.speed = 0
		if player_x > screen_width - (screen_width / 4) and direction_x > 0:
			self.world_shift = -8
			player.speed = 0
			for sprite in self.pas_b.sprites():
				sprite.speed2 = 8
			for sprite in self.obstaculos.sprites():
				sprite.speed2 = 8
		else:
			self.world_shift = 0
			player.speed = 8
			for sprite in self.pas_b.sprites():
				sprite.speed2 = 0
			for sprite in self.obstaculos.sprites():
				sprite.speed2 = 0

	def horizontal_movement_collision(self):
		player = self.player.sprite
		player.rect.x += player.direction.x * player.speed

		# colisão com tiles
		for sprite in self.tiles.sprites():
			if sprite.rect.colliderect(player.rect):
				if player.direction.x < 0: 
					player.rect.left = sprite.rect.right
					player.on_left = True
					self.current_x = player.rect.left
				elif player.direction.x > 0:
					player.rect.right = sprite.rect.left
					player.on_right = True
					self.current_x = player.rect.right

		if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
			player.on_left = False
		if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
			player.on_right = False
   
	def generate_map(self,direita_ma):
		print('entrou')
		# self.c_index += 1
		for row_index,row in enumerate(self.aleatorio):
			for col_index,cell in enumerate(row):
						
						x = col_index * tile_size + direita_ma#(tam_map * self.c_index)
						y = row_index * tile_size
						
						if cell == 'X':
							tile = Tile((x,y),tile_size)
							self.tiles.add(tile)
						if cell == 'M':
							marca = Marcador((x,y),tile_size, 'ma')
							self.marcadores.add(marca)
						if cell == 'J':
							marca2 = Marcador((x,y),tile_size, 'ja')
							self.marcadores2.add(marca2)
						if cell == 'E':
							tipo = random.randint(0,1)
							if tipo == 0:
								passaro_b = P_b((x,y),tile_size)
								self.pas_b.add(passaro_b)
							else:
								passaro_a = P_a((x,y+5),tile_size)
								self.pas_a.add(passaro_a)
						if cell == 'T':
							tramp = Trampolim((x,y),tile_size, 'tramp')
							self.obstaculos.add(tramp)
   
	def deletar_mapa(self):
		for sprite in self.tiles.sprites():
			if sprite.name == 'ma' and sprite.rect.right <= self.linha_del:
				# deletar mapa
				# self.layout.remove([0][0])
				# del self.layout[0][0]  # esse deleta
				pass


	def add_map(self):
		# player = self.player.sprite
		# player_r = player.rect.right
		# print(player_r)
		if self.primeira_vez == True:
			self.aleatorio = random.choice(lista_mapas)
			self.generate_map(1792)
			self.primeira_vez = False
			self.linha_add = 1792
			print(self.c_index)
		else:
			for sprite in self.marcadores.sprites():
				if sprite.name == 'ma':
					# print(sprite.rect.right)
					for sprite2 in self.marcadores2.sprites():
						if ( sprite2.name == 'ja') and sprite2.rect.left <= self.linha_add:
							sprite.name = 'mo'
							sprite2.name = 'jo'
							self.aleatorio = random.choice(lista_mapas)
							self.generate_map(sprite.rect.right + 320)
							self.linha_add = 1792

								
							# self.tiles.remove(sprite)
							# self.layout.append(random.choice(lista_mapas))
							# print(len(self.layout))
							# print(self.c_index)
						# 	del self.layout[0][0]  # esse deleta
						# 	self.tiles.empty()

						# if not self.tiles:
						# 	self.setup_level(self.layout)

	def limpar(self):
		estado = 'menu'
		print('veio do limpar')
		# print(len(self.player))
		# self.tiles.empty()
		# self.marcadores.empty()
		# self.player.empty()
		self.kill()
		return estado

	def cair(self):
		player = self.player.sprite
		if player.rect.y > screen_height:
			return True
		return False

	def saiu_da_tela(self):
		player = self.player.sprite
		if player.rect.left < 0:
			return True
		return False
   
	def move_map(self):
		player = self.player.sprite
		self.world_shift -= 1
		# player.rect.x -= 1
		self.linha_del -= self.world_shift
		if player.speed > 0:
			self.linha_add = player.speed
		else:
			self.linha_add = 8
		# self.linha_add += player.speed #self.world_shift

	def get_status_p_b(self):
		self.ja_levantou(self.pas_b)
		self.viu_player(self.pas_b)
		if not self.viu_player(self.pas_b) and not self.ja_levantou(self.pas_b):
			for sprite in self.pas_b.sprites():
				sprite.status = 'comendo'
				# sprite.rect.x -= 1
    
	def get_status_p_a(self):
		self.ja_levantou(self.pas_a)
		self.viu_player(self.pas_a)
		if not self.viu_player(self.pas_a) and not self.ja_levantou(self.pas_a):
			for sprite in self.pas_a.sprites():
				sprite.status = 'comendo'
			
	def viu_player(self, grupo):
		player = self.player.sprite
		# pas_b = self.pas_b.sprites()
		for sprite in grupo.sprites():
			if sprite.rect.x - player.rect.x <= 400 and sprite.levantou == False:
				if sprite.passaro_branco_time >= -50:
					sprite.passaro_branco_time -= 50
				sprite.status = 'levantando'
				# sprite.rect.x -= 1
				return True
		return False

	def ja_levantou(self, grupo):
		player = self.player.sprite
		# pas_b = self.pas_b.sprites()
		for sprite in grupo.sprites():
			if sprite.rect.x - player.rect.x <= 400 and self.viu_player(grupo) and sprite.passaro_branco_time <= 0:
				sprite.levantou = True
			if sprite.levantou:
				sprite.status = 'voando'
				if grupo == self.pas_a:
					if player.rect.y > sprite.rect.y:
						sprite.rect.y += 1
					elif player.rect.y < sprite.rect.y:
						sprite.rect.y -= 1
				return True
		return False

	def criar_objetos_caem(self):
		self.agora = pygame.time.get_ticks()
		if self.agora >= self.tempo_criacao_obj_caem:
			player = self.player.sprite 
			self.imagem_obj_cai = random.choice(self.itens_que_caem)
			obj_cai = Objetos_que_caem((player.rect.x,-200),tile_size,'cai', self.imagem_obj_cai)
			self.obstaculos.add(obj_cai)
			self.tempo_criacao_obj_caem += 10000
   
	def colision_player_obstaculos(self):
		player = self.player.sprite
		for sprite in self.obstaculos.sprites():
			if player.rect.colliderect(sprite.rect):
				if sprite.name == 'cai':
					return True
				if sprite.name == 'tramp' and sprite.rect.top == player.rect.bottom + 10:
					sprite.status = 'pisando'
				else:
					sprite.status = 'normal'
		return False

	def colision_player_passaro(self):
		player = self.player.sprite
		colidiu = pygame.sprite.spritecollide(player, self.pas_a, True)	# se houver algo dentro da lista retorna True
		colidiu1 = pygame.sprite.spritecollide(player, self.pas_b, True)	# se houver algo dentro da lista retorna True
		if colidiu != []:
			return True
		if  colidiu1 != []:
			return True
		return False



	def vertical_movement_collision(self):
		player = self.player.sprite
		player.apply_gravity()

		# colisão com tiles
		for sprite in self.tiles.sprites():
			if sprite.rect.colliderect(player.rect):
				if player.direction.y > 0: 
					player.rect.bottom = sprite.rect.top
					player.direction.y = 0
					player.on_ground = True
				elif player.direction.y < 0:
					player.rect.top = sprite.rect.bottom
					player.direction.y = 0
					player.on_ceiling = True
     
		# colisão com obstáculos x e y
		for sprite in self.obstaculos.sprites():
			if sprite.name == 'tramp':
				# pygame.draw.rect(self.display_surface, (0,0,0) , ((sprite.rect.left,sprite.rect.centery,),(sprite.enemy_size,sprite.enemy_size/2)), 1)
				if sprite.rect.colliderect(player.rect):
					if player.direction.y > 0: 
						player.rect.bottom = sprite.rect.top
						sprite.status = 'pisando'
						player.direction.y = 0
						if sprite.frame_index == 2:
							player.jump_trampolim()
							sprite.status = 'normal'
						player.on_ground = True
					elif player.direction.y < 0:
						player.rect.top = sprite.rect.bottom
						player.direction.y = 0
						player.on_ceiling = True
						sprite.status = 'normal'
					if player.direction.x < 0: 
						player.rect.left = sprite.rect.right
						player.on_left = True
						self.current_x = player.rect.left
						sprite.status = 'normal'
					elif player.direction.x > 0:
						player.rect.right = sprite.rect.left
						player.on_right = True
						self.current_x = player.rect.right
						sprite.status = 'normal'
				# else:
				# 	sprite.status = 'normal'

		if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
			player.on_ground = False
		if player.on_ceiling and player.direction.y > 0.1:
			player.on_ceiling = False


	def run(self):
		global estado
		# dust particles 
		self.dust_sprite.update(self.world_shift)
		self.dust_sprite.draw(self.display_surface)

		#marcadores
		self.marcadores.update(self.world_shift)
		self.marcadores.draw(self.display_surface)
  
		#marcadores2
		self.marcadores2.update(self.world_shift)
		self.marcadores2.draw(self.display_surface)
  
		self.colision_player_passaro()
		#passaro branco
		self.get_status_p_b()
		self.pas_b.update()
		self.pas_b.draw(self.display_surface)
  
		#passaro azul
		self.get_status_p_a()
		self.pas_a.update()
		self.pas_a.draw(self.display_surface)
  
		# obstaculos
		self.criar_objetos_caem()
		self.obstaculos.update()
		self.obstaculos.draw(self.display_surface)
  
		# level tiles
		self.tiles.update(self.world_shift)
		self.tiles.draw(self.display_surface)
		self.scroll_x()
  


		# player
		self.player.update()
		self.horizontal_movement_collision()
		self.get_player_on_ground()
		self.vertical_movement_collision()
		self.create_landing_dust()
		self.cair()
		self.saiu_da_tela()
		self.player.draw(self.display_surface)

		#movimentação mapa e deletar
		# self.deletar_mapa()
		self.move_map()
		self.add_map()
		self.deletar_mapa()


