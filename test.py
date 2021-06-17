import random


inventory = {
            'Weapons':{
                'Fists':{
                    'Name': 'Fists',
                    'Description': 'At least its something...',
                    #'Icon': pygame.image.load(''),
                    'Physical Attack': 2,
                    'Magic Attack': 1,
                    'Mana Cost': 0,
                    'Weight': 0,
                    'Equipped': True,
                },
                'Magic':{
                    'Name': 'Fists',
                    'Description': 'At least its something...',
                    #'Icon': pygame.image.load(''),
                    'Physical Attack': 2,
                    'Magic Attack': 1,
                    'Mana Cost': 0,
                    'Weight': 0,
                }
            },
            'Armor':{
                'Simple Tunic':{
                    'Name': 'Simple Tunic',
                    'Description': 'More like a rag than a piece of armor',
                    'Physical Defense': 2,
                    'Magic Defense': 1,
                    'Weight': .25,
                }
            },
            'Consumables':{
                'Low Grade Health Potion':{
                    'Name': 'Low Grade Health Potion',
                    'Description': 'While it may restore some of your health, the taste is absolutely awful',
                    #'Buff': self.hp + 10,
                }
            }
        }

weapons = {
        'Name': 'Fang of Medusa',
        'Description': 'A razor sharp tooth gatherd from the head of medusa, you would not want this for shaving',
        'Icon': 'None',
        'Durability': 30,
        'Max Durability': 30,
        'Physical Attack': 3,
        'Stamina Cost': 2,
        'Weight': 1,
        'Stack': 1,
        'Equipped': False
    }

print(weapons['Physical Attack'])