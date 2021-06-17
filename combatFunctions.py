import pygame

import random, time

from usefulFunctions import txtCenterFunction, speak
from monster import monster
from monsterPresets import medusaPreset
from combatSystems import calculateDMG, attack, updateGUI, rest

def combatFunction(rpg):
    enemy = monsterRandomizer(rpg)
    player = rpg.player
    updateGUI(rpg, player, enemy)

    while enemy.monster.stats['Hp'] > 1 and player.stats['Hp'] > 1:
        rpg.combatGUI.showEnemySlot2Indicator = False
        rpg.combatGUI.showPlayerIndicator = False
        if enemy.monster.stats['Agility'] > player.stats['Agility']:
            monsterTurn(rpg, enemy, player)
            if enemy.monster.stats['Hp'] < 1 or player.stats['Hp'] < 1:
                break
            playerTurn(rpg, enemy, player)
        else:
            playerTurn(rpg, enemy, player)
            if enemy.monster.stats['Hp'] < 1 or player.stats['Hp'] < 1:
                break
            monsterTurn(rpg, enemy, player)
    if player.stats['Hp'] > 1:    
        pygame.draw.rect(rpg.screen, (0,0,0), (0, 0, 1920, 1080))
        rpg.combatOpen = False
        loot(rpg, enemy)

def loot(rpg, enemy):
    speak(rpg, rpg.player.stats['Icon'], "Congrats You've gained 50 Gold!!!")

def monsterTurn(rpg, enemy, player):
    enemy.battleTatic(rpg, player)
    updateGUI(rpg, player, enemy)

def playerTurn(rpg, enemy, player):
    choice = ""
    while choice == "" or choice == None:
        choice = rpg.combatGUI.mouseEvents(rpg)
    if choice == "Attack":
        rpg.combatGUI.showPlayerIndicator = False
        attack(rpg, player, enemy.monster)
        rpg.combatGUI.showEnemySlot2Indicator = True
        updateGUI(rpg, player, enemy)
        rpg._update_screen()
        time.sleep(1)
    elif choice == "Flee":
        player.stats['Hp'] = 0
    elif choice == "Rest":
        rest(player)
    updateGUI(rpg, player, enemy)
    
def monsterRandomizer(rpg):
    monsterList = [medusaPreset(rpg)]
    return(random.choice(monsterList))

