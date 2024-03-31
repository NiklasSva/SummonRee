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

    global current_phase
    global last_phase
    if current_phase != last_phase:
        print (f"Phase changed from {last_phase} to {current_phase}") # add logic for when phase changes
        last_phase = current_phase
    
    match current_phase:
        case GamePhase.Exploring: Exploring()
        case GamePhase.Combat: Combat()
        case GamePhase.GameOver: GameOver()
        case _:
            print (f"Invalid phase {current_phase}")
            current_phase = GamePhase.Exploring  

    return True

def Exploring():
    # check for enemies, if not empty switch to combat, else pop from level_pods
    # if level_pods is empty switch to game over (Victory)
    pass

def Combat():
    # if player dies switch to game over (Defeat)
    # if player kills all enemies switch to exploring
    pass

def GameOver():
    # take argument to determine win or lose
    # end game on player confirmation (input)
    # highscore?
    pass

