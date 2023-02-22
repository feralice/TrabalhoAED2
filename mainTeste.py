import pygame
import random
import time
from configuracoes import *
from sprite import *
from Soluciona import buscaInformada

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.tempo_aleatorio = 0
        self.cria_aleatorio = False
        self.comeca_jogo = False
        self.comeca_timer = 0
        self.tempo = 0
        self.ganhou = False
        self.semsolucao = False
        self.resolve_aut = False

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
        self.tempo = 0
        self.comeca_jogo = False
        self.comeca_timer = False
        self.listaBotoes = []
        self.listaBotoes.append(Botao(650, 100, 350, 50, "Gerar Aleatório", WHITE, BLACK))
        self.listaBotoes.append(Botao(650, 170, 350, 50, "Recomeçar", WHITE, BLACK))
        self.listaBotoes.append(Botao(650,240,350,50,"Começar jogo",WHITE,BLACK))
        self.listaBotoes.append(Botao(650,310,350,50,"Resolver automático",WHITE,BLACK))




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

        if(self.comeca_jogo ):

            if(self.tiles_lista == self.tiles_lista_completo):
                self.comeca_jogo = False
                self.ganhou = True
                
            if(self.comeca_timer):
                self.timer = time.time()
                self.comeca_timer = False

            self.tempo = time.time() - self.timer

        if(self.cria_aleatorio):
            self.cria_lista_aleatoria()
            self.draw_tiles()
            self.tempo_aleatorio +=1

            if(self.tempo_aleatorio > 50):
                self.cria_aleatorio = False
                
        if(self.resolve_aut):
            
            #print(self.caminho)
            #print(self.passos)
        
            if(self.caminho != -1 and self.contador != len(self.caminho)):
                    self.tiles_lista = self.caminho[self.contador]
                    self.draw_tiles()
                    self.contador += 1
            elif(self.caminho == -1 and self.passos == -1):
                    self.resolve_aut = False
                    self.semsolucao = True
                    print(self.caminho)
                    print(self.passos)
                
            else:
                self.resolve_aut = False
                
        

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

        ElemGraficos(780,35,"%.2f" % self.tempo).draw(self.screen)

        if(self.ganhou):
            ElemGraficos(200,500,"Parabéns!!! Você ganhou :D").draw(self.screen)

        pygame.display.flip()
        
        if(self.semsolucao):
            ElemGraficos(200,500,"Sem solução :(").draw(self.screen)

        pygame.display.flip()

    def events(self):

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit(0)

            if(event.type == pygame.MOUSEBUTTONDOWN and not self.resolve_aut):

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
                            self.cria_aleatorio = True

                        if(botao.text=="Recomeçar"):
                            self.new()

                        if(botao.text=="Começar jogo" and self.tiles_lista!=self.tiles_lista_completo):
                            self.comeca_jogo = True
                            self.comeca_timer =True

                        if(botao.text=="Resolver automático" and self.tiles_lista!=self.tiles_lista_completo):
                            self.resolve_aut = True 
                            self.contador = 0
                            self.caminho, self.passos = buscaInformada(self.tiles_lista)
                            self.comeca_timer = True
                            self.comeca_jogo = True
                            
                            



game = Game()
while True:
    game.new()
    game.run()
