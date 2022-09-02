import pygame, time
from support import import_folder
from settings import *

class Trampolim(pygame.sprite.Sprite):    # Trampolim  
    def __init__(self,pos, enemy_size, name):
        super().__init__()
        self.t_img = []
        self.t_img.append(pygame.image.load('graphics/obstaculos/0.png').convert_alpha())
        self.t_img.append(pygame.image.load('graphics/obstaculos/1.png').convert_alpha())
        self.t_img.append(pygame.image.load('graphics/obstaculos/2.png').convert_alpha())
        self.t_img[0] = pygame.transform.scale(self.t_img[0], (enemy_size,enemy_size))
        self.t_img[1] = pygame.transform.scale(self.t_img[1], (enemy_size,(enemy_size/4)*3))
        self.t_img[2] = pygame.transform.scale(self.t_img[2], (enemy_size,enemy_size/2))
        
        self.frame_index = 0
        self.name = name
        self.animation_speed = 0.1
        self.image = self.t_img[self.frame_index]
        # self.image = pygame.transform.scale(self.image, (enemy_size,enemy_size))
        self.rect = self.image.get_rect(topleft = pos)
        self.enemy_size = enemy_size
        self.trampolim_time = 10000
        
        #status
        self.status = 'normal'
        self.speed = 1
        self.speed2 = 0
        
    def atualizax(self):
        self.rect.x -= self.speed
        self.rect.x -= self.speed2
        
    def animate(self):
        # print(self.status)
        # temporariox = self.rect.left
        # temporarioy = self.rect.top
        temporario = self.rect.bottomleft
        if self.status == 'pisando':
            # loop over frame index 
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.t_img):
                self.frame_index = 2
                self.animation_speed = 0
        elif self.status == 'normal':
            self.frame_index = 0
            self.animation_speed = 0.1
        image =  self.t_img[int(self.frame_index)]
        self.image = image
            
        self.rect =  self.image.get_rect(bottomleft = temporario) #pygame.Rect(temporariox,temporarioy, self.enemy_size,self.enemy_size/2) #self.image.get_rect(bottomleft = temporario)
        
        
    def update(self):
        self.animate()
        self.atualizax()