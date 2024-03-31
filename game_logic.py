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

    global last_phase
    global current_phase   
    global level_pods
    global enemies_present

    if current_phase != last_phase:
        print (f"Phase changed from {last_phase} to {current_phase}") # add logic for when phase changes
        last_phase = current_phase
    
    match current_phase:
        case GamePhase.Exploring: Exploring(current_phase, level_pods, enemies_present)
        case GamePhase.Combat: Combat(current_phase, level_pods, enemies_present)
        case GamePhase.GameOver:
            GameOver(level_pods, enemies_present)
            return False
        case _:
            print (f"Invalid phase {current_phase}")
            current_phase = GamePhase.Exploring  

    return True

def Exploring(phase : GamePhase, level_pods : set, enemies_present : dict):
    # check for enemies, if not empty switch to combat, else pop from level_pods
    # if level_pods is empty switch to game over (Victory)
    if enemies_present:
        phase = GamePhase.Combat
    elif level_pods:
        match level_pods.pop():
            case EnemyType.OrenianSwordsmen: pass # add 1-3 orenian swordsmen
            case EnemyType.OrenianHammerman: pass # add 1 orenian hammerman
            case _: print ("Invalid enemy type")
        phase = GamePhase.Combat
    else:
        current_phase = GamePhase.GameOver
        print ("Victory!")

def Combat(phase : GamePhase, level_pods : set, enemies_present : dict):
    # if player dies switch to game over (Defeat)
    if not enemies_present:
        current_phase = GamePhase.Exploring

    # combat here

def GameOver(level_pods : set, enemies_present : dict):
    if enemies_present or level_pods:
        print ("Defeat!")
    else:
        print ("Victory!")
    # end game on player confirmation (input)
    # highscore?
