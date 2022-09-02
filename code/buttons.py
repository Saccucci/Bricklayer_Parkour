import pygame

Tam_Button = 128

class Start_button(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('graphics/main/start_menu_1.png').convert_alpha())
        self.sprites.append(pygame.image.load('graphics/main/start_menu_2.png').convert_alpha())
        self.sprites[0] = pygame.transform.rotate(self.sprites[0], 10)
        self.sprites[1] = pygame.transform.rotate(self.sprites[1], 10)
        
        
        self.atual = 0
        self.image = self.sprites[self.atual]
        
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (Tam_Button,Tam_Button))
        
        self.rect.topleft = (xpos, ypos)
        
        self.clicked = False

    def update(self):
        self.atual += 0.05
        if self.atual >= 2:
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        
    def draw(self, surface):
        action = False
		# Pega a posição do mouse
        pos = pygame.mouse.get_pos()
        
        #Verifica se o mouse foi clicado e se o cliked == False
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

		#Desenha o Botão na tela
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action



# EXIT Button

class Exit_button(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('graphics/main/exit_menu_1.png').convert_alpha())
        self.sprites.append(pygame.image.load('graphics/main/exit_menu_2.png').convert_alpha())
        self.sprites[0] = pygame.transform.rotate(self.sprites[0], 10)
        self.sprites[1] = pygame.transform.rotate(self.sprites[1], 10)
        
        
        self.atual = 0
        self.image = self.sprites[self.atual]
        
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (Tam_Button,Tam_Button))
        self.rect.topleft = (xpos, ypos)
        
        self.clicked = False

    def update(self):
        self.atual += 0.05
        if self.atual >= 2:
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        
    def draw(self, surface):
        action = False
		# Pega a posição do mouse
        pos = pygame.mouse.get_pos()

        #Verifica se o mouse foi clicado e se o cliked == False
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

		# Desenha o Botão na tela
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

