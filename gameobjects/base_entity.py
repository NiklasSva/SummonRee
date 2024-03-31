# SummonRee - base_entity.py

import pygame
import uuid

def __init__(self):
    self.position = pygame.Vector2(0, 0)
    self.ID = uuid.uuid4()
    self.name = "UnknownEntity" + str(self.ID)
