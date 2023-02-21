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
        grid = [[x + y * GAME_SIZE for x in range(1, GAME_SIZE + 1)] for y in range(GAME_SIZE)]
        grid[-1][-1] = 0
        return grid

    def draw_tiles(self):
        self.tiles = []
        for row, x in enumerate(self.tiles_lista):
            self.tiles.append([])
            for col, tile in enumerate(x):
                if tile != 0:
                    self.tiles[row].append(Tile(self, col, row, str(tile)))
                else:
                    self.tiles[row].append(Tile(self, col, row, "empty"))
        
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.tiles_lista = self.create_game()
        self.tiles_lista_completo = self.create_game()


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
        for row in range(-1,GAME_SIZE*TILESIZE, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY,(row,0),(row, GAME_SIZE*TILESIZE))
        for col in range(-1,GAME_SIZE*TILESIZE, TILESIZE):
            pygame.draw.line(self.screen,LIGHTGREY,(0,col),(GAME_SIZE*TILESIZE,col))


    def draw(self):
        self.screen.fill(BGCOLOUR)
        self.all_sprites.draw(self.screen)
        self.draw_grid()
        self.draw_tiles()
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

    

game = Game()
while True:
    game.new()
    game.run()
