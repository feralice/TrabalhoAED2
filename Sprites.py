import pygame
from Configuracoes import *

#inicializa pygame
pygame.font.init()

#classe para criar os quadrados do jogo
class Quadrado(pygame.sprite.Sprite):

    def __init__(self, game, x, y, texto):
        self.grupos = game.sprites
        pygame.sprite.Sprite.__init__(self, self.grupos)
        self.game = game
        self.image = pygame.Surface((TAM_QUADRADO,TAM_QUADRADO))
        self.x, self.y = x, y
        self.texto = texto
        self.rect = self.image.get_rect()

        #coloca as configurações caso o quadradinho não for vazio
        if(self.texto != "vazio"):
            self.font = pygame.font.SysFont("Consolas",50) #fonte e tamanho
            font_surface = self.font.render(self.texto, True, PRETO)
            self.image.fill(LILAS)
            self.font_tam = self.font.size(self.texto)

            #Cálculo para numeros ficarem centralizados nos quadradosradinhos
            drawX = (TAM_QUADRADO/2) - self.font_tam[0]/2
            drawY = (TAM_QUADRADO/2) - self.font_tam[1]/2
            
            #faz os quadradinhos
            self.image.blit(font_surface,(drawX, drawY))
        else:
            #se for vazio, preenche o quadradinho com a cor do fundo
            self.image.fill(CINZA)

    #atualizando os quadrados
    def update(self):

        self.rect.x = self.x *TAM_QUADRADO
        self.rect.y = self.y *TAM_QUADRADO

    #Mostrar o mouse dentro da tela feita
    def click(self, mouse_x, mouse_y):
        #checa a posição do mouse
        return self.rect.left <= mouse_x <= self.rect.right and self.rect.top <= mouse_y <= self.rect.bottom

    #checa a direita do quadradinho, para ver se está vazio
    def checkDireita(self):
        return self.rect.x + TAM_QUADRADO < TAM_JOGO * TAM_QUADRADO

    #checa a esquerda do quadradinho, para ver se está vazio
    def checkEsquerda(self):
        return self.rect.x - TAM_QUADRADO >= 0

    #checa acima do quadradinho, para ver se está vazio
    def checkCima(self):
        return self.rect.y - TAM_QUADRADO >= 0

    #checa abaixo do quadradinho, para ver se está vazio
    def checkBaixo(self):
        return self.rect.y + TAM_QUADRADO < TAM_JOGO * TAM_QUADRADO


#classe para utilizarmos para colocar os elementos gráficos na tela
class ElemGraficos:
    def __init__(self, x, y, texto):
        self.x = x
        self.y = y
        self.texto = texto

    #desenha na tela
    def draw(self,screen):
        font = pygame.font.SysFont("Consolas",50) #escolhe a fonte
        texto = font.render(self.texto, True, LILAS)
        screen.blit(texto, (self.x,self.y))

#Classe para os botões da tela
class Botao:
    def __init__(self, x, y, largura, altura, texto, cor, cor_texto):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.texto = texto
        self.cor = cor
        self.cor_texto = cor_texto

    def draw(self, screen):

        #desenha um retangulo
        pygame.draw.rect(screen, self.cor, (self.x, self.y, self.largura, self.altura))

        font = pygame.font.SysFont("Consolas", 30) #escolhe a fonte
        texto = font.render(self.texto, True, self.cor_texto)
        self.font_tam = font.size(self.texto)

        #calculo para centralizar o texto
        drawX = self.x + (self.largura/2) - self.font_tam[0]/2
        drawY = self.y + (self.altura/2) - self.font_tam[1]/2
        
        #adiciona o texto
        screen.blit(texto,(drawX, drawY))

    #verificar se é "Clicavel"
    def click(self, mouse_x, mouse_y):
        #checa a posição do mouse
        return self.x <= mouse_x <= self.x + self.largura and self.y <= mouse_y <= self.y + self.altura
