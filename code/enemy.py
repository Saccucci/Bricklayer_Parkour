import pygame, time
from support import import_folder
from settings import *


class P_b(pygame.sprite.Sprite):    # Pássaro Branco
    def __init__(self,pos, enemy_size):
        super().__init__()
        self.import_enemy_assets()
        self.frame_index = 0
        self.animation_speed = 0.1
        self.image = self.animations['comendo'][self.frame_index]
        self.image = pygame.transform.scale(self.image, (enemy_size,enemy_size))
        # self.image = pygame.Surface((enemy_size,enemy_size),pygame.SRCALPHA)
        # self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        self.facing_left = True
        self.enemy_size = enemy_size
        self.passaro_branco_time = 10000
        
        #status
        self.status = 'comendo'
        self.time_animation = time.time()
        self.levantou = False
        self.speed = 0
        self.speed2 = 0
        
    def import_enemy_assets(self):
        enemy_path = 'graphics/enemy_sprites/passaro/branco/'
        self.animations = {'comendo':[],'levantando':[],'voando':[]}

        for animation in self.animations.keys():
            full_path = enemy_path + animation
            self.animations[animation] = import_folder(full_path)
            
    def animate(self):
        animation = self.animations[self.status]

        # loop over frame index 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_left:
            self.image = image
            self.image = pygame.transform.scale(self.image, (self.enemy_size,self.enemy_size))
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            
            self.image = flipped_image
            self.image = pygame.transform.scale(self.image, (self.enemy_size,self.enemy_size))
            
        self.rect = self.image.get_rect(topleft = self.rect.topleft)
        
    def saiu_da_tela(self):
        if self.rect.x <= -10:
            self.kill()
            
    def esta_voando(self):
        if self.status == 'voando':
            self.speed = 10
        else:
            self.speed = 1
    def atualizax(self):
        self.rect.x -= self.speed
        self.rect.x -= self.speed2
        
            
    def update(self):
        self.esta_voando()
        self.atualizax()
        self.animate()
        self.saiu_da_tela()
        
class Objetos_que_caem(pygame.sprite.Sprite):
    def __init__(self,pos, enemy_size, name, imagem):
        super().__init__()
        self.name = name
        self.image = imagem
        self.image = pygame.transform.scale(self.image, (enemy_size,enemy_size))
        self.rect = self.image.get_rect(topleft = pos)
        
    def cair(self):
        self.rect.y += 10

    def update(self):
        self.cair()
        
class P_a(pygame.sprite.Sprite):    # Pássaro Branco
    def __init__(self,pos, enemy_size):
        super().__init__()
        self.import_enemy_assets()
        self.frame_index = 0
        self.animation_speed = 0.1
        self.image = self.animations['comendo'][self.frame_index]
        self.image = pygame.transform.scale(self.image, (enemy_size,enemy_size))
        # self.image = pygame.Surface((enemy_size,enemy_size),pygame.SRCALPHA)
        # self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        self.facing_left = True
        self.enemy_size = enemy_size
        self.passaro_branco_time = 10000
        
        #status
        self.status = 'comendo'
        self.time_animation = time.time()
        self.levantou = False
        self.speed = 0
        self.speed2 = 0
        
    def import_enemy_assets(self):
        enemy_path = 'graphics/enemy_sprites/passaro/azul/'
        self.animations = {'comendo':[],'levantando':[],'voando':[]}

        for animation in self.animations.keys():
            full_path = enemy_path + animation
            self.animations[animation] = import_folder(full_path)
            
    def animate(self):
        animation = self.animations[self.status]

        # loop over frame index 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_left:
            self.image = image
            self.image = pygame.transform.scale(self.image, (self.enemy_size,self.enemy_size))
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            
            self.image = flipped_image
            self.image = pygame.transform.scale(self.image, (self.enemy_size,self.enemy_size))
            
        self.rect = self.image.get_rect(topleft = self.rect.topleft)
        
    def saiu_da_tela(self):
        if self.rect.x <= -10:
            self.kill()
            
    def esta_voando(self):
        if self.status == 'voando':
            self.speed = 8
        else:
            self.speed = 1
    def atualizax(self):
        self.rect.x -= self.speed
        self.rect.x -= self.speed2
        
            
    def update(self):
        self.esta_voando()
        self.atualizax()
        self.animate()
        self.saiu_da_tela()