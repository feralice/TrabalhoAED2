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
        self.tempo_aleatorio = 0
        self.bCria_aleatorio = False

    def create_game(self):
        estadoFinal = [0,1,2,3,4,5,6,7,8]
        return estadoFinal
    
    def eh_solucionavel(self, puzzle):
            numInversoes = 0

            for i in range(len(puzzle)):
                if(puzzle[i]==0):
                    continue
                for j in range(i+1, len(puzzle)) :
                    if(puzzle[j]==0):
                        continue
                    if puzzle[i] > puzzle[j]:
                        numInversoes+=1

            if(numInversoes)%2==1:
                return False
            else: 
                return True

    def cria_lista_aleatoria(self):

        puzzle = self.tiles_lista.copy()
        random.shuffle(puzzle)

        if(self.eh_solucionavel(puzzle)):
            self.tiles_lista = puzzle
        else:
           return self.cria_lista_aleatoria()

        print(self.tiles_lista)
 

    def draw_tiles(self):
        self.tiles = []
        for i in range(GAME_SIZE):
            self.tiles.append([])
            for j in range(GAME_SIZE):
                indice = i * GAME_SIZE + j
                if self.tiles_lista[indice] != 0:
                    self.tiles[i].append(Tile(self, j, i, str(self.tiles_lista[indice])))
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

        if(self.bCria_aleatorio and self.tempo_aleatorio<=100):
            self.cria_lista_aleatoria()
            self.draw_tiles()
            self.tempo_aleatorio +=1

        if(self.tiles_lista_completo == self.tiles_lista and self.tempo_aleatorio!=0):
            print("vc ganhou!")
        

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
                        indice = i * GAME_SIZE + j
                        if tile.click(mouseX, mouseY):
                            if (tile.checkDireita() and j < GAME_SIZE-1 and self.tiles_lista[indice+1] == 0):
                                self.tiles_lista[indice], self.tiles_lista[indice+1] = self.tiles_lista[indice+1], self.tiles_lista[indice] # faz a troca

                            if(tile.checkEsquerda() and j > 0 and self.tiles_lista[indice-1]==0):
                                self.tiles_lista[indice], self.tiles_lista[indice-1] = self.tiles_lista[indice-1], self.tiles_lista[indice] # faz a troca

                            if(tile.checkCima() and i > 0 and self.tiles_lista[indice-GAME_SIZE]==0):
                                self.tiles_lista[indice], self.tiles_lista[indice-GAME_SIZE] = self.tiles_lista[indice-GAME_SIZE], self.tiles_lista[indice] # faz a troca

                            if(tile.checkBaixo() and i < GAME_SIZE-1 and self.tiles_lista[indice+GAME_SIZE]==0):
                                self.tiles_lista[indice], self.tiles_lista[indice+GAME_SIZE] = self.tiles_lista[indice+GAME_SIZE], self.tiles_lista[indice] # faz a troca

                            self.draw_tiles()

                for botao in self.listaBotoes:
                    if(botao.click(mouseX,mouseY)):
                        if(botao.text == "Gerar Aleatório"):
                            self.tempo_aleatorio = 0
                            self.bCria_aleatorio = True

                        elif(botao.text=="Recomeçar"):
                            self.new()





game = Game()
while True:
    game.new()
    game.run()
