import pygame

pontuar = 1000
pontos = 0
font = pygame.font.SysFont('arial', 20, True, True) #1- qual font, tamanho, negrito, itálico


instrucao = pygame.image.load('graphics/bg/how2play.png').convert_alpha()
post_it = pygame.image.load('graphics/main/how_2_play.png').convert_alpha()

# TECLAS ANIMADAS

teclas_animadas = []
teclas_animadas.append(pygame.image.load('graphics/main/w.png').convert_alpha())
teclas_animadas.append(pygame.image.load('graphics/main/w_.png').convert_alpha())
teclas_animadas.append(pygame.image.load('graphics/main/a.png').convert_alpha())
teclas_animadas.append(pygame.image.load('graphics/main/a_.png').convert_alpha())
teclas_animadas.append(pygame.image.load('graphics/main/s.png').convert_alpha())
teclas_animadas.append(pygame.image.load('graphics/main/s_.png').convert_alpha())
teclas_animadas.append(pygame.image.load('graphics/main/d.png').convert_alpha())
teclas_animadas.append(pygame.image.load('graphics/main/d_.png').convert_alpha())
teclas_animadas.append(pygame.image.load('graphics/main/e.png').convert_alpha())
teclas_animadas.append(pygame.image.load('graphics/main/e_.png').convert_alpha())
teclas_animadas.append(pygame.image.load('graphics/main/ctrl.png').convert_alpha())
teclas_animadas.append(pygame.image.load('graphics/main/ctrl_.png').convert_alpha())
teclas_animadas.append(pygame.image.load('graphics/main/space.png').convert_alpha())
teclas_animadas.append(pygame.image.load('graphics/main/space_.png').convert_alpha())
teclas_animadas.append(pygame.image.load('graphics/main/h.png').convert_alpha())
teclas_animadas.append(pygame.image.load('graphics/main/h_.png').convert_alpha())
teclas_animadas[14] = pygame.transform.scale(teclas_animadas[14], (128,128))
teclas_animadas[15] = pygame.transform.scale(teclas_animadas[15], (128,128))
teclas_animadas[14] = pygame.transform.rotate(teclas_animadas[14], -10)
teclas_animadas[15] = pygame.transform.rotate(teclas_animadas[15], -10)



w = 0
a = 2
s = 4
d = 6
e = 8
ctrl = 10
space = 12
h = 14