#!/usr/bin/env python
# initial random mushroom spawn, and Mushroom object.
# Shooting test.
import pygame
import sys
import os
import random
from Shooter import Shooter

ASSETS_PATH = os.getcwd()
TITLE = "Mushroom module"
        

class GameMap:
    def __init__(self, screen):
        self.screen = screen
        self.mushrooms = pygame.sprite.Group()
        self.generate_random_coordinates()
        self.create_map()
    def generate_random_coordinates(self, MAX_MUSHROOM = 60, squares = 20):
        xy_set = set() # so they're unique.
        while len(xy_set) < MAX_MUSHROOM:
            r_cor = (random.randint(0, squares), (random.randint(0, squares-3)))
            xy_set.add(r_cor)
        self.cords = xy_set
    def create_map(self):
        w = self.screen.get_width() / 20
        h = self.screen.get_height() / 20
        for i in self.cords:
            m = Mushroom(self.screen,(w * i[0], h * i[1]))
            self.mushrooms.add(m)
    # w and h placing points mapped to actual width and height.


class Mushroom(pygame.sprite.Sprite):
    def __init__(self, screen, pos):
        super().__init__()
        self.screen = screen
        self.ACTIVE = True
        self.pos = pos
        self.cur_state = 0
        self.image = [
            pygame.image.load(ASSETS_PATH + "/app/assets/images/mushroom/mushroom_full.png"),
            pygame.image.load(ASSETS_PATH + "/app/assets/images/mushroom/mushroom_oneb.png"),
            pygame.image.load(ASSETS_PATH + "/app/assets/images/mushroom/mushroom_twob.png"),
            pygame.image.load(ASSETS_PATH + "/app/assets/images/mushroom/mushroom_threeb.png")
            ]
        self.rect = self.image[self.cur_state].get_rect()
        self.rect.centerx = pos[0] + 5
        self.rect.centery = pos[1] + 5
        self.snd_destroyed = pygame.mixer.Sound(ASSETS_PATH + "/app/assets/sounds/mushroom_destroyed.wav")
        for i in self.image:
            i.convert_alpha()
    def inc_state(self):
            self.cur_state += 1
    def update(self):
            if self.cur_state <= 3:
                None
            else:
                self.ACTIVE = False
                self.snd_destroyed.play(maxtime=1000)
                pygame.mixer.fadeout(500)
                self.kill()
    def draw(self):
        if self.ACTIVE:
            self.screen.blit(self.image[self.cur_state], self.pos)
                    

if __name__ == "__main__":
    pygame.init()   # Init pygame
    pygame.mixer.init()
    ## Configure
    screen = pygame.display.set_mode((800,600)) # 800 x 600
    pygame.display.set_caption(TITLE) # Title
    bg = pygame.Surface(screen.get_size()) # Background object
    bg = bg.convert()
    bg.fill((174, 170, 179))

    game_map = GameMap(screen)
    s = Shooter(screen)
    clock = pygame.time.Clock()
    keep = True
    while keep:
        oldpos = pygame.math.Vector2(s.rect.x, s.rect.y)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                keep = False
            elif e.type == pygame.MOUSEBUTTONUP:
                print(pygame.mouse.get_pos()) # Debug purposes
            else:
                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_SPACE:
                        if shooter.shoot():
                            shooter.snd_shoot.play(maxtime=1000) 
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
            
        for mushroom in game_map.mushrooms:
            mushroom.update()
            mushroom.draw()
        
        s.update()
        s.draw()
        pygame.display.flip()
        clock.tick(30)