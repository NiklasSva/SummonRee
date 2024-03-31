# SummonRee - game_logic.py
import pygame
from enum import Enum

class GamePhase(Enum):
    Exploring   = 0
    Combat      = 1
    GameOver    = 2

class EnemyType(Enum):
    OrenianSwordsmen = 1
    OrenianHammerman = 2

last_phase = GamePhase.Exploring
current_phase = GamePhase.Exploring
enemies_present = {}
level_pods = {
    EnemyType.OrenianHammerman, # Boss
    EnemyType.OrenianSwordsmen, # 10
    EnemyType.OrenianSwordsmen, # 9
    EnemyType.OrenianSwordsmen, # 8
    EnemyType.OrenianSwordsmen, # 7
    EnemyType.OrenianSwordsmen, # 6
    EnemyType.OrenianSwordsmen, # 5
    EnemyType.OrenianSwordsmen, # 4
    EnemyType.OrenianSwordsmen, # 3
    EnemyType.OrenianSwordsmen, # 2
    EnemyType.OrenianSwordsmen # 1
} # NOTE: reverse order because pop() removes from end

def Run():
    for each in pygame.event.get():
        if each.type == pygame.QUIT:
            return False
        
    

    return True