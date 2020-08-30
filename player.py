import pygame


class player:
    def __init__(self):
        self.name = ""
        self.icon = ""

        self.weapon = ""
        self.armor = ""

        self.profession = ""

        self.maxHp = 100
        self.hp = 100

        self.physicalAttack = 5
        self.magicAttack = 5
        self.agility = 5

        self.maxStamina = 100
        self.stamina = 100
        self.maxMana = 100
        self.mana = 100

        self.physicalDefense = 5
        self.magicDefense = 5

        self.fireResist = 2
        self.poisonResist = 2
        self.waterResist = 2
        self.earthResist = 2
        self.windResit = 2

        self.level = 0 
        self.expCap = 15
        self.exp = 0 

        self.accuracy = 75
        self.evasion = 15
        self.criticalChance = 10
        self.criticalMultiplier = 1.5
        self.luck = 10

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
                    'Buff': self.hp + 10,
                }
            }
        }


