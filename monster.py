import pygame
import random
import time

from combatSystems import calculateDMG, attack, updateGUI

class monster:
    def __init__(self):
        self.stats = {
            'Name': 'None',
            'Icon': 'None',
            'Weapon': {},
            'Armor': {},
            
            'Max Hp': 100,
            'Hp': 100,
            
            'Physical Attack': 5,
            'Magic Attack': 5,
            'Agility': 5,

            'Max Stamina': 100,
            'Stamina': 100,
            'Max Mana': 100,
            'Mana': 100,

            'Physical Defense': 5,
            'Magic Defense': 5,
            'Physical Penetration': 5,
            'Magic Penetration': 5,
            
            'Fire Resist': 2,
            'Poison Resist': 2,
            'Water Resist': 2,
            'Earth Resist': 2,
            'Wind Resist': 2,

            'Level': 0,
            'Intelligence': 'High',
        
            'Accuracy': 75,
            'Evasion': 15,
            'Critical Chance': 10,
            'Critical Multiplier': 1.5,
            'Luck': 10,
        }

        self.lootPool1 = {}

#note to self made the decision to make monster presets into classes into functions

class medusaPreset:
    def __init__(self, rpg):
        self.monster = monster()

        self.monster.stats['Name'] = "Medusa"
        self.monster.stats['Icon'] = "Images\Medusa.png"
        self.monster.stats['Level'] = rpg.player.stats['Level'] 
        self.monster.stats['Max Hp'] = random.randint(round(rpg.player.stats['Max Hp'] * .20), round(rpg.player.stats['Max Hp'] * .35))
        self.monster.stats['Hp'] = self.monster.stats['Max Hp']
        
        self.monster.stats['Physical Attack'] = random.randint(round(rpg.player.stats['Physical Attack'] * .2), round(rpg.player.stats['Physical Attack'] * .4))
        self.monster.stats['Magic Attack'] = random.randint(round(rpg.player.stats['Magic Attack'] * .9), round(rpg.player.stats['Magic Attack'] * 1.4))
        self.monster.stats['Agility'] = random.randint(round(rpg.player.stats['Agility'] * .7), round(rpg.player.stats['Agility'] * 1.2))
        
        self.monster.stats['Max Stamina'] = random.randint(round(rpg.player.stats['Max Stamina'] * .1), round(rpg.player.stats['Max Stamina'] * .35))
        self.monster.stats['Stamina'] = self.monster.stats['Max Stamina']
        self.monster.stats['Max Mana'] = random.randint(round(rpg.player.stats['Max Mana'] * .35), round(rpg.player.stats['Max Mana'] * .7))
        self.monster.stats['Mana'] = self.monster.stats['Max Mana']
    
        self.monster.stats['Physical Defense'] =  random.randint(round(rpg.player.stats['Physical Defense'] * .9), round(rpg.player.stats['Physical Defense'] * 1.4))
        self.monster.stats['Magic Defense'] = random.randint(round(rpg.player.stats['Magic Defense'] * .4), round(rpg.player.stats['Magic Defense'] * .8))
        self.monster.stats['Physical Penetration'] = random.randint(round(rpg.player.stats['Physical Penetration'] * .4), round(rpg.player.stats['Physical Penetration'] * .9))
        self.monster.stats['Magic Penetration'] = random.randint(round(rpg.player.stats['Magic Penetration'] * .8), round(rpg.player.stats['Magic Penetration'] * 1.4))
        
        self.monster.stats['Fire Resist'] = random.randint(round(rpg.player.stats['Fire Resist'] * 1.1), round(rpg.player.stats['Fire Resist'] * 1.4))
        self.monster.stats['Poison Resist'] = random.randint(round(rpg.player.stats['Poison Resist'] * .9), round(rpg.player.stats['Poison Resist'] * 1.2))
        self.monster.stats['Water Resist'] = random.randint(round(rpg.player.stats['Water Resist']* .4), round(rpg.player.stats['Water Resist']* .8))
        self.monster.stats['Wind Resist'] = random.randint(round(rpg.player.stats['Wind Resist'] * .2), round(rpg.player.stats['Wind Resist'] * .4))
        self.monster.stats['Earth Resist'] = random.randint(round(rpg.player.stats['Earth Resist'] * .7), round(rpg.player.stats['Earth Resist'] * 1.1))

        self.monster.stats['Accuracy'] = 100
        self.monster.stats['Evasion'] = random.randint(round(rpg.player.stats['Evasion'] * .2), round(rpg.player.stats['Evasion'] * .4))
        self.monster.stats['Critical Chance'] = random.randint(round(rpg.player.stats['Critical Chance'] * 1.1), round(rpg.player.stats['Critical Chance'] * 1.4))
        self.monster.stats['Critical Multiplier'] = 2
        #medusa.stats['Luck'] = random.randint(rpg.player.stats['Luck']
        

        self.monster.stats['Weapon'] = {
            'Name': 'Laser Beam',
            'Description': 'The patanted magic of the Medusa race, it concentrates the eyesight to make a powerful attack. Probs will lead to blindness',
            'Icon': 'None',
            'Durability': 15,
            'Max Durability': 15,
            'Magic Attack': round(self.monster.stats['Magic Attack'] * 1.25),
            'Mana Cost': 5,
            'Weight': 1,
            'Stack': 1,
            'Elemental Affinity': 'Fire',
            'Elemental Intensity': 30,
            'Equipped': False
            }
        self.monster.stats['Secondary Weapon'] = {
            'Name': 'Fang of Medusa',
            'Description': 'A razor sharp tooth gatherd from the head of medusa, you would not want this for shaving',
            'Icon': 'None',
            'Durability': 30,
            'Max Durability': 30,
            'Physical Attack': self.monster.stats['Physical Attack'],
            'Stamina Cost': 2,
            'Weight': 1,
            'Stack': 1,
            'Elemental Affinity': 'None',
            'Elemental Intensity': 0,
            'Equipped': False
        }

        if self.monster.stats['Critical Chance'] > 100:
            self.monster.stats['Critical Chance'] = 100
        
        self.firstTurn = True
        self.secondTurn = True
        self.physicalDMG = 0
        self.magicDMG = 0
    
    def swapWeapons(self, wantedEquipped):
        if wantedEquipped == 'Physical':
            try:
                if self.monster.stats['Weapon']['Physical Attack'] != 0:
                    pass
            except:
                temp = self.monster.stats['Weapon']
                self.monster.stats['Weapon'] = self.monster.stats['Secondary Weapon']
                self.monster.stats['Secondary Weapon'] = temp
        elif wantedEquipped == 'Magic':
            try:
                if self.monster.stats['Weapon']['Magic Attack'] != 0:
                    pass
            except:
                temp = self.monster.stats['Weapon']
                self.monster.stats['Weapon'] = self.monster.stats['Secondary Weapon']
                self.monster.stats['Secondary Weapon'] = temp
            
    def battleTatic(self, rpg, player):
        if self.firstTurn == True:
            if random.randrange(0, 100) >= 50:
                self.swapWeapons('Magic')
                self.magicDMG = calculateDMG(self.monster, player, False)
                rpg.combatGUI.showEnemySlot2Indicator = False
                attack(rpg, self.monster, player)
                rpg.combatGUI.showPlayerIndicator = True
                updateGUI(rpg, player, self)
                rpg._update_screen()
                time.sleep(1)
            else:
                self.swapWeapons('Physical')
                self.physicalDMG = calculateDMG(self.monster, player, False)
                rpg.combatGUI.showEnemySlot2Indicator = False
                attack(rpg, self.monster, player)
                rpg.combatGUI.showPlayerIndicator = True
                updateGUI(rpg, player, self)
                rpg._update_screen()
                time.sleep(1)
            self.firstTurn = False
        elif self.secondTurn == True:
            if self.magicDMG == 0:
                self.swapWeapons('Magic')
                self.magicDMG = calculateDMG(self.monster, player, False)
                rpg.combatGUI.showEnemySlot2Indicator = False
                attack(rpg, self.monster, player)
                rpg.combatGUI.showPlayerIndicator = True
                updateGUI(rpg, player, self)
                rpg._update_screen()
                time.sleep(1)
            else:
                self.swapWeapons('Physical')
                self.physicalDMG = calculateDMG(self.monster, player, False)
                rpg.combatGUI.showEnemySlot2Indicator = False
                attack(rpg, self.monster, player)
                rpg.combatGUI.showPlayerIndicator = True
                updateGUI(rpg, player, self)
                rpg._update_screen()
                time.sleep(1)
            self.secondTurn = False
        if self.magicDMG > self.physicalDMG:
            self.swapWeapons('Magic')
            if self.monster.stats['Weapon']['Durability'] < 1:
                self.swapWeapons('Physical')
        else:
            self.swapWeapons('Physical')
            if self.monster.stats['Weapon']['Durability'] < 1:
                self.swapWeapons('Magic')

        if self.secondTurn == False:
            if self.monster.stats['Hp'] < round(self.monster.stats['Max Hp'] * .15):
                if random.randrange(0, 100) < 25:
                    player.stats['Hp'] -= calculateDMG(self.monster, player, False) + self.monster.stats['Hp']
                    self.monster.stats['Hp'] = 0
            if self.monster.stats['Hp'] < round(self.monster.stats['Max Hp'] * .35) or self.monster.stats['Stamina'] < round(self.monster.stats['Max Stamina'] * .35) or self.monster.stats['Mana'] < round(self.monster.stats['Max Mana'] * .35): 
                pass
                #rest
            else:
                rpg.combatGUI.showEnemySlot2Indicator = False
                attack(rpg, self.monster, player)
                rpg.combatGUI.showPlayerIndicator = True
                updateGUI(rpg, player, self)
                rpg._update_screen()
                time.sleep(1)
        

        

            



