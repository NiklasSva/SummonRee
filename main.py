# SummonRee - main.py

import pygame
from pygame.time import Clock

from game_logic import Run

pygame.init()
clock = Clock()

# create window
window = pygame.display.set_mode((640, 480))


while Run():
    # make basic window
    window.fill((100, 100, 100))    
    # draw
    pygame.display.update()
    
    clock.tick(60)

pygame.quit()
