#!/usr/bin/env python
# Improved Shooter module.

import pygame
import sys
import random
import os

__author__ = ["Kemal Yildirim", "Haktan Basak"]
__credits__ = ["Samsun Basarici", "Computer Games CSE420"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = ["Kemal Yildirim", "Haktan Basak"]
__email__ = "kemalyildirm@gmail.com"
__status__ = "Development"

ASSETS_PATH = os.getcwd()
TITLE = "Spider module"

class Spider(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load(ASSETS_PATH + "/app/assets/images/spider/spider.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.x_min = 0
        self.x_max = 800
        self.rect.centerx, self.rect.centery = self.setSpawnPoint()
        self.dx = 5
        self.dy = 5
        self.DIRS = {
            "N": pygame.math.Vector2(0, -1),
            "S": pygame.math.Vector2(0, 1),
            "W": pygame.math.Vector2(-1, 0),
            "E": pygame.math.Vector2(1, 0),
            "NW": pygame.math.Vector2(-1, -1),
            "NE": pygame.math.Vector2(1, -1),
            "SW": pygame.math.Vector2(-1, 1),
            "SE": pygame.math.Vector2(1, 1)
        }
        self.keys = self.setKeys()

    def setSpawnPoint(self):
        x = random.randint(0, 2)
        if x == 1: 
            r_x = self.x_min
        else:
            r_x = self.x_max
        return r_x, random.randint(400, 580)
    
    def setKeys(self):
        keys = self.DIRS.keys()
        return list(keys)
    
    def checkBoundaries(self):
        if self.rect.centerx >= self.x_max or self.rect.centerx <= self.x_min:
            self.kill()
        if self.rect.centery <= 400:
            self.rect.centery = 400
        if self.rect.centery >= 600:
            self.rect.centery = 600
    
    def get_direction(self):
        if not self.rect.centerx >= 900:
            di = ["NW", "SW", "W"]
            d = random.randint(0, len(di) - 1)
            id = di[d]
            direction = self.DIRS[id]
            return direction
        else:
            di = ["NE", "SE", "E"]
            d = random.randint(0, len(di) - 1)
            id = di[d]
            direction = self.DIRS[id]
            return direction
    def update(self):
        #print(self.rect.center)
        d = self.get_direction()
        self.rect = self.rect.move(d*self.dx)
        self.checkBoundaries()
    def draw(self):
        self.screen.blit(self.image, self.rect)



if __name__ == "__main__":
    
    pygame.init()   # Init pygame
    pygame.mixer.init()
    ## Configure
    screen = pygame.display.set_mode((800,600)) # 800 x 600
    pygame.display.set_caption(TITLE) # Title
    bg = pygame.Surface(screen.get_size()) # Background object
    bg = bg.convert()
    bg.fill((174, 170, 179))
    spider = Spider(screen)
    spiderGroup = pygame.sprite.Group(spider)
    # GAME LOOP
    clock = pygame.time.Clock()
    keep = True
    while keep:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                keep = False
            elif e.type == pygame.MOUSEBUTTONUP:
                print(pygame.mouse.get_pos()) # Debug purposes
        screen.blit(bg, (0, 0))
        spiderGroup.update()
        spiderGroup.draw(screen)
        pygame.display.flip()
        clock.tick(30)