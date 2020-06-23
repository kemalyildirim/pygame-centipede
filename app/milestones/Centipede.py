#!/usr/bin/env python
# Improved Shooter module.
import pygame
import sys
import os

__author__ = ["Kemal Yildirim", "Haktan Basak"]
__credits__ = ["Samsun Basarici", "Computer Games CSE420"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = ["Kemal Yildirim", "Haktan Basak"]
__email__ = "kemalyildirm@gmail.com"
__status__ = "Development"

ASSETS_PATH = os.getcwd()
TITLE = "Centipede module"

class Centipede(pygame.sprite.Sprite):
    def __init__(self, screen, pos, dx):
        super().__init__()
        self.screen = screen
        self.pos = pos
        self.image = pygame.image.load(ASSETS_PATH + "/app/assets/images/centipede/centipede.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dx = dx
        #self.dy = 0
    def move(self):
        self.rect = self.rect.move(self.dx, 0)
    def update(self):
        self.move()
        self.checkBounds()
    def draw(self):
        self.screen.blit(self.image, self.rect)    
    def checkBounds(self):
        if self.rect.right >= self.screen.get_width():
            self.dx *= -1
            self.rect.y += 20
        if self.rect.left <= 0:
            self.dx *= -1
            self.rect.y += 20
        if self.rect.bottom >= self.screen.get_height():
            self.dx = 0

if __name__ == "__main__":
    
    pygame.init()   # Init pygame
    pygame.mixer.init()
    ## Configure
    screen = pygame.display.set_mode((800,600)) # 800 x 600
    pygame.display.set_caption(TITLE) # Title
    bg = pygame.Surface(screen.get_size()) # Background object
    bg = bg.convert()
    bg.fill((174, 170, 179))
    cen = Centipede(screen, (300, 300), 5)
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
        cen.update()
        cen.draw()
        pygame.display.flip()
        clock.tick(30)