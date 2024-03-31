# SummonRee - player_character.py

import base_entity
import pygame
class PlayerCharacter(base_entity.BaseEntity):
    def __init__(self, name:str , position2D:pygame.Vector2, speed:float = 100.0):
        super().__init__()
        self.name = name             
        if position2D: self.position = position2D
        self.speed = speed
        