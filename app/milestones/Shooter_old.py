#!/usr/bin/env python
# Shooter milestone of the game.
# TO DO: Wrong initation, not using the superclass.
import pygame
import sys
import math
import random
import os


ASSETS_PATH = os.getcwd()
TITLE = "Shooter module"

# https://www.pygame.org/docs/ref/sprite.html
# chapter 06 - basicSprite.py

## Moving sprite:
## https://stackoverflow.com/a/16186396

class Shooter(pygame.sprite.Sprite):
    def __init__(self, screen, bg):
        super().__init__()
        self.screen = screen
        self.bg = bg
        self.bullets = []
        self.image = pygame.image.load(ASSETS_PATH + "/app/assets/images/shooter/shooter.png")
        self.image = self.image.convert_alpha() # for png
        self.rect = self.image.get_rect()
        self.rect.centerx = 700 / 2 ## only for 800x600
        self.rect.centery = 580 ## only for 800x600
        self.dx = 10
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init()
            self.snd_shoot = pygame.mixer.Sound(ASSETS_PATH + "/app/assets/sounds/shoot.ogg")
    
    def shoot(self):
        pos = [self.rect.centerx - 8, self.rect.centery - 25]
        b = Projectile(pos)
        self.bullets.append(b)
    def checkBoundaries(self):
        if self.rect.centerx > self.screen.get_width():
            self.rect.centerx = self.screen.get_width() # can't go to the other side.
        if self.rect.centerx < 0:
            self.rect.centerx = 0
        # no need for y axis.
    def handle_keys(self):
        key = pygame.key.get_pressed() # tuple => print(type(key))
        if key[pygame.K_LEFT]:
            self.rect.centerx -= self.dx
            self.checkBoundaries()
        elif key[pygame.K_RIGHT]:
            self.rect.centerx += self.dx
            self.checkBoundaries()
        elif key[pygame.K_SPACE]:
            self.shoot()
            self.snd_shoot.play()
        elif key[pygame.K_LEFT] and key[pygame.K_SPACE]:
            print("asd")
            self.rect.centerx += self.dx
            self.checkBoundaries()
            self.shoot()
            self.snd_shoot.play()
        elif key[pygame.K_RIGHT] and key[pygame.K_SPACE]:
            print(2)
            self.rect.centerx -= self.dx
            self.checkBoundaries()
            self.shoot()
            self.snd_shoot.play()
        else:
            None
    def draw(self, screen):
        self.screen.blit(self.image, self.rect)
        for b in self.bullets:
            b.move(self.screen)
            if b.pos[1] == 0:
                self.bullets.remove(b)

# How to shoot, class implementation.
# https://stackoverflow.com/a/52011537

class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(ASSETS_PATH + "/app/assets/images/beam/beam.png")
        self.image = self.image.convert_alpha() # for png
        self.pos = pos
        self.dy = -5
    def move(self, screen):
        print(self.pos)
        self.pos[1] += self.dy # y pos.
        self.draw(screen)
        self.kill()
    def draw(self, screen):
        screen.blit(self.image, self.pos)
    
if __name__ == "__main__":
    
    pygame.init()   # Init pygame
    ## Configure
    screen = pygame.display.set_mode((800,600)) # 800 x 600
    pygame.display.set_caption(TITLE) # Title
    bg = pygame.Surface(screen.get_size()) # Background object
    bg = bg.convert()
    bg.fill((174, 170, 179))

    # GAME LOOP
    clock = pygame.time.Clock()
    keep = True
    p = Shooter(screen, bg)

    #font = pygame.font.SysFont(None, 45) => ADDED TO CLASS
    #label = font.render("P", 1, (250, 250, 250)) => ADDED TO CLASS

    while keep:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                keep = False
            elif e.type == pygame.MOUSEBUTTONUP:
                print(pygame.mouse.get_pos()) # To decide proper position of player when game starts,
                              # somewhere middle bottom.

        p.handle_keys()
        screen.blit(bg, (0, 0))
        p.draw(screen)
        
        #screen.blit(label, p.rect) => ADDED TO CLASS
        pygame.display.flip()
        # tick
        clock.tick(30)