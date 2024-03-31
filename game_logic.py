# SummonRee - game_logic.py
import pygame

def Run():
    for each in pygame.event.get():
        if each.type == pygame.QUIT:
            return False
        
    

    return True