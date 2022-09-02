import pygame, sys
from settings import * 
from level import Level
from gerador_mapas import *
from buttons import *

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
start_button = Start_button((screen_width//2 - 380), (screen_height//2))
exit_button = Exit_button((screen_width//2 - 280), (screen_height//2 + 40))
level = 0
fundo_menu = pygame.image.load('graphics/bg/fundo_jogo.png').convert_alpha()
# primeira_vez = True
highscore = 0
bg_indice = 0
from fundo import *
from teclas_animadas import *

musica_menu = pygame.mixer.music.load('sound/Obra.mp3')  # pygame.mixer.mixer() Só aceita MP3 


# if not prime ira_vez:
# 	# ler highscore
arq_ = open('highscore.txt', 'r')
highscore = arq_.readline()
highscore = int(highscore)
	# print(type(highscore))

def criar_level():
	global level
	level = Level(lista_gameplay,screen)

criar_level()

fundo_group = pygame.sprite.Group()    # Cria um Grupo

def criar_fundo():
	for i in range(2):          # Cria no máximo 2 i onde i é o número de vezes, na primeira interação i vale 0, na segunda i vale 1, ...
		fundo = Fundo(screen_width * i, i)   # xpos = (SCREENX * i) isso é o x do primeiro fundo, o segundo vai estar lá na frente, depois de toda a largura do fundo
		fundo_group.add(fundo)    # adiciona no grupo

criar_fundo()

def desenhar_fundo():
	global bg_indice
	if is_off_screen(fundo_group.sprites()[0]): # Testa se o primeiro fundo do grupo [0] está fora da tela
		fundo_group.remove(fundo_group.sprites()[0]) # Se SIM apaga aquele fundo

		new_fundo = Fundo((screen_width * 1) - 10, bg_indice)      #cria um new fundo onde a xpos é (SCREENX * 4) --- '-10' pq sobrava um espacinho
		if bg_indice < 2:
			bg_indice += 1
		else:
			bg_indice = 0
		fundo_group.add(new_fundo)
			
			
	fundo_group.draw(screen)
	fundo_group.update()

def apagar_fundo():
	fundo_group.empty() # Se SIM apaga aquele fundo

def morrer():
	if level.saiu_da_tela():
		return True
	if level.cair():
		return True
	if level.colision_player_passaro():
		return True
	if level.colision_player_obstaculos():
		return True
	return False

def play_music():
    pygame.mixer.music.play(-1) # -1 começa a tocar denovo (em looping)
    
def stop_music():
    pygame.mixer.music.stop() # parar a musica


while True:
	tempo_jogado = pygame.time.get_ticks()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	# screen.fill('yellow')
	screen.blit(fundo_menu, (0,0))
	mousex, mousey = pygame.mouse.get_pos()
	if start_button.rect.collidepoint(mousex,mousey):
		if pygame.mouse.get_pressed()[0]:
			estado = 'game'
			apagar_fundo()
			criar_fundo()
			criar_level()
			play_music()
			pontos = 0
			pontuar = tempo_jogado + 1000
			level.tempo_criacao_obj_caem = level.agora + 5000
	if exit_button.rect.collidepoint(mousex,mousey):
		if pygame.mouse.get_pressed()[0]:
			pygame.quit()
			sys.exit()
	if estado == 'menu':						# menu
		keys = pygame.key.get_pressed()
		if keys[pygame.K_h]:
			estado = 'how_to_play'
			apagar_fundo()
			criar_fundo()
		screen.blit(fundo_menu, (0,0))
		h += 0.15
		if h >= 16:
			h = 14
		screen.blit(teclas_animadas[int(h)], ((screen_width//2 + 200), (screen_height//2 + 30)))
		start_button.draw(screen)
		exit_button.draw(screen)
		start_button.update()
		exit_button.update()
	elif estado == 'game':						# game
		desenhar_fundo()
		if tempo_jogado - pontuar >= 0:
			pontos += 1
			pontuar += 1000
		level.run()
		if morrer():
			stop_music()
			if highscore < pontos: #or primeira_vez:
				highscore = pontos
				arq = open('highscore.txt', 'w')
				arq.write(str(pontos))
				arq.close()
				primeira_vez = False
			estado = level.limpar()
			criar_level()
		score = font.render(f' Pontos: {int(pontos)}', True, (0,0,0))
		screen.blit(score, (50,50)) 
		hs = font.render(f' HighScore: {int(highscore)}', True, (0,0,0))
		screen.blit(hs, (50,20)) 
		#teclas game
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LCTRL] and estado == 'game':	# Apertar M para voltar pro menu
			estado = level.limpar()
			print(estado)
			stop_music()
	elif estado == 'how_to_play':					# how to play
		desenhar_fundo()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_e] or keys[pygame.K_LCTRL]:
			estado = 'menu'
		screen.blit(instrucao, (0,0)) # 800,600
		screen.blit(post_it, (700,570)) # 800,600
		w += 0.15
		a += 0.15
		s += 0.15
		d += 0.15
		e += 0.15
		ctrl += 0.15
		space += 0.15

		if w >= 2:
			w = 0
		if a >= 4:
			a = 2
		if s >= 6:
			s = 4
		if d >= 8:
			d = 6
		if e >= 10:
			e = 8
		if ctrl >= 12:
			ctrl = 10
		if space >= 14:
			space = 12
		screen.blit(teclas_animadas[int(w)], (610,130))
		screen.blit(teclas_animadas[int(a)], (650,130))
		screen.blit(teclas_animadas[int(s)], (690,130))
		screen.blit(teclas_animadas[int(d)], (730,130))
		screen.blit(teclas_animadas[int(e)], (665,490)) #(810,255)
		screen.blit(teclas_animadas[int(ctrl)], (665,310))
		screen.blit(teclas_animadas[int(space)], (680,220))



	
	# print(lista_mapas)

	pygame.display.update()
	clock.tick(60)