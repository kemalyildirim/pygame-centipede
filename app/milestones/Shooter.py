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
TITLE = "Shooter module"

UP = pygame.math.Vector2(0, -1)
DOWN = pygame.math.Vector2(0, 1)
LEFT = pygame.math.Vector2(-1, 0)
RIGHT = pygame.math.Vector2(1, 0)


class Shooter(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        pygame.key.set_repeat(1, 10) # for moving constantly.
        self.screen = screen
        self.image = pygame.image.load(ASSETS_PATH + "/app/assets/images/shooter/shooter.png")
        self.image = self.image.convert_alpha() # for png
        self.rect = self.image.get_rect()
        self.rect.centerx = 700 / 2 ## only for 800x600
        self.rect.centery = 580 ## only for 800x600
        self.dx = 10
        self.bullets = pygame.sprite.Group()
        self.max_bullets = 10
        self.snd_shoot = pygame.mixer.Sound(ASSETS_PATH + "/app/assets/sounds/shoot.ogg")
    
    def checkBoundaries(self):
        if self.rect.centerx > self.screen.get_width():
            self.rect.centerx = self.screen.get_width() # can't go to the other side.
        if self.rect.centerx < 0:
            self.rect.centerx = 0
        # Shooter is allowed to move on y axis a bit.
        if self.rect.centery < 400:
            self.rect.centery = 400 # can't go to the other side.
        if self.rect.centery >= 580:
            self.rect.centery = 580
    def move(self, direction):
        self.rect = self.rect.move(2*direction)
    
    def update(self):
        self.bullets.update()
    
    def draw(self):
        self.screen.blit(self.image, self.rect)
        self.bullets.draw(self.screen)

    def shoot(self):
        if len(self.bullets) < self.max_bullets:
            p = Projectile(self.screen, self.rect.center)
            self.bullets.add(p)
            return True
        else:
            return False

class Projectile(pygame.sprite.Sprite):
    def __init__(self, screen, pos):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load(ASSETS_PATH + "/app/assets/images/beam/beam.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0] - 3
        self.rect.centery = pos[1] - 20 
        self.dx = 8

    def checkIfBulletLeavesScreen(self):
        if self.rect.centery <= 0:
            return True
        else:
            return False

    def update(self):
        self.rect = self.rect.move(0, -self.dx)
        if self.checkIfBulletLeavesScreen():
            self.kill()
    def draw(self):
        self.screen.blit(self.image, self.rect)
        self.update()

if __name__ == "__main__":
    
    pygame.init()   # Init pygame
    pygame.mixer.init()
    ## Configure
    screen = pygame.display.set_mode((800,600)) # 800 x 600
    pygame.display.set_caption(TITLE) # Title
    bg = pygame.Surface(screen.get_size()) # Background object
    bg = bg.convert()
    bg.fill((174, 170, 179))

    # GAME LOOP
    clock = pygame.time.Clock()
    keep = True
    shooter = Shooter(screen)
    pygame.key.set_repeat(1, 10)
    
    while keep:
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
                        shooter.rect = shooter.rect.move((-shooter.dx, 0))
                    elif e.key == pygame.K_RIGHT:
                        shooter.rect = shooter.rect.move((shooter.dx, 0))
                    elif e.key == pygame.K_UP:
                        shooter.rect = shooter.rect.move((0, -shooter.dx))
                    elif e.key == pygame.K_DOWN:
                        shooter.rect = shooter.rect.move((0, +shooter.dx))
                    shooter.checkBoundaries()


        screen.blit(bg, (0, 0))
        shooter.update()
        shooter.draw()
        pygame.display.flip()
        clock.tick(30)