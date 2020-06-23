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

def drawLine(background, color, start, end):
    pygame.draw.line(background, color, start, end)

def drawRect(background, color, start, end, thick):
    pygame.draw.rect(background, color, start, end, thick)

def drawCircle(background, color, center, radius):
    pygame.draw.circle(background, color, center, radius)
# drawEllipse
# drawArc
# drawLines
# drawPolygon
# pygame.draw.aaline() => anti-aliased line. (smoother line.)
def randint():
    return int(random.random() * 600)
if __name__ == "__main__":
    pygame.init()   # Init pygame
    ## Configure
    screen = pygame.display.set_mode((800,600)) # 800 x 600
    pygame.display.set_caption("Draw random lines") # Title
    bg = pygame.Surface(screen.get_size()) # Background object
    bg = bg.convert()
    bg.fill((174, 170, 179))

    # GAME LOOP
    clock = pygame.time.Clock()
    keep = True
    while keep:
        clock.tick(30)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                keep = False
        screen.blit(bg, (0, 0))
        pygame.display.flip()
        pygame.draw.line(bg, (0x33, 0xFF,0x33), (randint(), randint()), (randint(), randint()), 10)