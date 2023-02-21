import pygame
from configuracoes import *

pygame.font.init()

class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, text):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        self.x, self.y = x, y
        self.text = text
        self.rect = self.image.get_rect()

        if(self.text != "empty"):
            self.font = pygame.font.SysFont("Consolas",50)
            font_surface = self.font.render(self.text, True, BLACK)
            self.image.fill(WHITE)
            self.font_size = self.font.size(self.text)

            #Cálculo para numeros ficarem centralizados nos quadradinhos
            drawX = (TILESIZE/2) - self.font_size[0]/2
            drawY = (TILESIZE/2) - self.font_size[1]/2
            
            #faz os quadradinhos
            self.image.blit(font_surface,(drawX, drawY))

    def update(self): #atualizando o quadradinho
        self.rect.x = self.x *TILESIZE
        self.rect.y = self.y *TILESIZE

    #Mostrar o mouse dentro da tela feita
    def click(self, mouse_x, mouse_y):
        #checa a posição do mouse
        return self.rect.left <= mouse_x <= self.rect.right and self.rect.top <= mouse_y <= self.rect.bottom


