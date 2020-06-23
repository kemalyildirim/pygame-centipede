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
    while keep:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                keep = False
            elif e.type == pygame.MOUSEBUTTONUP:
                print(pygame.mouse.get_pos()) # Debug purposes
        screen.blit(bg, (0, 0))
        pygame.display.flip()
        clock.tick(30)