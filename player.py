import pygame


class player:
    def __init__(self):
        self.stats = {
            'Name': 'Jonathan',
            'Icon': 'None',
            'Weapon': 'None',
            'Armor': 'None',
            'Profession': 'Swordsman',
            
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
            'Exp Cap': 15,
            'Exp': 0,

            'Accuracy': 75,
            'Evasion': 15,
            'Critical Chance': 10,
            'Critical Multiplier': 1.5,
            'Luck': 10,

            'Gold': 100,
            'Skill Points': 5
        }

        self.inventory = {
            'Weapons':{
                'Fists':{
                    'Name': 'Fists',
                    'Description': 'At least its something...',
                    'Icon': pygame.image.load('Images\Fists Icon.png'),
                    'Durability': 15,
                    'Max Durability': 15,
                    'Physical Attack': 2,
                    'Magic Attack': 1,
                    'Mana Cost': 0,
                    'Weight': 0,
                    'Stack': 1,
                    'Equipped': True,
                },
                'Iron Sword':{
                    'Name': 'Iron Sword',
                    'Description': 'High',
                    'Icon': pygame.image.load('Images\Fists Icon.png'),
                    'Equipped': True,
                    'Type': 'One Handed',
                    'Physical Attack': 2,
                    'Durability': 15,
                    'Max Durability': 15,
                }
            },
            'Armor':{
                'Simple Tunic':{
                    'Name': 'Simple Tunic',
                    'Description': 'More like a rag than a piece of armor',
                    'Physical Defense': 2,
                    'Magic Defense': 1,
                    'Weight': .25,
                    'Type': 'Chestplate',
                    'Equipped': True,
                }
            },
            'Consumables':{
                'Low Grade Health Potion':{
                    'Name': 'Low Grade Health Potion',
                    'Description': 'While it may restore some of your health, the taste is absolutely awful',
                }
            }
        }


