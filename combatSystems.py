import pygame

import random, time

from usefulFunctions import txtCenterFunction, speak

def updateGUI(rpg, player, enemy):
    rpg.combatGUI.health.txt = "Health: {}/{}".format(player.stats['Hp'], player.stats['Max Hp'])
    rpg.combatGUI.mana.txt = "Mana: {}/{}" .format(player.stats['Mana'], player.stats['Max Mana'])
    rpg.combatGUI.stamina.txt = "Stamina: {}/{}" .format(player.stats['Stamina'], player.stats['Max Stamina'])
    rpg.combatGUI.healthBar.width = 400 * player.stats['Hp'] // player.stats['Max Hp']
    rpg.combatGUI.manaBar.width = 400 * player.stats['Mana'] // player.stats['Max Mana']
    rpg.combatGUI.staminaBar.width = 400 * player.stats['Stamina'] // player.stats['Max Stamina']
        
    txtCenterFunction(rpg.combatGUI.health, rpg.combatGUI.health.msg_image_rect, rpg.combatGUI.health.txt, rpg.combatGUI.health.font)
    txtCenterFunction(rpg.combatGUI.mana, rpg.combatGUI.mana.msg_image_rect, rpg.combatGUI.mana.txt, rpg.combatGUI.mana.font)
    txtCenterFunction(rpg.combatGUI.stamina, rpg.combatGUI.stamina.msg_image_rect, rpg.combatGUI.stamina.txt, rpg.combatGUI.stamina.font)
    txtCenterFunction(rpg.combatGUI.playerDamageIndicator, rpg.combatGUI.playerDamageIndicator.msg_image_rect, rpg.combatGUI.playerDamageIndicator.txt, rpg.combatGUI.playerDamageIndicator.font)

    rpg.combatGUI.enemySlot2.health.txt = "Health: {}/{}".format(enemy.monster.stats['Hp'], enemy.monster.stats['Max Hp'])
    rpg.combatGUI.enemySlot2.mana.txt = "Mana: {}/{}" .format(enemy.monster.stats['Mana'], enemy.monster.stats['Max Mana'])
    rpg.combatGUI.enemySlot2.stamina.txt = "Stamina: {}/{}" .format(enemy.monster.stats['Stamina'], enemy.monster.stats['Max Stamina'])
    rpg.combatGUI.enemySlot2.healthBar.width = 400 * enemy.monster.stats['Hp'] // enemy.monster.stats['Max Hp']
    rpg.combatGUI.enemySlot2.manaBar.width = 400 * enemy.monster.stats['Mana'] // enemy.monster.stats['Max Mana']
    rpg.combatGUI.enemySlot2.staminaBar.width = 400 * enemy.monster.stats['Stamina'] // enemy.monster.stats['Max Stamina']
        
    txtCenterFunction(rpg.combatGUI.enemySlot2.health, rpg.combatGUI.enemySlot2.health.msg_image_rect, rpg.combatGUI.enemySlot2.health.txt, rpg.combatGUI.enemySlot2.health.font)
    txtCenterFunction(rpg.combatGUI.enemySlot2.mana, rpg.combatGUI.enemySlot2.mana.msg_image_rect, rpg.combatGUI.enemySlot2.mana.txt, rpg.combatGUI.enemySlot2.mana.font)
    txtCenterFunction(rpg.combatGUI.enemySlot2.stamina, rpg.combatGUI.enemySlot2.stamina.msg_image_rect, rpg.combatGUI.enemySlot2.stamina.txt, rpg.combatGUI.enemySlot2.stamina.font)
    txtCenterFunction(rpg.combatGUI.enemySlot2.damageIndicator, rpg.combatGUI.enemySlot2.damageIndicator.msg_image_rect, rpg.combatGUI.enemySlot2.damageIndicator.txt, rpg.combatGUI.enemySlot2.damageIndicator.font)

def attack(rpg, combatant1, combatant2):
    critAchieved = False
    elementalAchived = False

    combatant1manaLoss = 0
    combantant1durabilityLoss = 0
    combatant1staminaLoss = 0

    DMG, critAchieved, elementalAchived = calculateDMG(combatant1, combatant2, True)
    combantant2durabilityLoss = round(DMG * .10)
    try:
        if combatant1.stats['Weapon']['Physical Attack'] != 0:
            combantant1durabilityLoss = round(combatant1.stats['Physical Attack'] * .75)
            combatant1staminaLoss = combatant1.stats['Physical Attack'] * 4
    except:
        combantant1durabilityLoss = round(combatant1.stats['Magic Attack'] * .75)
        combatant1manaLoss = combatant1.stats['Physical Attack'] * 4

    combatant1.stats['Weapon']['Durability'] -= combantant1durabilityLoss
    combatant1.stats['Stamina'] -= combatant1staminaLoss
    combatant1.stats['Mana'] -= combatant1manaLoss

    combatant2.stats['Hp'] -= DMG
    combatant2.stats['Weapon']['Durability'] -= combantant2durabilityLoss

    if critAchieved == True and elementalAchived == True:
        rpg.combatGUI.playerDamageIndicator.txt = "ELM + CRIT!! -{}!!".format(DMG)
        rpg.combatGUI.enemySlot2.damageIndicator.txt = "ELM + CRIT!! -{}!!".format(DMG)
    elif critAchieved == True:
        rpg.combatGUI.playerDamageIndicator.txt = "CRIT!! -{}".format(DMG)
        rpg.combatGUI.enemySlot2.damageIndicator.txt = "CRIT!! -{}".format(DMG)
    elif elementalAchived == True:
        rpg.combatGUI.playerDamageIndicator.txt = "ELM!! -{}!!".format(DMG)
        rpg.combatGUI.enemySlot2.damageIndicator.txt = "ELM!! -{}!!".format(DMG)
    else:
        rpg.combatGUI.playerDamageIndicator.txt = "-{}!!".format(DMG)
        rpg.combatGUI.enemySlot2.damageIndicator.txt = "-{}!!".format(DMG)


def calculateDMG(combatant1, combatant2, isfromAttack):
    critAchieved = False
    elementalAchived = False

    try:
        if combatant1.stats['Weapon']['Physical Attack'] != 0:
            DMG = combatant1.stats['Weapon']['Physical Attack'] + combatant1.stats['Physical Attack']
    except:
        DMG = combatant1.stats['Weapon']['Magic Attack'] + combatant1.stats['Magic Attack']
    try:
        elementalSuperiority = combatant1.stats['Weapon']['Elemental Intensity'] // combatant2.stats[combatant1.stats['Weapon']['Elemental Affinity'] + 'Resist']
        if elementalSuperiority > 2:
            DMG *= elementalSuperiority
            elementalSuperiority = True
    except:
        pass
    if random.randrange(0, 100) <= combatant1.stats['Critical Chance']:
        DMG *= combatant1.stats['Critical Multiplier']
        critAchieved = True
    try:
        if combatant1.stats['Weapon']['Physical Attack'] != 0:
            DMG -= (combatant2.stats['Physical Defense'] - combatant2.stats['Physical Penetration'])
    except:
        DMG -=(combatant2.stats['Magic Defense'] - combatant2.stats['Magic Penetration'])
    
    if isfromAttack == True:
        return(round(DMG), critAchieved, elementalAchived)
    else:
        return(DMG)

def rest(combatant):
    restHp = (round((combatant.stats['Max Hp'] * random.randrange(10, 25))/100))
    restStamina = (round((combatant.stats['Max Stamina'] * random.randrange(10, 25))/100))   

    combatant.stats['Hp'] += restHp
    combatant.stats['Stamina'] += restStamina

    if combatant.stats['Hp'] > combatant.stats['Max Hp']:
        combatant.stats['Hp'] = combatant.stats['Max Hp']
    if combatant.stats['Stamina'] > combatant.stats['Max Stamina']:
        combatant.stats['Stamina'] = combatant.stats['Max Stamina']