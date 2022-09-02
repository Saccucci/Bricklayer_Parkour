import pygame
from settings import *
game_speed = 4

class Fundo(pygame.sprite.Sprite):         # Cria a classe fundo

    def __init__(self, xpos, indice):       # define parametros da Classe fundo
        super().__init__()
        
        self.sprites = []
        self.sprites.append(pygame.image.load('graphics/bg/fundo_movel/0.png').convert_alpha())
        self.sprites.append(pygame.image.load('graphics/bg/fundo_movel/1.png').convert_alpha())
        self.sprites.append(pygame.image.load('graphics/bg/fundo_movel/2.png').convert_alpha())
        
        self.image = self.sprites[indice]       #Escolhendo o Sprite que será mostrado
        self.image = pygame.transform.scale(self.image, (screen_width,screen_height))

        self.rect = self.image.get_rect()                   # pega o retangulo da imagem (0,0,fundox,fundoy)
        self.rect[0] = xpos                                 # muda o primeiro parametro por xpos (esse,0,fundox,fundoy)
        self.rect[1] = 0        # muda o segundo parametro (0,esse,fundox,fundoy)
    
    def update(self):       #atualizar coisas 'nesse caso para o fundo'
        self.rect[0] -= game_speed
    
def is_off_screen(sprite):  # define se o sprite está fora da tela
    return sprite.rect[0] < -(sprite.rect[2])