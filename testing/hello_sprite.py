#!/usr/bin/env python
import pygame
import sys
import math
import random
__author__ = ["Kemal Yildirim", "Haktan Basak"]
__credits__ = ["Samsun Basarici", "Computer Games CSE420"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = ["Kemal Yildirim", "Haktan Basak"]
__email__ = "kemalyildirm@gmail.com"
__status__ = "Development"

# https://www.pygame.org/docs/ref/sprite.html
# chapter 06 - basicSprite.py

## Moving sprite:
## https://stackoverflow.com/a/16186396
class Player(pygame.sprite.Sprite):
    def __init__(self):
        # pygame.sprite.Sprite.__init__(self)
        # super() method for inherited class, pygame.sprite.Sprite
        super().__init__()
        self.image = pygame.Surface((25, 25))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 400
        self.dx = 10
        self.dx_max = 20 # TO DO: for centipede
        # label
        self.font = pygame.font.SysFont(None, 45)
        self.label = self.font.render("P", 1, (250, 250, 250))
    def handle_keys(self):
        key = pygame.key.get_pressed() # tuple => print(type(key))
        if key[pygame.K_LEFT]:
            print("handled")
            self.rect.centerx -= self.dx
        elif key[pygame.K_RIGHT]:
            print("handled")
            self.rect.centerx += self.dx
        else:
            None
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.label, self.rect)
if __name__ == "__main__":
    pygame.init()   # Init pygame
    ## Configure
    screen = pygame.display.set_mode((800,600)) # 800 x 600
    pygame.display.set_caption("Moving sprites") # Title
    bg = pygame.Surface(screen.get_size()) # Background object
    bg = bg.convert()
    bg.fill((174, 170, 179))

    # GAME LOOP
    clock = pygame.time.Clock()
    keep = True
    p = Player()

    #font = pygame.font.SysFont(None, 45) => ADDED TO CLASS
    #label = font.render("P", 1, (250, 250, 250)) => ADDED TO CLASS

    while keep:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                keep = False
            elif e.type == pygame.MOUSEBUTTONUP:
                print(p.rect) # To decide proper position of player when game starts,
                              # somewhere middle bottom.
        p.handle_keys()
        screen.blit(bg, (0, 0))
        p.draw(screen)
        #screen.blit(label, p.rect) => ADDED TO CLASS
        pygame.display.flip()

        # tick
        clock.tick(30)