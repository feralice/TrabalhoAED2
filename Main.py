import pygame
import random
import time
from Configuracoes import *
from Sprites import *
from Soluciona import buscaInformada

"""
código main que roda o jogo
"""

class Jogo:

    #construtor do jogo
    def __init__(self):
        #inicia o pygame
        pygame.init()

        #cria a tela
        self.screen = pygame.display.set_mode((LARGURA, ALTURA))

        #coloca o título
        pygame.display.set_caption(TITULO)

        #para utilizamos o timer
        self.clock = pygame.time.Clock()

        #tempo para gerar um puzzle aleatório
        self.tempo_aleatorio = 0

        #variável para saber se precisamos criar um estado aleatório
        self.cria_aleatorio = False

        #variável para controlar o inicio do jogo
        self.comeca_jogo = False

        #variáveis para controlar o contador
        self.comeca_timer = 0
        self.tempo = 0

        #variável para verificar se player ganhou
        self.ganhou = False

        #variável para verificar se puzzle tem solução
        self.sem_solucao = False

        #variável para controlar o resolvimento automatico
        self.resolve_aut = False

        #variaveis para controlar o tempo de frases na tela
        self.clock = pygame.time.Clock()
        self.tempo_tela = None

    #função para criar o jogo com o estado final que desejamos
    def cria_jogo(self):
        estado_final = [0,1,2,3,4,5,6,7,8]
        return estado_final
     
    #verifica se o puzzle é solucionável a partir das inversões
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

            #se o número de inversões for ímpar, não é solucionável
            if(numInversoes)%2==1:
                return False

            #se o número de inversões for par, é solucionável
            else: 
                return True

    #função que cria a lista aleatória para usarmos no puzzle
    def cria_lista_aleatoria(self):

        puzzle = self.quadrados_lista.copy()
        random.shuffle(puzzle)

        #chama a função para ver se a lista criada é solucionável
        if(self.eh_solucionavel(puzzle)):
            self.quadrados_lista = puzzle
        #se não for solucionável, chamamos cria_lista_aleatoria() 
        #recursivamente até criar uma lista solucionável
        else:
           return self.cria_lista_aleatoria()

    #desenha os quadradinhos do jogo juntamente com seus números e deixa o que possui o 0 vazio
    def draw_quadrados(self):
        self.quadrados = []
        for i in range(TAM_JOGO):
            self.quadrados.append([])
            for j in range(TAM_JOGO):
                indice = i * TAM_JOGO + j
                if self.quadrados_lista[indice] != 0:
                    self.quadrados[i].append(Quadrado(self, j, i, str(self.quadrados_lista[indice])))
                else:
                    self.quadrados[i].append(Quadrado(self, j, i, "vazio"))

    #cria um novo jogo    
    def novo(self):

        self.sprites = pygame.sprite.Group()

        #recebe a lista
        self.quadrados_lista = self.cria_jogo()

        #guarda a lista como o gabarito ou estado final
        self.gabarito = self.cria_jogo()

        #inicializa as variaveis
        self.tempo = 0
        self.comeca_jogo = False
        self.comeca_timer = False

        #cria uma lista para guardar todos os botões que iremos utilizar
        self.listaBotoes = []
        #cria os botoões e adiciona eles na lista
        self.listaBotoes.append(Botao(650, 120, 380, 55, "Gerar Aleatório", LILAS, PRETO))
        self.listaBotoes.append(Botao(650,200,380,55,"Começar jogo",LILAS,PRETO))
        self.listaBotoes.append(Botao(650,280,380,55,"Resolver automático",LILAS,PRETO))
        self.listaBotoes.append(Botao(650, 360, 380, 55, "Recomeçar", LILAS, PRETO))

        #começa um jogo novo e mostra o estado final ao inicializar 
        #o jogo é desenhado na tela
        self.draw_quadrados()
        

    #função que roda enquanto o jogador está jogando
    def run(self):

        self.jogando = True

        #chama as funções necessárias para o funcionamento do jogo
        while(self.jogando):
            self.clock.tick(FPS)
            self.eventos()
            self.update()
            self.draw()
    
    #Faz o update dos dados
    def update(self):

        if(self.comeca_jogo):

            #verifica se o jogador ganhou
            if(self.quadrados_lista == self.gabarito):
                self.comeca_jogo = False
                self.ganhou = True
            
            #começa o timer
            if(self.comeca_timer):
                self.timer = time.time()
                self.comeca_timer = False

            self.tempo = time.time() - self.timer

        #começa a criar o puzzle aleatório
        if(self.cria_aleatorio):
            self.cria_lista_aleatoria()
            self.draw_quadrados()
            self.tempo_aleatorio +=1

            #puzzles serão criados para dar efeito de "carregando" e irá parar quando o tempo for >50
            if(self.tempo_aleatorio > 50):
                self.cria_aleatorio = False
                
        #resolve o puzzle automaticamente utilizando o módulo Soluciona
        if(self.resolve_aut):
            
            #mostra os caminhos e passos no prompt
            print(self.caminho)
            print(self.passos)
        
            if(self.caminho != -1 and self.contador != len(self.caminho)):
                    
                    self.quadrados_lista = self.caminho[self.contador]
                    self.draw_quadrados()
                    pygame.time.delay(800)
                    self.contador += 1
            elif(self.caminho == -1 and self.passos == -1):
                    self.resolve_aut = False
                    self.sem_solucao = True
                    print(self.caminho)
                    print(self.passos)
                
            else:
                self.resolve_aut = False
        
        #chama novamente a função para sempre atualizar o jogo
        self.sprites.update()
        
        
    #função que desenha a grade do jogo
    def draw_grade(self):
        for i in range(-1,TAM_JOGO*TAM_QUADRADO, TAM_QUADRADO):
            pygame.draw.line(self.screen, CINZA_CLARO,(i,0),(i, TAM_JOGO*TAM_QUADRADO))

        for j in range(-1,TAM_JOGO*TAM_QUADRADO, TAM_QUADRADO):
            pygame.draw.line(self.screen,CINZA_CLARO,(0,j),(TAM_JOGO*TAM_QUADRADO,j))


    #função que coloca os elementos na tela, "desenha" na tela
    def draw(self):

        self.screen.fill(CINZA)
        self.sprites.draw(self.screen)
        self.draw_grade()

        #cria os botoes do jogo que estao na lista de botoes que criamos
        for botao in self.listaBotoes:
           botao.draw(self.screen)

        #cria um timer
        ElemGraficos(780,35,"%.2f" % self.tempo).draw(self.screen)
        
        #coloca o elemento na tela caso o player ganhe!
        if(self.ganhou):

            if self.tempo_tela is None:
                # se é a primeira vez que ganhou, salva o tempo atual
                self.tempo_tela = pygame.time.get_ticks()
            
            #coloca frase de que ganhou na tela
            ElemGraficos(200,550,"Parabéns!!! Você ganhou :D").draw(self.screen)

            #deixa a frase na tela por 3 segundos
            if pygame.time.get_ticks() - self.tempo_tela >= 3000:
                # remove a mensagem após 3 segundos
                self.ganhou = False
                self.tempo_tela = None
            
        #coloca sem solução na tela, caso o puzzle não tenha solução usando a mesma lógica acima
        if(self.sem_solucao):

            if self.tempo_tela is None:
                self.tempo_tela = pygame.time.get_ticks()

            ElemGraficos(200,550,"Sem solução :(").draw(self.screen)

            if pygame.time.get_ticks() - self.tempo_tela >= 3000:
                # remove a mensagem após 3 segundos
                self.sem_solucao = False
                self.tempo_tela = None
            

        pygame.display.flip()


    #função para utilizarmos o pygame.event.get() e obter todos os eventos que ocorrem no game
    def eventos(self):

        for event in pygame.event.get():

            #sai do jogo
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit(0)

            if(event.type == pygame.MOUSEBUTTONDOWN and not self.resolve_aut):

                mouseX, mouseY = pygame.mouse.get_pos()

                #para realizar a resolução manual
                #faz as trocas dependendo de onde o player clicou
                for i, quadrados in enumerate(self.quadrados):
                    for j, tile in enumerate(quadrados):
                        indice = i * TAM_JOGO + j
                        if tile.click(mouseX, mouseY):

                            #realiza a troca com o elemento da direita, se estiver vazio
                            if (tile.checkDireita() and j < TAM_JOGO-1 and self.quadrados_lista[indice+1] == 0):
                                self.quadrados_lista[indice], self.quadrados_lista[indice+1] = self.quadrados_lista[indice+1], self.quadrados_lista[indice] # faz a troca

                            #realiza a troca com o elemento da esquerda, se estiver vazio
                            if(tile.checkEsquerda() and j > 0 and self.quadrados_lista[indice-1]==0):
                                self.quadrados_lista[indice], self.quadrados_lista[indice-1] = self.quadrados_lista[indice-1], self.quadrados_lista[indice] # faz a troca

                            #realiza a troca com o elemento acima, se estiver vazio
                            if(tile.checkCima() and i > 0 and self.quadrados_lista[indice-TAM_JOGO]==0):
                                self.quadrados_lista[indice], self.quadrados_lista[indice-TAM_JOGO] = self.quadrados_lista[indice-TAM_JOGO], self.quadrados_lista[indice] # faz a troca

                            #realiza a troca com o elemento abaixo, se estiver vazio
                            if(tile.checkBaixo() and i < TAM_JOGO-1 and self.quadrados_lista[indice+TAM_JOGO]==0):
                                self.quadrados_lista[indice], self.quadrados_lista[indice+TAM_JOGO] = self.quadrados_lista[indice+TAM_JOGO], self.quadrados_lista[indice] # faz a troca

                            self.draw_quadrados()

                #para ver qual botão o player clicou
                for botao in self.listaBotoes:
                    if(botao.click(mouseX,mouseY)):

                        #verifica qual botão foi clicado e seta as variáveis necessárias
                        if(botao.texto == "Gerar Aleatório"):
                            self.novo()
                            self.tempo_aleatorio = 0
                            self.cria_aleatorio = True

                        if(botao.texto=="Recomeçar"):
                            self.novo()

                        if(botao.texto=="Começar jogo" and self.quadrados_lista!=self.gabarito):
                            self.comeca_jogo = True
                            self.comeca_timer =True

                        if(botao.texto=="Resolver automático" and self.quadrados_lista!=self.gabarito):
                            self.resolve_aut = True 
                            self.contador = 0
                            self.caminho, self.passos = buscaInformada(self.quadrados_lista)
                            self.comeca_timer = True
                            self.comeca_jogo = True

#inicializa o jogo                           
game = Jogo()
while True:
    game.novo()
    game.run()