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

number = 0
check = list(inventory['Weapons'])[number]
print(check)


for item in inventory['Weapons']:
    if inventory['Weapons'][list(inventory['Weapons'])[number]]['Equipped'] == True:
        print("Hi")
        number += 1