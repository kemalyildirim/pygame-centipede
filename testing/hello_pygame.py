#!/usr/bin/env python
# Main file for the CSE420 Computer Games project, Centipede game.
import pygame
import sys

__author__ = ["Kemal Yildirim", "Haktan Basak"]
__credits__ = ["Samsun Basarici", "Computer Games CSE420"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = ["Kemal Yildirim", "Haktan Basak"]
__email__ = "kemalyildirm@gmail.com"
__status__ = "Development"

if __name__ == "__main__":
    pygame.init()   # Init pygame
    ## Configure
    screen = pygame.display.set_mode((800,600)) # 800 x 600
    pygame.display.set_caption("Centipede") # Title
    bg = pygame.Surface(screen.get_size()) # Background object
    bg = bg.convert()
    bg.fill((174, 170, 179))

    ### Moving box
    box = pygame.Surface((25,25))
    box.fill((98, 20, 196))
    box.convert()
    box_x = 0
    box_y = 200


    # GAME LOOP
    clock = pygame.time.Clock()
    keep = True

    while keep:
        clock.tick(30)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                keep = False
        box_x += 20
        if box_x > screen.get_width():
            box_x = 0
        screen.blit(bg, (0, 0))
        screen.blit(box, (box_x, box_y)) # Move box to box_x and box_y
        pygame.display.flip()