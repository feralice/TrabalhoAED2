import pygame
import random
import time
from configuracoes import *
from sprite import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

    def create_game(self):
        estadoFinal = [[0,1,2],[3,4,5],[6,7,8]]
        return estadoFinal

    def draw_tiles(self):
        self.tiles = []
        for i, x in enumerate(self.tiles_lista):
            self.tiles.append([])
            for j, tile in enumerate(x):
                if tile != 0:
                    self.tiles[i].append(Tile(self, j, i, str(tile)))
                else:
                    self.tiles[i].append(Tile(self, j, i, "empty"))
        
    def new(self):
        #cria um novo jogo
        self.all_sprites = pygame.sprite.Group()
        self.tiles_lista = self.create_game()
        self.tiles_lista_completo = self.create_game()

        self.listaBotoes = []
        self.listaBotoes.append(Botao(650, 100, 300, 50, "Gerar Aleatório", WHITE, BLACK))
        self.listaBotoes.append(Botao(650, 170, 300, 50, "Recomeçar", WHITE, BLACK))


        #começa um jogo novo e mostra o estado final ao inicializar
        self.draw_tiles()
        

    def run(self):
        self.playing = True
        while(self.playing):
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def update(self):
        self.all_sprites.update()

    def draw_grid(self):
        for i in range(-1,GAME_SIZE*TILESIZE, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY,(i,0),(i, GAME_SIZE*TILESIZE))
        for j in range(-1,GAME_SIZE*TILESIZE, TILESIZE):
            pygame.draw.line(self.screen,LIGHTGREY,(0,j),(GAME_SIZE*TILESIZE,j))


    def draw(self):
        self.screen.fill(BGjOUR)
        self.all_sprites.draw(self.screen)
        self.draw_grid()

        #cria os botoes do jogo
        for botao in self.listaBotoes:
           botao.draw(self.screen)

        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit(0)
            
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mouseX, mouseY = pygame.mouse.get_pos()
                for i, tiles in enumerate(self.tiles):
                    for j, tile in enumerate(tiles):
                        if tile.click(mouseX, mouseY):
                            #checa se a direita do numero clicado está vazio e troca, se estiver
                            if (tile.checkDireita() and self.tiles_lista[i][j + 1] == 0):
                                self.tiles_lista[i][j], self.tiles_lista[i][j + 1] = self.tiles_lista[i][j + 1], self.tiles_lista[i][j] # faz a troca

                            #checa se a esquerda do numero clicado está vazio e troca, se estiver
                            if(tile.checkEsquerda() and self.tiles_lista[i][j-1]==0):
                                self.tiles_lista[i][j], self.tiles_lista[i][j - 1] = self.tiles_lista[i][j - 1], self.tiles_lista[i][j] # faz a troca
                                
                            #checa se em cima do numero clicado está vazio e troca, se estiver
                            if(tile.checkCima() and self.tiles_lista[i-1][j]==0):
                                self.tiles_lista[i][j], self.tiles_lista[i-1][j] = self.tiles_lista[i-1][j], self.tiles_lista[i][j] # faz a troca

                            #checa se em baixo do numero clicado está vazio e troca, se estiver
                            if(tile.checkBaixo() and self.tiles_lista[i+1][j]==0):
                                self.tiles_lista[i][j], self.tiles_lista[i+1][j] = self.tiles_lista[i+1][j], self.tiles_lista[i][j] # faz a troca

                            
                            self.draw_tiles()

                for botao in self.listaBotoes:
                    #verifica qual o botão que foi clicado
                    if(botao.click(mouseX,mouseY)):
                        if(botao.text == "Gerar Aleatório"):
                            print("oi")





game = Game()
while True:
    game.new()
    game.run()
