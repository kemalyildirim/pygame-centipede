#!/usr/bin/env python
# initial random mushroom spawn, and Mushroom object.
# Shooting test.
import pygame
import sys
import os
import random
from Shooter import Shooter
from Mushroom import Mushroom
from Centipede import Centipede
from Spider import Spider
ASSETS_PATH = os.getcwd()


TITLE = "Centipede"

class Scoreboard:
    def __init__(self, score):
        self.score = score

    def inc_score(self, amount):
        self.score += amount
        

class GameMap:
    def __init__(self, screen, cen_speed, score, levels):
        self.screen = screen
        self.w = self.screen.get_width() // 20
        self.h = self.screen.get_height() // 20
        self.cen_speed = cen_speed
        self.mushrooms = pygame.sprite.Group()
        self.centipede_train = pygame.sprite.Group()
        self.generate_random_coordinates()
        self.create_map()
        self.create_centipedes()
        self.scoreboard = Scoreboard(score)
        self.levels = levels

    def create_centipedes(self, N = 15):
        ini_pos = [0, 0]
        for i in range(N):
            cen = Centipede(self.screen, (ini_pos[0], ini_pos[1]), self.cen_speed)
            self.centipede_train.add(cen)
            ini_pos[0] += 20

    def generate_random_coordinates(self, MAX_MUSHROOM = 30 , squares = 20):
        xy_set = set() # so they're unique.
        while len(xy_set) < MAX_MUSHROOM:
            r_cor = (random.randint(0, squares), (random.randint(1, squares-3)))
            xy_set.add(r_cor)
        self.cords = xy_set
    def create_map(self):
        for i in self.cords:
            m = Mushroom(self.screen, (self.w * i[0], self.h * i[1]))
            self.mushrooms.add(m)
    # w and h are tiles.
    def inc_level_reset(self):
        self = self.__init__(self.screen, (self.cen_speed*2), self.scoreboard.score, self.levels+1)

if __name__ == "__main__":
    pygame.init()   # Init pygame
    pygame.mixer.init()
    pygame.font.init()
    ## Configure
    screen = pygame.display.set_mode((800,600)) # 800 x 600
    pygame.display.set_caption(TITLE) # Title
    bg = pygame.Surface(screen.get_size()) # Background object
    bg = bg.convert()
    bg.fill((174, 170, 179))

    game_map = GameMap(screen, cen_speed=2, score=0, levels=0)
    s = Shooter(screen)
    spider = Spider(screen)
    allSprites = pygame.sprite.Group(s, game_map.mushrooms, game_map.centipede_train)
    spider_g = pygame.sprite.Group(spider)
    clock = pygame.time.Clock()
    
    instruction = True
    while instruction:
        screen.blit(bg, (0,0))
        font = pygame.font.SysFont("Comic Sans MS", 20)
        text = "Centipede game. Move with arrow keys, shoot with spacebar. Press enter to start."
        rendered = font.render(text, 20, (0, 0, 0))
        screen.blit(rendered, (20,300))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                instruction = False
                sys.exit()
            if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                        instruction = False
        pygame.display.flip()
        clock.tick(30)
        
    keep = True
    while keep:
        if game_map.levels >= 3:
            keep = False
        oldpos = pygame.math.Vector2(s.rect.x, s.rect.y)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                keep = False
                sys.exit()
            elif e.type == pygame.MOUSEBUTTONUP:
                print(pygame.mouse.get_pos()) # Debug purposes
            else:
                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_SPACE:
                        if s.shoot():
                            s.snd_shoot.play(maxtime=1000) 
                            pygame.mixer.fadeout(500)
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_LEFT:
                        s.rect = s.rect.move((-s.dx, 0))
                    elif e.key == pygame.K_RIGHT:
                        s.rect = s.rect.move((s.dx, 0))
                    elif e.key == pygame.K_UP:
                        s.rect = s.rect.move((0, -s.dx))
                    elif e.key == pygame.K_DOWN:
                        s.rect = s.rect.move((0, +s.dx))
                    s.checkBoundaries()
        
        screen.blit(bg, (0, 0))
        if pygame.sprite.spritecollideany(s, game_map.mushrooms, False):
            print("OLD   :", oldpos)
            curpos = pygame.math.Vector2(s.rect.x, s.rect.y)
            print("CUR   :", curpos )
            s.move(curpos - oldpos)
        for mushroom in game_map.mushrooms:
            m_hit = pygame.sprite.spritecollideany(mushroom, s.bullets, False)
            if m_hit:
                m_hit.kill()
                mushroom.inc_state()
                game_map.scoreboard.inc_score(25)
            mushroom.update()
            mushroom.draw()

        for cen in game_map.centipede_train:
            cen.update()
            cen.draw()
            c_hit = pygame.sprite.spritecollideany(cen, s.bullets, False)
            if c_hit:
                game_map.scoreboard.inc_score(200)
                c_hit.kill()
                cen.kill()
        
        for sp in spider_g:
            sp_hit = pygame.sprite.spritecollideany(sp, s.bullets, False)
            if sp_hit:
                game_map.scoreboard.inc_score(500)
                sp_hit.kill()
                sp.kill()
        if not spider.alive():
            spider = Spider(screen)
            spider_g.add(spider)
        
        if len(game_map.centipede_train) == 0:
            game_map.inc_level_reset()
        
        spider_g.update()
        spider_g.draw(screen)
        s.update()
        s.draw()
        pygame.display.flip()
        clock.tick(30)
    if not keep:
        screen.fill((255,255,255))
        end = True
        while end:
            screen.blit(bg, (0, 0))
            font = pygame.font.SysFont("Comic Sans MS", 20)
            text = "Game over. Score: %d Press q to quit or close the window." % (game_map.scoreboard.score)
            rendered = font.render(text, 40, (0, 0, 0))
            screen.blit(rendered, (100,100))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    end = False
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_q:
                        end = False
                        sys.exit()
            
            pygame.display.flip()
            clock.tick(30)
            