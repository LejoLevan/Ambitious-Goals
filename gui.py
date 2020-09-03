"""This file contains classes and function 
making up the game's gui"""

import pygame
import time
import sys

from Images.searchUp import searchUp
from usefulFunctions import txtCenterFunction, txtSplitter

# pylint: disable=invalid-name
class buildingBlocks:
    def __init__(self, rpg):
        """Useful class for making gui components

        Args:
            rpg (variable): has all that useful game info
        """

        self.screen = rpg.screen

        self.width, self.height = 0, 0
        self.left, self.top = 0, 0

        self.font = pygame.font.SysFont('cambria', 35)
        self.image = None
        self.txt = ""

        self.button_color = (0, 0, 0)
        self.text_color = (200, 200, 200)

        self.border = False
        self.clickable = False
        self.transparent = False

        try:
            self.msg_image = self.font.render(self.txt, True, self.text_color)
            self.msg_image_rect = self.msg_image.get_rect()
        except:
            pass
        self.draw()

    def draw(self):
        """Method updates necessary variables and displays gui components
        """
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
        if self.border == True:
            pygame.draw.rect(self.screen, self.text_color, self.rect, 3)
        if self.transparent == False:
            self.screen.fill(self.button_color, self.rect)
        try:
            self.screen.blit(self.image, self.rect)
        except:
            pass
        try:
            self.image_rect = self.image.get_rect()
        except:
            pass
        try:
            self.msg_image = self.font.render(self.txt, True, self.text_color, None)
            self.screen.blit(self.msg_image, self.msg_image_rect)
        except:
            pass
        if (self.clickable == True):
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.button_color = (115, 115, 115)
            else:
                self.button_color = (0, 0, 0)

class combatGUI:
    def __init__(self, rpg):
        self.background = buildingBlocks(rpg)
        self.background.width, self.background.height = 1920, 1080
        self.background.left, self.background.top = 0, 0
        self.background.image = pygame.transform.scale(pygame.image.load("Images\Dungeon.jpg"), (1920, 1080))

        self.playerIcon = buildingBlocks(rpg)
        self.playerIcon.width, self.playerIcon.height = 200, 200
        self.playerIcon.left, self.playerIcon.top = 125, 787
        self.playerIcon.image = pygame.image.load("Images\Bandit_4.png").convert_alpha()
        self.playerIcon.transparent = True
        self.playerIcon.image = pygame.transform.scale(self.playerIcon.image, (200, 200))
        #self.playerIcon.border = True
        
        self.health = buildingBlocks(rpg)
        self.health.width, self.health.height = 400, 30
        self.health.left, self.health.top = 25, 988.5
        self.health.txt = "Health 100/100"
        self.health.font = pygame.font.SysFont('cambria', 20)
        self.health.msg_image_rect.top = 993.5
        txtCenterFunction(self.health, self.health.msg_image_rect, self.health.txt, self.health.font)
        self.health.border = True
        self.health.transparent = True

        self.healthBar = buildingBlocks(rpg)
        self.healthBar.button_color = (100, 0, 0)
        self.healthBar.width, self.healthBar.height = 400, 30
        self.healthBar.left, self.healthBar.top = 25, 988.5

        self.mana = buildingBlocks(rpg)
        self.mana.width, self.mana.height = 400, 30
        self.mana.left, self.mana.top = 25, 1018.5
        self.mana.txt = "Mana 100/100"
        self.mana.font = pygame.font.SysFont('cambria', 20)
        self.mana.msg_image_rect.top = 1023.5
        txtCenterFunction(self.mana, self.mana.msg_image_rect, self.mana.txt, self.mana.font)
        self.mana.border = True
        self.mana.transparent = True

        self.manaBar = buildingBlocks(rpg)
        self.manaBar.button_color = (0, 0, 100)
        self.manaBar.width, self.manaBar.height = 400, 30
        self.manaBar.left, self.manaBar.top = 25, 1018.5

        self.stamina = buildingBlocks(rpg)
        self.stamina.width, self.stamina.height = 400, 30
        self.stamina.left, self.stamina.top = 25, 1048.5
        self.stamina.txt = "Stamina 100/100"
        self.stamina.font = pygame.font.SysFont('cambria', 20)
        self.stamina.msg_image_rect.top = 1053.5
        txtCenterFunction(self.stamina, self.stamina.msg_image_rect, self.stamina.txt, self.stamina.font)
        self.stamina.border = True
        self.stamina.transparent = True

        self.staminaBar = buildingBlocks(rpg)
        self.staminaBar.button_color = (0, 100, 0)
        self.staminaBar.width, self.staminaBar.height = 400, 30
        self.staminaBar.left, self.staminaBar.top = 25, 1048.5

        self.enemySlot2 = buildingBlocks(rpg)
        self.enemySlot2.width, self.enemySlot2.height = 400, 400
        self.enemySlot2.left, self.enemySlot2.top = 760, 225
        self.enemySlot2.txt = "Madusa Lvl: 50"
        self.enemySlot2.font = pygame.font.SysFont('cambria', 30)
        self.enemySlot2.msg_image_rect.top = 95
        txtCenterFunction(self.enemySlot2, self.enemySlot2.msg_image_rect, self.enemySlot2.txt, self.enemySlot2.font)
        self.enemySlot2.image = pygame.image.load('Images\Monster.png')
        self.enemySlot2.transparent = True
        self.enemySlot2.mana = buildingBlocks(rpg)
        self.enemySlot2.mana.width, self.enemySlot2.mana.height = 400, 30
        self.enemySlot2.mana.left, self.enemySlot2.mana.top = 760, 195
        self.enemySlot2.mana.txt = "Mana 100/100"
        self.enemySlot2.mana.font = pygame.font.SysFont('cambria', 20)
        self.enemySlot2.mana.msg_image_rect.top = 200
        txtCenterFunction(self.enemySlot2.mana, self.enemySlot2.mana.msg_image_rect, self.enemySlot2.mana.txt, self.enemySlot2.mana.font)
        self.enemySlot2.mana.border = True
        self.enemySlot2.mana.transparent = True
        self.enemySlot2.manaBar = buildingBlocks(rpg)
        self.enemySlot2.manaBar.button_color = (0, 100, 0)
        self.enemySlot2.manaBar.width, self.enemySlot2.manaBar.height = 400, 30
        self.enemySlot2.manaBar.left, self.enemySlot2.manaBar.top = 760, 195
        self.enemySlot2.stamina = buildingBlocks(rpg)
        self.enemySlot2.stamina.width, self.enemySlot2.stamina.height = 400, 30
        self.enemySlot2.stamina.left, self.enemySlot2.stamina.top = 760, 165
        self.enemySlot2.stamina.txt = "Stamina 100/100"
        self.enemySlot2.stamina.font = pygame.font.SysFont('cambria', 20)
        self.enemySlot2.stamina.msg_image_rect.top = 170
        txtCenterFunction(self.enemySlot2.stamina, self.enemySlot2.stamina.msg_image_rect, self.enemySlot2.stamina.txt, self.enemySlot2.stamina.font)
        self.enemySlot2.stamina.border = True
        self.enemySlot2.stamina.transparent = True
        self.enemySlot2.staminaBar = buildingBlocks(rpg)
        self.enemySlot2.staminaBar.button_color = (0, 0, 100)
        self.enemySlot2.staminaBar.width, self.enemySlot2.staminaBar.height = 400, 30
        self.enemySlot2.staminaBar.left, self.enemySlot2.staminaBar.top = 760, 165
        self.enemySlot2.health = buildingBlocks(rpg)
        self.enemySlot2.health.width, self.enemySlot2.health.height = 400, 30
        self.enemySlot2.health.left, self.enemySlot2.health.top = 760, 135
        self.enemySlot2.health.txt = "Health 100/100"
        self.enemySlot2.health.font = pygame.font.SysFont('cambria', 20)
        self.enemySlot2.health.msg_image_rect.top = 140
        txtCenterFunction(self.enemySlot2.health, self.enemySlot2.health.msg_image_rect, self.enemySlot2.health.txt, self.enemySlot2.health.font)
        self.enemySlot2.health.border = True
        self.enemySlot2.health.transparent = True
        self.enemySlot2.healthBar = buildingBlocks(rpg)
        self.enemySlot2.healthBar.button_color = (100, 0, 0)
        self.enemySlot2.healthBar.width, self.enemySlot2.healthBar.height = 400, 30
        self.enemySlot2.healthBar.left, self.enemySlot2.healthBar.top = 760, 135
    
    def update(self, rpg):
        self.health.txt = "Health: {}/{}".format(rpg.player.stats['Hp'], rpg.player.stats['Max Hp'])
        self.mana.txt = "Mana: {}/{}" .format(rpg.player.stats['Mana'], rpg.player.stats['Max Mana'])
        self.mana.txt = "Stamina: {}/{}" .format(rpg.player.stats['Stamina'], rpg.player.stats['Max Stamina'])
        
        txtCenterFunction(self.health, self.health.msg_image_rect, self.health.txt, self.health.font)
        txtCenterFunction(self.mana, self.mana.msg_image_rect, self.mana.txt, self.mana.font)
        txtCenterFunction(self.stamina, self.stamina.msg_image_rect, self.stamina.txt, self.stamina.font)

    def draw(self, rpg):
        self.update(rpg)

        self.background.draw()

        self.healthBar.draw()
        self.manaBar.draw()
        self.staminaBar.draw()

        self.health.draw()
        self.mana.draw()
        self.stamina.draw()

        self.playerIcon.draw()

        self.enemySlot2.draw()
        self.enemySlot2.manaBar.draw()
        self.enemySlot2.staminaBar.draw()
        self.enemySlot2.healthBar.draw()
        self.enemySlot2.mana.draw()
        self.enemySlot2.stamina.draw()
        self.enemySlot2.health.draw()

class dialogueBlock:
    def __init__(self, rpg):
        self.dialogueBlock = buildingBlocks(rpg)
        self.dialogueBlock.width, self.dialogueBlock.height = 1917, 418.5
        self.dialogueBlock.top, self.dialogueBlock.left = 661.5, 1.5
        self.dialogueBlock.border = True

        self.iconBlock = buildingBlocks(rpg)
        self.iconBlock.width, self.iconBlock.height = 668.5, 418.5
        self.iconBlock.top, self.iconBlock.left = 661.5, 1.5
        self.iconBlock.image = pygame.image.load("Images\Thing.png")
        self.iconBlock.border = True

        self.txtSlot1 = buildingBlocks(rpg)
        self.txtSlot1.txt = ""
        self.txtSlot1.width, self.txtSlot1.height = 1248.5, 83.7
        self.txtSlot1.top, self.txtSlot1.left = 661.5, 670
        self.txtSlot1.msg_image_rect.top, self.txtSlot1.msg_image_rect.left = 683.85, 720

        self.txtSlot2 = buildingBlocks(rpg)
        self.txtSlot2.txt = ""
        self.txtSlot2.width, self.txtSlot2.height = 1248.5, 83.7
        self.txtSlot2.top, self.txtSlot2.left = 745.2, 670
        self.txtSlot2.msg_image_rect.top, self.txtSlot2.msg_image_rect.left = 769.55, 720

        self.txtSlot3 = buildingBlocks(rpg)
        self.txtSlot3.txt = ""
        self.txtSlot3.width, self.txtSlot3.height = 1248.5, 83.7
        self.txtSlot3.top, self.txtSlot3.left = 828.9, 670
        self.txtSlot3.msg_image_rect.top, self.txtSlot3.msg_image_rect.left = 853.25, 720

        self.txtSlot4 = buildingBlocks(rpg)
        self.txtSlot4.txt = ""
        self.txtSlot4.width, self.txtSlot4.height = 1248.5, 83.7
        self.txtSlot4.top, self.txtSlot4.left = 912.6, 670
        self.txtSlot4.msg_image_rect.top, self.txtSlot4.msg_image_rect.left = 936.95, 720

        self.txtSlot5 = buildingBlocks(rpg)
        self.txtSlot5.txt = ""
        self.txtSlot5.width, self.txtSlot5.height = 1248.5, 83.7
        self.txtSlot5.top, self.txtSlot5.left = 996.3, 670
        self.txtSlot5.msg_image_rect.top, self.txtSlot5.msg_image_rect.left = 1020.65, 720
        
    def wipe(self):
        self.txtSlot1.txt = ""
        self.txtSlot2.txt = ""
        self.txtSlot3.txt = ""
        self.txtSlot4.txt = ""
        self.txtSlot5.txt = ""
    
    def mouseEvents(self, mous_pos):
        if self.dialogueBlock.rect.collidepoint(mous_pos):
            self.clicked = True

    def draw(self):
        self.dialogueBlock.draw()
        self.iconBlock.draw()
        self.txtSlot1.draw()
        self.txtSlot2.draw()
        self.txtSlot3.draw()
        self.txtSlot4.draw()
        self.txtSlot5.draw()

class optionMenu:
    def __init__(self, rpg):
        self.menuBox = buildingBlocks(rpg)
        self.menuBox.width, self.menuBox.height = 420, 690
        self.menuBox.left, self.menuBox.top = 700, 195
        self.menuBox.border = True

        self.topicBanner = buildingBlocks(rpg)
        self.topicBanner.width, self.topicBanner.height = 420, 115
        self.topicBanner.left, self.topicBanner.top = 700, 195
        self.topicBanner.image = pygame.image.load("Images\General Settings Banner.png")

        self.slot1 = buildingBlocks(rpg)
        self.slot1.width, self.slot1.height = 420, 115
        self.slot1.left, self.slot1.top = 700, 310
        self.slot1.clickable = True
        self.slot1.txt = "1.) Resume Game"
        self.slot1.msg_image_rect.top, self.slot1.msg_image_rect.left = 347.5, 720

        self.slot2 = buildingBlocks(rpg)
        self.slot2.width, self.slot2.height = 420, 115
        self.slot2.left, self.slot2.top = 700, 425
        self.slot2.clickable = True
        self.slot2.txt = "2.) Save Game"
        self.slot2.msg_image_rect.top, self.slot2.msg_image_rect.left = 462.5, 720

        self.slot3 = buildingBlocks(rpg)
        self.slot3.width, self.slot3.height = 420, 115
        self.slot3.left, self.slot3.top = 700, 540
        self.slot3.clickable = True
        self.slot3.txt = "3.) Load Game"
        self.slot3.msg_image_rect.top, self.slot3.msg_image_rect.left = 572.5, 720

        self.slot4 = buildingBlocks(rpg)
        self.slot4.width, self.slot4.height = 420, 115
        self.slot4.left, self.slot4.top = 700, 665
        self.slot4.clickable = True
        self.slot4.txt = "4.) Help Button"
        self.slot4.msg_image_rect.top, self.slot4.msg_image_rect.left = 697.5, 720

        self.slot5 = buildingBlocks(rpg)
        self.slot5.width, self.slot5.height = 420, 115
        self.slot5.left, self.slot5.top = 700, 770
        self.slot5.clickable = True
        self.slot5.txt = "5.) Quit Game"
        self.slot5.msg_image_rect.top, self.slot5.msg_image_rect.left = 802.5, 720

        self.generalSettingsTxt = ["1.) Resume Game", "2.) Save Game", "3.) Load Game", "4.) Help Button", "5.) Quit Game"]
        self.playerSettingsTxt = ["1.) Player Statistics", "2.) Player Inventory", "3.) Quest Logs"]
        self.stopLoop = False

    def switchSettingTopic(self):
        if self.slot1.txt == "1.) Resume Game":
                self.slot1.txt = self.playerSettingsTxt[0]
                self.slot2.txt = self.playerSettingsTxt[1]
                self.slot3.txt = self.playerSettingsTxt[2]
                self.slot4.txt = ""
                self.slot5.txt = ""
                self.topicBanner.image = pygame.image.load("Images\Player Options Banner.png")
        else:
            self.slot1.txt = self.generalSettingsTxt[0]
            self.slot2.txt = self.generalSettingsTxt[1]
            self.slot3.txt = self.generalSettingsTxt[2]
            self.slot4.txt = self.generalSettingsTxt[3]
            self.slot5.txt = self.generalSettingsTxt[4]
            self.topicBanner.image = pygame.image.load("Images\General Settings Banner.png")


    def keyEvents(self, event):
        if event.key == pygame.K_d or event.key == pygame.K_a:
            self.switchSettingTopic()
    
    def mouseEvents(self, rpg, mous_pos):
        if self.topicBanner.rect.collidepoint(mous_pos):
            self.switchSettingTopic()
        if self.slot1.rect.collidepoint(mous_pos):
            if self.slot1.txt == "1.) Resume Game":
                self.stopLoop = True
            else:
                if rpg.statsOpen == False:
                    rpg.statsOpen = True
                else:
                    rpg.statsOpen = False
                self.stopLoop = True
        if self.slot2.rect.collidepoint(mous_pos):
            if self.slot1.txt == "1.) Resume Game":
                self.stopLoop = True
            else:
                if rpg.inventoryOpen == False:
                    rpg.inventoryOpen = True
                else:
                    rpg.inventoryOpen = False
        if self.slot3.rect.collidepoint(mous_pos):
            if self.slot1.txt == "1.) Resume Game":
                self.stopLoop = True
            else:
                self.stopLoop = True
        if self.slot4.rect.collidepoint(mous_pos):
            self.stopLoop = True
        if self.slot5.rect.collidepoint(mous_pos):
            if self.slot1.txt == "1.) Resume Game":
                sys.exit()

    def draw(self):
        self.menuBox.draw()
        self.topicBanner.draw()
        self.slot1.draw()
        self.slot2.draw()
        self.slot3.draw()
        self.slot4.draw()
        self.slot5.draw()

class Inventory:
    def __init__(self, rpg):
        self.mainBox = buildingBlocks(rpg)
        self.mainBox.width, self.mainBox.height = 840, 920
        self.mainBox.left, self.mainBox.top = 1060, 80
        self.mainBox.border = True

        self.title = buildingBlocks(rpg)
        self.title.width, self.title.height = 840, 92
        self.title.left, self.title.top = 1060, 80
        self.title.txt = "Player Inventory"
        self.title.msg_image_rect.top = 108.5
        txtCenterFunction(self.title, self.title.msg_image_rect, self.title.txt, self.title.font)

        self.equippedWeapon_1 = buildingBlocks(rpg)
        self.equippedWeapon_1.width, self.equippedWeapon_1.height = 420, 92
        self.equippedWeapon_1.left, self.equippedWeapon_1.top = 1060, 172
        self.equippedWeapon_1.font = pygame.font.SysFont('cambria', 25)
        self.equippedWeapon_1.msg_image_rect.top, self.equippedWeapon_1.msg_image_rect.left = 230, 1070
        self.equippedWeapon_1.border = True
        
        self.equippedWeapon_2 = buildingBlocks(rpg)
        self.equippedWeapon_2.width, self.equippedWeapon_2.height = 420, 92
        self.equippedWeapon_2.left, self.equippedWeapon_2.top = 1480, 172
        self.equippedWeapon_2.font = pygame.font.SysFont('cambria', 25)
        self.equippedWeapon_2.msg_image_rect.top, self.equippedWeapon_2.msg_image_rect.left = 230, 1490
        self.equippedWeapon_2.border = True

        self.equippedHelmet = buildingBlocks(rpg)
        self.equippedHelmet.width, self.equippedHelmet.height = 210, 92
        self.equippedHelmet.left, self.equippedHelmet.top = 1060, 264
        self.equippedHelmet.font = pygame.font.SysFont('cambria', 15)
        self.equippedHelmet.msg_image_rect.top, self.equippedHelmet.msg_image_rect.left = 330, 1070
        self.equippedHelmet.border = True

        self.equippedChestplate = buildingBlocks(rpg)
        self.equippedChestplate.width, self.equippedChestplate.height = 210, 92
        self.equippedChestplate.left, self.equippedChestplate.top = 1270, 264
        self.equippedChestplate.font = pygame.font.SysFont('cambria', 15)
        self.equippedChestplate.msg_image_rect.top, self.equippedChestplate.msg_image_rect.left = 330, 1280
        self.equippedChestplate.border = True

        self.equippedPants = buildingBlocks(rpg)
        self.equippedPants.width, self.equippedPants.height = 210, 92
        self.equippedPants.left, self.equippedPants.top = 1480, 264
        self.equippedPants.font = pygame.font.SysFont('cambria', 15)
        self.equippedPants.msg_image_rect.top, self.equippedPants.msg_image_rect.left = 330, 1490
        self.equippedPants.border = True

        self.equippedGlovesBoots = buildingBlocks(rpg)
        self.equippedGlovesBoots.width, self.equippedGlovesBoots.height = 210, 92
        self.equippedGlovesBoots.left, self.equippedGlovesBoots.top = 1690, 264
        self.equippedGlovesBoots.font = pygame.font.SysFont('cambria', 15)
        self.equippedGlovesBoots.msg_image_rect.top, self.equippedGlovesBoots.msg_image_rect.left = 330, 1700
        self.equippedGlovesBoots.border = True

        self.weaponsTab = buildingBlocks(rpg)
        self.weaponsTab.width, self.weaponsTab.height = 168, 80
        self.weaponsTab.left, self.weaponsTab.top = 1060, 357.5
        self.weaponsTab.image = pygame.image.load('Images\Weapons Tab.png')
        self.weaponsTab.clickable = True
        self.weaponsTab.border = True

        self.armorTab = buildingBlocks(rpg)
        self.armorTab.width, self.armorTab.height = 168, 80
        self.armorTab.left, self.armorTab.top = 1228, 357.5
        self.armorTab.image = pygame.image.load('Images\Armor Tab.png')
        self.armorTab.clickable = True
        self.armorTab.border = True

        self.consumableTab = buildingBlocks(rpg)
        self.consumableTab.width, self.consumableTab.height = 168, 80
        self.consumableTab.left, self.consumableTab.top = 1396, 357.5
        self.consumableTab.image = pygame.image.load('Images\Consumable Tab.png')
        self.consumableTab.clickable = True
        self.consumableTab.border = True

        self.materialsTab = buildingBlocks(rpg)
        self.materialsTab.width, self.materialsTab.height = 168, 80
        self.materialsTab.left, self.materialsTab.top = 1564, 357.5
        self.materialsTab.image = pygame.image.load('Images\Materials Tab.png')
        self.materialsTab.clickable = True
        self.materialsTab.border = True

        self.questTab = buildingBlocks(rpg)
        self.questTab.width, self.questTab.height = 168, 80
        self.questTab.left, self.questTab.top = 1732, 357.5
        self.questTab.image = pygame.image.load('Images\Quest Tab.png')
        self.questTab.clickable = True
        self.questTab.border = True

        self.slideBar1 = buildingBlocks(rpg)
        self.slideBar1.width, self.slideBar1.height = 60, 282
        self.slideBar1.left, self.slideBar1.top = 1840, 437.5
        self.slideBar1.image = pygame.image.load('Images\ArrowUp.png')
        self.slideBar1.clickable = True
        self.slideBar1.border = True
        
        self.slideBar2 = buildingBlocks(rpg)
        self.slideBar2.width, self.slideBar2.height = 60, 282
        self.slideBar2.left, self.slideBar2.top = 1840, 719.5
        self.slideBar2.image = pygame.image.load('Images\ArrowDown.png')
        self.slideBar2.clickable = True
        self.slideBar2.border = True

        self.box1 = buildingBlocks(rpg)
        self.box1.width, self.box1.height = 195, 94
        self.box1.left, self.box1.top = 1060, 437.5
        self.box2 = buildingBlocks(rpg)
        self.box2.width, self.box2.height = 195, 94
        self.box2.left, self.box2.top = 1255, 437.5
        self.box3 = buildingBlocks(rpg)
        self.box3.width, self.box3.height = 195, 94
        self.box3.left, self.box3.top = 1450, 437.5
        self.box4 = buildingBlocks(rpg)
        self.box4.width, self.box4.height = 195, 94
        self.box4.left, self.box4.top = 1645, 437.5

        self.box5 = buildingBlocks(rpg)
        self.box5.width, self.box5.height = 195, 94
        self.box5.left, self.box5.top = 1060, 531.5
        self.box6 = buildingBlocks(rpg)
        self.box6.width, self.box6.height = 195, 94
        self.box6.left, self.box6.top = 1255, 531.5
        self.box7 = buildingBlocks(rpg)
        self.box7.width, self.box7.height = 195, 94
        self.box7.left, self.box7.top = 1450, 531.5
        self.box8 = buildingBlocks(rpg)
        self.box8.width, self.box8.height = 195, 94
        self.box8.left, self.box8.top = 1645, 531.5

        self.box9 = buildingBlocks(rpg)
        self.box9.width, self.box9.height = 195, 94
        self.box9.left, self.box9.top = 1060, 625.5
        self.box10 = buildingBlocks(rpg)
        self.box10.width, self.box10.height = 195, 94
        self.box10.left, self.box10.top = 1255, 625.5
        self.box11 = buildingBlocks(rpg)
        self.box11.width, self.box11.height = 195, 94
        self.box11.left, self.box11.top = 1450, 625.5
        self.box12 = buildingBlocks(rpg)
        self.box12.width, self.box12.height = 195, 94
        self.box12.left, self.box12.top = 1645, 625.5

        self.box13 = buildingBlocks(rpg)
        self.box13.width, self.box13.height = 195, 94
        self.box13.left, self.box13.top = 1060, 719.5
        self.box14 = buildingBlocks(rpg)
        self.box14.width, self.box14.height = 195, 94
        self.box14.left, self.box14.top = 1255, 719.5
        self.box15 = buildingBlocks(rpg)
        self.box15.width, self.box15.height = 195, 94
        self.box15.left, self.box15.top = 1450, 719.5
        self.box16 = buildingBlocks(rpg)
        self.box16.width, self.box16.height = 195, 94
        self.box16.left, self.box16.top = 1645, 719.5

        self.box17 = buildingBlocks(rpg)
        self.box17.width, self.box17.height = 195, 94
        self.box17.left, self.box17.top = 1060, 813.5
        self.box18 = buildingBlocks(rpg)
        self.box18.width, self.box18.height = 195, 94
        self.box18.left, self.box18.top = 1255, 813.5
        self.box19 = buildingBlocks(rpg)
        self.box19.width, self.box19.height = 195, 94
        self.box19.left, self.box19.top = 1450, 813.5
        self.box20 = buildingBlocks(rpg)
        self.box20.width, self.box20.height = 195, 94
        self.box20.left, self.box20.top = 1645, 813.5

        self.box21 = buildingBlocks(rpg)
        self.box21.width, self.box21.height = 195, 94
        self.box21.left, self.box21.top = 1060, 907.5
        self.box22 = buildingBlocks(rpg)
        self.box22.width, self.box22.height = 195, 94
        self.box22.left, self.box22.top = 1255, 907.5
        self.box23 = buildingBlocks(rpg)
        self.box23.width, self.box23.height = 195, 94
        self.box23.left, self.box23.top = 1450, 907.5
        self.box24 = buildingBlocks(rpg)
        self.box24.width, self.box24.height = 195, 94
        self.box24.left, self.box24.top = 1645, 907.5

        self.weaponDescriptor = buildingBlocks(rpg)
        self.weaponDescriptor.width, self.weaponDescriptor.height = 220, 420
        self.weaponDescriptor.left, self.weaponDescriptor.top = 1500, 220
        self.weaponDescriptor.border = True
        
        self.weaponDescriptorTitle = buildingBlocks(rpg)
        self.weaponDescriptorTitle.width, self.weaponDescriptorTitle.height = 220, 60
        self.weaponDescriptorTitle.left, self.weaponDescriptorTitle.top = 1500, 220
        self.weaponDescriptorTitle.font = pygame.font.SysFont('cambria', 25)
        self.weaponDescriptorTitle.font.set_underline(True)
        self.weaponDescriptorTitle.txt = "Fists"
        self.weaponDescriptorTitle.msg_image_rect.top = 235
        self.weaponDescriptorTitle.border = True
        txtCenterFunction(self.weaponDescriptorTitle, self.weaponDescriptorTitle.msg_image_rect, self.weaponDescriptorTitle.txt, self.weaponDescriptorTitle.font)
        
        self.weaponDescriptorDMG = buildingBlocks(rpg)
        self.weaponDescriptorDMG.width, self.weaponDescriptorDMG.height = 220, 60
        self.weaponDescriptorDMG.left, self.weaponDescriptorDMG.top = 1500, 280
        self.weaponDescriptorDMG.font = pygame.font.SysFont('cambria', 20)
        self.weaponDescriptorDMG.txt = "Damage Output: 150"
        self.weaponDescriptorDMG.msg_image_rect.left, self.weaponDescriptorDMG.msg_image_rect.top = 1515, 300
        self.weaponDescriptorDMG.border = True

        self.weaponDescriptorDurability = buildingBlocks(rpg)
        self.weaponDescriptorDurability.width, self.weaponDescriptorDurability.height = 220, 60
        self.weaponDescriptorDurability.left, self.weaponDescriptorDurability.top = 1500, 340
        self.weaponDescriptorDurability.font = pygame.font.SysFont('cambria', 20)
        self.weaponDescriptorDurability.txt = "Durability: 15/15"
        self.weaponDescriptorDurability.msg_image_rect.left, self.weaponDescriptorDurability.msg_image_rect.top = 1515, 360
        self.weaponDescriptorDurability.border = True

        self.weaponDescriptorLine1 = buildingBlocks(rpg)
        self.weaponDescriptorLine1.width, self.weaponDescriptorLine1.height = 220, 40
        self.weaponDescriptorLine1.left, self.weaponDescriptorLine1.top = 1500, 401
        self.weaponDescriptorLine1.font = pygame.font.SysFont('cambria', 13)
        self.weaponDescriptorLine1.txt = "Description: Made out of bone"
        self.weaponDescriptorLine1.msg_image_rect.left, self.weaponDescriptorLine1.msg_image_rect.top = 1515, 413

        self.weaponDescriptorLine2 = buildingBlocks(rpg)
        self.weaponDescriptorLine2.width, self.weaponDescriptorLine2.height = 220, 40
        self.weaponDescriptorLine2.left, self.weaponDescriptorLine2.top = 1500, 440
        self.weaponDescriptorLine2.font = pygame.font.SysFont('cambria', 13)
        self.weaponDescriptorLine2.txt = "Description: Made out of bone"
        self.weaponDescriptorLine2.msg_image_rect.left, self.weaponDescriptorLine2.msg_image_rect.top = 1515, 453

        self.weaponDescriptorLine3 = buildingBlocks(rpg)
        self.weaponDescriptorLine3.width, self.weaponDescriptorLine3.height = 220, 40
        self.weaponDescriptorLine3.left, self.weaponDescriptorLine3.top = 1500, 480
        self.weaponDescriptorLine3.font = pygame.font.SysFont('cambria', 13)
        self.weaponDescriptorLine3.txt = "Description: Made out of bone"
        self.weaponDescriptorLine3.msg_image_rect.left, self.weaponDescriptorLine3.msg_image_rect.top = 1515, 493

        self.weaponDescriptorLine4 = buildingBlocks(rpg)
        self.weaponDescriptorLine4.width, self.weaponDescriptorLine4.height = 220, 40
        self.weaponDescriptorLine4.left, self.weaponDescriptorLine4.top = 1500, 520
        self.weaponDescriptorLine4.font = pygame.font.SysFont('cambria', 13)
        self.weaponDescriptorLine4.txt = "Description: Made out of bone"
        self.weaponDescriptorLine4.msg_image_rect.left, self.weaponDescriptorLine4.msg_image_rect.top = 1515, 533

        self.weaponDescriptorLine5 = buildingBlocks(rpg)
        self.weaponDescriptorLine5.width, self.weaponDescriptorLine5.height = 220, 40
        self.weaponDescriptorLine5.left, self.weaponDescriptorLine5.top = 1500, 560
        self.weaponDescriptorLine5.font = pygame.font.SysFont('cambria', 13)
        self.weaponDescriptorLine5.txt = "Description: Made out of bone"
        self.weaponDescriptorLine5.msg_image_rect.left, self.weaponDescriptorLine5.msg_image_rect.top = 1515, 573

        self.weaponDescriptorLine6 = buildingBlocks(rpg)
        self.weaponDescriptorLine6.width, self.weaponDescriptorLine6.height = 220, 40
        self.weaponDescriptorLine6.left, self.weaponDescriptorLine6.top = 1500, 600
        self.weaponDescriptorLine6.font = pygame.font.SysFont('cambria', 13)
        self.weaponDescriptorLine6.txt = "Description: Made out of bone"
        self.weaponDescriptorLine6.msg_image_rect.left, self.weaponDescriptorLine6.msg_image_rect.top = 1515, 613

        self.tab = 'Weapons'
        self.showDescriptor = False
        self.checkList = []
        self.set = 0
        self.boxList = [self.box1, self.box2, self.box3, self.box4,
        self.box5, self.box6, self.box7, self.box8, self.box9, self.box10,
        self.box11, self.box12, self.box13, self.box14, self.box15, self.box16,
        self.box17, self.box18, self.box19, self.box20, self.box21, self.box22, self.box23, self.box24]

    def update(self, rpg):
        self.clearInventory()
        for box in self.boxList:
            box.border = True
            number = self.set
            check = ""
            checkValid = False
            try:
                while checkValid == False:
                    check = list(rpg.player.inventory[self.tab])[number]
                    if check not in self.checkList:
                        self.checkList.append(check)
                        box.msg_image_rect.left, box.msg_image_rect.top = box.left + 15, (box.top + box.height) - 25
                        box.font = pygame.font.SysFont('cambria', 15)
                        box.txt = "{}".format(rpg.player.inventory[self.tab][check]['Name'])
                        box.image = rpg.player.inventory[self.tab][check]['Icon']
                        checkValid = True      
                    else:
                        number = number + 1
            except Exception:
                pass

        self.weaponEquipChecker(rpg)
        self.equipChecker(rpg, 'Armor', 'Helemt', self.equippedHelmet)
        self.equipChecker(rpg, 'Armor', 'Chestplate', self.equippedChestplate)
        self.equipChecker(rpg, 'Armor', 'Pants', self.equippedPants)
        self.equipChecker(rpg, 'Armor', 'Gloves and Boots', self.equippedGlovesBoots)

        mous_pos = pygame.mouse.get_pos()
        for box in self.boxList:
            if box.rect.collidepoint(mous_pos):
                if box.txt != "":
                    box.border = True

                    self.showDescriptor = True
                    self.weaponDescriptorTitle.txt = box.txt
                    txtCenterFunction(self.weaponDescriptorTitle, self.weaponDescriptorTitle.msg_image_rect, self.weaponDescriptorTitle.txt, self.weaponDescriptorTitle.font)
                    self.weaponDescriptor.left, self.weaponDescriptor.top = box.left + 245, box.top - 217.5
                    
                    self.weaponDescriptorTitle.left, self.weaponDescriptorTitle.top = box.left + 245, box.top - 217.5
                    self.weaponDescriptorTitle.msg_image_rect.top = box.top - 202.5
                    
                    self.weaponDescriptorDMG.left, self.weaponDescriptorDMG.top = box.left + 245, box.top - 157.5
                    self.weaponDescriptorDMG.msg_image_rect.left, self.weaponDescriptorDMG.msg_image_rect.top = box.left + 260, box.top - 137.5

                    self.weaponDescriptorDurability.left, self.weaponDescriptorDurability.top = box.left + 245, box.top - 97.5
                    self.weaponDescriptorDurability.msg_image_rect.left, self.weaponDescriptorDurability.msg_image_rect.top = box.left + 260, box.top - 77.5

                    self.weaponDescriptorLine1.left, self.weaponDescriptorLine1.top = box.left + 245, box.top - 36.5
                    self.weaponDescriptorLine1.msg_image_rect.left, self.weaponDescriptorLine1.msg_image_rect.top = box.left + 260, box.top - 24.5

                    self.weaponDescriptorLine2.left, self.weaponDescriptorLine2.top = box.left + 245,  box.top + 2.5
                    self.weaponDescriptorLine2.msg_image_rect.left, self.weaponDescriptorLine2.msg_image_rect.top = box.left + 260, box.top + 15.5

                    self.weaponDescriptorLine3.left, self.weaponDescriptorLine3.top = box.left + 245, box.top + 42.5
                    self.weaponDescriptorLine3.msg_image_rect.left, self.weaponDescriptorLine3.msg_image_rect.top = box.left + 260, box.top + 55.5

                    self.weaponDescriptorLine4.left, self.weaponDescriptorLine4.top = box.left + 245, box.top + 82.5
                    self.weaponDescriptorLine4.msg_image_rect.left, self.weaponDescriptorLine4.msg_image_rect.top = box.left + 260, box.top + 95.5

                    self.weaponDescriptorLine5.left, self.weaponDescriptorLine5.top = box.left + 245, box.top + 122.5
                    self.weaponDescriptorLine5.msg_image_rect.left, self.weaponDescriptorLine5.msg_image_rect.top = box.left + 260, box.top + 135.5

                    self.weaponDescriptorLine6.left, self.weaponDescriptorLine6.top = box.left + 245, box.top + 162.5
                    self.weaponDescriptorLine6.msg_image_rect.left, self.weaponDescriptorLine6.msg_image_rect.top = box.left + 260, box.top + 175.5

                    if self.tab == 'Weapons':
                        try:
                            self.weaponDescriptorDMG.txt = "Physical Damage: {}".format(rpg.player.inventory[self.tab][box.txt]['Physical Attack'])
                        except:
                            self.weaponDescriptorDMG.txt = "Magic Damage: {}".format(rpg.player.inventory[self.tab][box.txt]['Magic Attack'])
                        self.weaponDescriptorDurability.txt = "Durability: {}/{}".format(rpg.player.inventory[self.tab][box.txt]['Durability'], rpg.player.inventory[self.tab][box.txt]['Max Durability'])
                    if self.tab == 'Armor':
                        try:
                            self.weaponDescriptorDMG.txt = "Physical Defense: {}".format(rpg.player.inventory[self.tab][box.txt]['Physical Defense'])
                        except:
                            self.weaponDescriptorDMG.txt = "Magic Defense: {}".format(rpg.player.inventory[self.tab][box.txt]['Magic Defense'])
                    if self.tab == 'Consumable':
                        pass
                    if self.tab == 'Materials':
                        pass
                    if self.tab == 'Quest Items':
                        pass
                try:
                    self.weaponDescriptorLine1.txt = "Description: {}".format(rpg.player.inventory[self.tab][box.txt]['Description']) 
                    self.weaponDescriptorLine1.txt, self.weaponDescriptorLine2.txt = txtSplitter(self.weaponDescriptorLine1, self.weaponDescriptorLine1.font, self.weaponDescriptorLine1.txt, 13)
                    self.weaponDescriptorLine2.txt, self.weaponDescriptorLine3.txt = txtSplitter(self.weaponDescriptorLine2, self.weaponDescriptorLine2.font, self.weaponDescriptorLine2.txt, 13)
                    self.weaponDescriptorLine3.txt, self.weaponDescriptorLine4.txt = txtSplitter(self.weaponDescriptorLine3, self.weaponDescriptorLine3.font, self.weaponDescriptorLine3.txt, 13)
                    self.weaponDescriptorLine4.txt, self.weaponDescriptorLine5.txt = txtSplitter(self.weaponDescriptorLine4, self.weaponDescriptorLine4.font, self.weaponDescriptorLine4.txt, 13)
                    self.weaponDescriptorLine5.txt, self.weaponDescriptorLine6.txt = txtSplitter(self.weaponDescriptorLine5, self.weaponDescriptorLine5.font, self.weaponDescriptorLine5.txt, 13)
                except:
                    pass
                break
            else:
                self.showDescriptor = False

    def weaponEquipChecker(self, rpg):
        number = 0
        count = 0 
        for item in rpg.player.inventory['Weapons']:
            try:
                if rpg.player.inventory['Weapons'][list(rpg.player.inventory['Weapons'])[number]]['Equipped'] == True:
                    if self.equippedWeapon_1.txt == "":
                        self.equippedWeapon_1.txt = list(rpg.player.inventory['Weapons'])[number]
                        self.equippedWeapon_1.image = rpg.player.inventory['Weapons'][list(rpg.player.inventory['Weapons'])[number]]['Icon']
                    elif self.equippedWeapon_2.txt == "":
                        self.equippedWeapon_2.txt = list(rpg.player.inventory['Weapons'])[number]
                        self.equippedWeapon_2.image = rpg.player.inventory['Weapons'][list(rpg.player.inventory['Weapons'])[number]]['Icon']
                    count += 1
                    if rpg.player.inventory['Weapons'][list(rpg.player.inventory['Weapons'])[number]]['Type'] == 'Two Handed':
                        self.equippedWeapon_1.txt = list(rpg.player.inventory['Weapons'])[number]
                        self.equippedWeapon_1.image = rpg.player.inventory['Weapons'][list(rpg.player.inventory['Weapons'])[number]]['Icon']
                        self.equippedWeapon_2.button_color = (200, 200, 200)
                    else:
                        self.equippedWeapon_2.button_color = (0, 0, 0)
            except:
                pass
            number += 1
        if count < 2:
            self.equippedWeapon_2.txt = ""

    def equipChecker(self, rpg, tab, Type, txtSurface):
        number = 0
        for item in rpg.player.inventory[tab]:
            try:
                if rpg.player.inventory[tab][list(rpg.player.inventory[tab])[number]]['Equipped'] == True:
                    if rpg.player.inventory[tab][list(rpg.player.inventory[tab])[number]]['Type'] == Type:
                        txtSurface.txt = list(rpg.player.inventory[tab])[number]
            except:
                pass
    
    def clearInventory(self):
        self.checkList = []
        for box in self.boxList:
            box.image = ""
            box.txt = ""
    
    def mouseEvents(self, mous_pos):
        if self.slideBar2.rect.collidepoint(mous_pos):
            self.set += 24
        if self.slideBar1.rect.collidepoint(mous_pos):
            self.set -= 24
            if self.set < 0:
                self.set = 0
        if self.weaponsTab.rect.collidepoint(mous_pos):
            self.tab = "Weapons"
        if self.armorTab.rect.collidepoint(mous_pos):
            self.tab = "Armor"
        if self.consumableTab.rect.collidepoint(mous_pos):
            self.tab = "Consumable"
        if self.questTab.rect.collidepoint(mous_pos):
            self.tab = "Quest Items"
        if self.materialsTab.rect.collidepoint(mous_pos):
            self.tab = "Materials"
        
    def draw(self, rpg):
        self.update(rpg)

        self.mainBox.draw()
        self.title.draw()

        self.equippedWeapon_1.draw()
        self.equippedWeapon_2.draw()
        self.equippedHelmet.draw()
        self.equippedChestplate.draw()
        self.equippedPants.draw()
        self.equippedGlovesBoots.draw()

        self.slideBar1.draw()
        self.slideBar2.draw()

        self.weaponsTab.draw()
        self.armorTab.draw()
        self.consumableTab.draw()
        self.materialsTab.draw()
        self.questTab.draw()

        self.box1.draw()
        self.box2.draw()
        self.box3.draw()
        self.box4.draw()
        self.box5.draw()
        self.box6.draw()
        self.box7.draw()
        self.box8.draw()
        self.box9.draw()
        self.box10.draw()
        self.box11.draw()
        self.box12.draw()
        self.box13.draw()
        self.box14.draw()
        self.box15.draw()
        self.box16.draw()
        self.box17.draw()
        self.box18.draw()
        self.box19.draw()
        self.box20.draw()
        self.box21.draw()
        self.box22.draw()
        self.box23.draw()
        self.box24.draw()

        if self.showDescriptor == True:
            self.weaponDescriptor.draw()
            self.weaponDescriptorTitle.draw()
            self.weaponDescriptorDMG.draw()
            self.weaponDescriptorDurability.draw()
            self.weaponDescriptorLine1.draw()
            self.weaponDescriptorLine2.draw()
            self.weaponDescriptorLine3.draw()
            self.weaponDescriptorLine4.draw()
            self.weaponDescriptorLine5.draw()
            self.weaponDescriptorLine6.draw()
        
class playerStats:
    def __init__(self, rpg):
        self.mainBox = buildingBlocks(rpg)
        self.mainBox.width, self.mainBox.height = 385, 920
        self.mainBox.left, self.mainBox.top = 20, 80
        self.mainBox.border = True

        self.iconBox = buildingBlocks(rpg)
        self.iconBox.width, self.iconBox.height = 120, 240
        self.iconBox.left, self.iconBox.top = 20, 80
        self.iconBox.border = True
        self.iconBox.image = pygame.image.load('Images\Bandit_4.png')
        
        self.infoBox = buildingBlocks(rpg)
        self.infoBox.width, self.infoBox.height = 265, 240
        self.infoBox.left, self.infoBox.top = 140, 80
        self.infoBox.border = True
        
        self.name = buildingBlocks(rpg)
        self.name.width, self.name.height = 265, 40
        self.name.left, self.name.top = 140, 80
        self.name.border = True
        self.name.font = pygame.font.SysFont('cambria', 20)
        self.name.msg_image_rect.top = 90
        txtCenterFunction(self.name, self.name.msg_image_rect, self.name.txt, self.name.font)

        self.level = buildingBlocks(rpg)
        self.level.width, self.level.height = 132.5, 40
        self.level.left, self.level.top = 140, 120
        self.level.border = True
        self.level.font = pygame.font.SysFont('cambria', 20)
        self.level.msg_image_rect.top = 130
        txtCenterFunction(self.level, self.level.msg_image_rect, self.level.txt, self.level.font)

        self.exp = buildingBlocks(rpg)
        self.exp.width, self.exp.height = 132.5, 40
        self.exp.left, self.exp.top = 272.5, 120
        self.exp.border = True
        self.exp.font = pygame.font.SysFont('cambria', 20)
        self.exp.msg_image_rect.top = 130
        txtCenterFunction(self.exp, self.exp.msg_image_rect, self.exp.txt, self.exp.font)

        self.occupation = buildingBlocks(rpg)
        self.occupation.width, self.occupation.height = 132.5, 40
        self.occupation.left, self.occupation.top = 140, 160
        self.occupation.border = True
        self.occupation.txt = "{}".format(rpg.player.stats['Profession'])
        self.occupation.font = pygame.font.SysFont('cambria', 20)
        self.occupation.msg_image_rect.top = 170
        txtCenterFunction(self.occupation, self.occupation.msg_image_rect, self.occupation.txt, self.occupation.font)

        self.gold = buildingBlocks(rpg)
        self.gold.width, self.gold.height = 132.5, 40
        self.gold.left, self.gold.top = 272.5, 160
        self.gold.border = True
        self.gold.font = pygame.font.SysFont('cambria', 20)
        self.gold.msg_image_rect.top = 170
        txtCenterFunction(self.gold, self.gold.msg_image_rect, self.gold.txt, self.gold.font)

        self.health = buildingBlocks(rpg)
        self.health.width, self.health.height = 265, 40
        self.health.left, self.health.top = 140, 200
        self.health.border = True
        self.health.transparent = True
        self.health.font = pygame.font.SysFont('cambria', 20)
        self.health.msg_image_rect.top = 210
        txtCenterFunction(self.health, self.health.msg_image_rect, self.health.txt, self.health.font)
        
        self.healthBar = buildingBlocks(rpg)
        self.healthBar.button_color = (100, 0, 0)
        self.healthBar.width, self.healthBar.height = 265, 40
        self.healthBar.left, self.healthBar.top = 140, 200

        self.mana = buildingBlocks(rpg)
        self.mana.width, self.mana.height = 265, 40
        self.mana.left, self.mana.top = 140, 240
        self.mana.border = True
        self.mana.transparent = True
        self.mana.font = pygame.font.SysFont('cambria', 20)
        self.mana.msg_image_rect.top = 250
        txtCenterFunction(self.mana, self.mana.msg_image_rect, self.mana.txt, self.mana.font)

        self.manaBar = buildingBlocks(rpg)
        self.manaBar.button_color = (0, 0, 100)
        self.manaBar.width, self.manaBar.height = 265, 40
        self.manaBar.left, self.manaBar.top = 140, 240

        self.stamina = buildingBlocks(rpg)
        self.stamina.width, self.stamina.height = 265, 40
        self.stamina.left, self.stamina.top = 140, 280
        self.stamina.border = True
        self.stamina.transparent = True
        self.stamina.font = pygame.font.SysFont('cambria', 20)
        self.stamina.msg_image_rect.top = 290
        txtCenterFunction(self.stamina, self.stamina.msg_image_rect, self.stamina.txt, self.stamina.font)

        self.staminaBar = buildingBlocks(rpg)
        self.staminaBar.button_color = (0, 100, 0)
        self.staminaBar.width, self.staminaBar.height = 265, 40
        self.staminaBar.left, self.staminaBar.top = 140, 280

        self.skillPoints = buildingBlocks(rpg)
        self.skillPoints.width, self.skillPoints.height = 385, 50
        self.skillPoints.left, self.skillPoints.top = 20, 320
        self.skillPoints.font = pygame.font.SysFont('cambria', 20)
        self.skillPoints.msg_image_rect.top = 335
        txtCenterFunction(self.skillPoints, self.skillPoints.msg_image_rect, self.skillPoints.txt, self.skillPoints.font)
        self.skillPoints.border = True

        self.scrollUp = buildingBlocks(rpg)
        self.scrollUp.width, self.scrollUp.height = 60, 315
        self.scrollUp.left, self.scrollUp.top = 20, 370
        self.scrollUp.image = pygame.image.load('Images\ArrowUpStat.png')
        self.scrollUp.clickable = True
        self.scrollUp.border = True

        self.scrollDown = buildingBlocks(rpg)
        self.scrollDown.width, self.scrollDown.height = 60, 315
        self.scrollDown.left, self.scrollDown.top = 20, 685
        self.scrollDown.image = pygame.image.load('Images\ArrowDownStat.png')
        self.scrollDown.clickable = True
        self.scrollDown.border = True

        self.skillBox1 = buildingBlocks(rpg)
        self.skillBox1.width, self.skillBox1.height = 325, 70
        self.skillBox1.left, self.skillBox1.top = 80, 370
        self.skillBox1.font = pygame.font.SysFont('cambria', 30)
        self.skillBox1.msg_image_rect.top = 385
        txtCenterFunction(self.skillBox1, self.skillBox1.msg_image_rect, self.skillBox1.txt, self.skillBox1.font)
        self.skillBox1.border = True
        self.skillBox1.skill = ''
        self.skillBox1.skillOption1 = 'Physical Attack'
        self.skillBox1.skillOption2 = 'Agility'
        self.skillBox1.TextOption1 = 'Strength: {}'.format(rpg.player.stats['Physical Attack'])
        self.skillBox1.ImageOption1 = pygame.image.load('Images\Strength.png')
        self.skillBox1.TextOption2 = 'Agility: {}'.format(rpg.player.stats['Agility'])
        self.skillBox1.ImageOption2 = pygame.image.load('Images\Agility.png')

        self.skillBox2 = buildingBlocks(rpg)
        self.skillBox2.width, self.skillBox2.height = 325, 70
        self.skillBox2.left, self.skillBox2.top = 80, 440
        self.skillBox2.font = pygame.font.SysFont('cambria', 30)
        self.skillBox2.msg_image_rect.top = 455
        txtCenterFunction(self.skillBox2, self.skillBox2.msg_image_rect, self.skillBox2.txt, self.skillBox2.font)
        self.skillBox2.border = True
        self.skillBox2.skill = ''
        self.skillBox2.skillOption1 = 'Magic Attack'
        self.skillBox2.skillOption2 = 'Evasion'
        self.skillBox2.TextOption1 = 'Intelligence: {}'.format(rpg.player.stats['Magic Attack'])
        self.skillBox2.ImageOption1 = pygame.image.load('Images\Intelligence.png')
        self.skillBox2.TextOption2 = 'Evasion: {}'.format(rpg.player.stats['Evasion'])
        self.skillBox2.ImageOption2 = pygame.image.load('Images\Evasion.png')

        self.skillBox3 = buildingBlocks(rpg)
        self.skillBox3.width, self.skillBox3.height = 325, 70
        self.skillBox3.left, self.skillBox3.top = 80, 510
        self.skillBox3.font = pygame.font.SysFont('cambria', 30)
        self.skillBox3.msg_image_rect.top = 525
        txtCenterFunction(self.skillBox3, self.skillBox3.msg_image_rect, self.skillBox3.txt, self.skillBox3.font)
        self.skillBox3.border = True
        self.skillBox3.skill = ''
        self.skillBox3.skillOption1 = 'Physical Defense'
        self.skillBox3.skillOption2 = 'Accuracy'
        self.skillBox3.TextOption1 = 'P. Defense: {}'.format(rpg.player.stats['Physical Defense'])
        self.skillBox3.ImageOption1 = pygame.image.load('Images\PhysicalDefense.png')
        self.skillBox3.TextOption2 = 'Accuracy: {}'.format(rpg.player.stats['Accuracy'])
        self.skillBox3.ImageOption2 = pygame.image.load('Images\Accuracy.png')

        self.skillBox4 = buildingBlocks(rpg)
        self.skillBox4.width, self.skillBox4.height = 325, 70
        self.skillBox4.left, self.skillBox4.top = 80, 580
        self.skillBox4.font = pygame.font.SysFont('cambria', 30)
        self.skillBox4.msg_image_rect.top = 595
        txtCenterFunction(self.skillBox4, self.skillBox4.msg_image_rect, self.skillBox4.txt, self.skillBox4.font)
        self.skillBox4.border = True
        self.skillBox4.skill = ''
        self.skillBox4.skillOption1 = 'Magic Defense'
        self.skillBox4.skillOption2 = 'Earth Resist'
        self.skillBox4.TextOption1 = 'M. Defense: {}'.format(rpg.player.stats['Magic Defense'])
        self.skillBox4.ImageOption1 = pygame.image.load('Images\MagicDefense.png')
        self.skillBox4.TextOption2 = 'Earth Resist: {}'.format(rpg.player.stats['Earth Resist'])
        self.skillBox4.ImageOption2 = pygame.image.load('Images\EarthResist.png')

        self.skillBox5 = buildingBlocks(rpg)
        self.skillBox5.width, self.skillBox5.height = 325, 70
        self.skillBox5.left, self.skillBox5.top = 80, 650
        self.skillBox5.font = pygame.font.SysFont('cambria', 30)
        self.skillBox5.msg_image_rect.top = 665
        txtCenterFunction(self.skillBox5, self.skillBox5.msg_image_rect, self.skillBox5.txt, self.skillBox5.font)
        self.skillBox5.border = True
        self.skillBox5.skill = ''
        self.skillBox5.skillOption1 = 'Physical Penetration'
        self.skillBox5.skillOption2 = 'Fire Resist'
        self.skillBox5.TextOption1 = 'P. Penetration: {}'.format(rpg.player.stats['Physical Penetration'])
        self.skillBox5.ImageOption1 = pygame.image.load('Images\ArmorPenetration.png')
        self.skillBox5.TextOption2 = 'Fire Resist: {}'.format(rpg.player.stats['Fire Resist'])
        self.skillBox5.ImageOption2 = pygame.image.load('Images\FireResist.png')

        self.skillBox6 = buildingBlocks(rpg)
        self.skillBox6.width, self.skillBox6.height = 325, 70
        self.skillBox6.left, self.skillBox6.top = 80, 720
        self.skillBox6.font = pygame.font.SysFont('cambria', 30)
        self.skillBox6.msg_image_rect.top = 735
        txtCenterFunction(self.skillBox6, self.skillBox6.msg_image_rect, self.skillBox6.txt, self.skillBox6.font)
        self.skillBox6.border = True
        self.skillBox6.skill = ''
        self.skillBox6.skillOption1 = 'Magic Penetration'
        self.skillBox6.skillOption2 = 'Poison Resist'
        self.skillBox6.TextOption1 = 'M. Penetration: {}'.format(rpg.player.stats['Magic Penetration'])
        self.skillBox6.ImageOption1 = pygame.image.load('Images\MagicPenetration.png')
        self.skillBox6.TextOption2 = 'Poison Resist: {}'.format(rpg.player.stats['Poison Resist'])
        self.skillBox6.ImageOption2 = pygame.image.load('Images\PoisonResist.png')

        self.skillBox7 = buildingBlocks(rpg)
        self.skillBox7.width, self.skillBox7.height = 325, 70
        self.skillBox7.left, self.skillBox7.top = 80, 790
        self.skillBox7.font = pygame.font.SysFont('cambria', 30)
        self.skillBox7.msg_image_rect.top = 805
        txtCenterFunction(self.skillBox7, self.skillBox7.msg_image_rect, self.skillBox7.txt, self.skillBox7.font)
        self.skillBox7.border = True
        self.skillBox7.skill = ''
        self.skillBox7.skillOption1 = 'Critical Chance'
        self.skillBox7.skillOption2 = 'Water Resist'
        self.skillBox7.TextOption1 = 'Crit Chance: {}'.format(rpg.player.stats['Critical Chance'])
        self.skillBox7.ImageOption1 = pygame.image.load('Images\CritChance.png')
        self.skillBox7.TextOption2 = 'Water Resist: {}'.format(rpg.player.stats['Water Resist'])
        self.skillBox7.ImageOption2 = pygame.image.load('Images\WaterResist.png')

        self.skillBox8 = buildingBlocks(rpg)
        self.skillBox8.width, self.skillBox8.height = 325, 70
        self.skillBox8.left, self.skillBox8.top = 80, 860
        self.skillBox8.font = pygame.font.SysFont('cambria', 30)
        self.skillBox8.msg_image_rect.top = 875
        txtCenterFunction(self.skillBox8, self.skillBox8.msg_image_rect, self.skillBox8.txt, self.skillBox8.font)
        self.skillBox8.border = True
        self.skillBox8.skill = ''
        self.skillBox8.skillOption1 = 'Critical Multiplier'
        self.skillBox8.skillOption2 = 'Wind Resist'
        self.skillBox8.TextOption1 = 'Crit Multi: {}'.format(rpg.player.stats['Critical Multiplier'])
        self.skillBox8.ImageOption1 = pygame.image.load('Images\CritMultiplier.png')
        self.skillBox8.TextOption2 = 'Wind Resist: {}'.format(rpg.player.stats['Wind Resist'])
        self.skillBox8.ImageOption2 = pygame.image.load('Images\WindResist.png')

        self.skillBox9 = buildingBlocks(rpg)
        self.skillBox9.width, self.skillBox9.height = 325, 70
        self.skillBox9.left, self.skillBox9.top = 80, 930
        self.skillBox9.font = pygame.font.SysFont('cambria', 30)
        self.skillBox9.msg_image_rect.top = 945
        txtCenterFunction(self.skillBox9, self.skillBox9.msg_image_rect, self.skillBox9.txt, self.skillBox9.font)
        self.skillBox9.border = True
        self.skillBox9.skill = ''
        self.skillBox9.skillOption1 = 'Luck'
        self.skillBox9.skillOption2 = ''
        self.skillBox9.TextOption1 = 'Luck: {}'.format(rpg.player.stats['Luck'])
        self.skillBox9.ImageOption1 = pygame.image.load('Images\Luck.png')
        self.skillBox9.TextOption2 = ""
        self.skillBox9.ImageOption2 = ""

        self.statDescriptor = buildingBlocks(rpg)
        self.statDescriptor.width, self.statDescriptor.height = 220, 260
        self.statDescriptor.left, self.statDescriptor.top = 500, 350
        self.statDescriptor.border = True

        self.statDescriptorTitle = buildingBlocks(rpg)
        self.statDescriptorTitle.width, self.statDescriptorTitle.height = 220, 60
        self.statDescriptorTitle.left, self.statDescriptorTitle.top = 500, 350
        self.statDescriptorTitle.font = pygame.font.SysFont('cambria', 20)
        self.statDescriptorTitle.font.set_underline(True)
        self.statDescriptorTitle.msg_image_rect.top = 370
        txtCenterFunction(self.statDescriptorTitle, self.statDescriptorTitle.msg_image_rect, self.statDescriptorTitle.txt, self.statDescriptorTitle.font)
        self.statDescriptorTitle.border = True

        self.statDescriptorLine1 = buildingBlocks(rpg)
        self.statDescriptorLine1.width, self.statDescriptorLine1.height = 220, 40
        self.statDescriptorLine1.left, self.statDescriptorLine1.top = 500, 410
        self.statDescriptorLine1.font = pygame.font.SysFont('cambria', 15)
        self.statDescriptorLine1.msg_image_rect.top = 420
        txtCenterFunction(self.statDescriptorLine1, self.statDescriptorLine1.msg_image_rect, self.statDescriptorLine1.txt, self.statDescriptorLine1.font)

        self.statDescriptorLine2 = buildingBlocks(rpg)
        self.statDescriptorLine2.width, self.statDescriptorLine2.height = 220, 40
        self.statDescriptorLine2.left, self.statDescriptorLine2.top = 500, 450
        self.statDescriptorLine2.font = pygame.font.SysFont('cambria', 15)
        self.statDescriptorLine2.msg_image_rect.top = 460
        txtCenterFunction(self.statDescriptorLine2, self.statDescriptorLine2.msg_image_rect, self.statDescriptorLine2.txt, self.statDescriptorLine2.font)

        self.statDescriptorLine3 = buildingBlocks(rpg)
        self.statDescriptorLine3.width, self.statDescriptorLine3.height = 220, 40
        self.statDescriptorLine3.left, self.statDescriptorLine3.top = 500, 490
        self.statDescriptorLine3.font = pygame.font.SysFont('cambria', 15)
        self.statDescriptorLine3.msg_image_rect.top = 500
        txtCenterFunction(self.statDescriptorLine3, self.statDescriptorLine3.msg_image_rect, self.statDescriptorLine3.txt, self.statDescriptorLine3.font)

        self.statDescriptorLine4 = buildingBlocks(rpg)
        self.statDescriptorLine4.width, self.statDescriptorLine4.height = 220, 40
        self.statDescriptorLine4.left, self.statDescriptorLine4.top = 500, 530
        self.statDescriptorLine4.font = pygame.font.SysFont('cambria', 15)
        self.statDescriptorLine4.msg_image_rect.top = 540
        txtCenterFunction(self.statDescriptorLine4, self.statDescriptorLine4.msg_image_rect, self.statDescriptorLine4.txt, self.statDescriptorLine4.font)

        self.statDescriptorLine5 = buildingBlocks(rpg)
        self.statDescriptorLine5.width, self.statDescriptorLine5.height = 220, 40
        self.statDescriptorLine5.left, self.statDescriptorLine5.top = 500, 570
        self.statDescriptorLine5.font = pygame.font.SysFont('cambria', 15)
        self.statDescriptorLine5.msg_image_rect.top = 580
        txtCenterFunction(self.statDescriptorLine5, self.statDescriptorLine5.msg_image_rect, self.statDescriptorLine5.txt, self.statDescriptorLine5.font)

        self.skillBoxList = [self.skillBox1, self.skillBox2, self.skillBox3, self.skillBox4,
        self.skillBox5, self.skillBox6, self.skillBox7, self.skillBox8, self.skillBox9]

        self.showDescriptor = False
        self.set = 0
    
    def update(self, rpg):
        self.name.txt = rpg.player.stats['Name']
        self.level.txt = "Level: {}".format(rpg.player.stats['Level'])
        self.exp.txt = "Exp: {}/{}".format(rpg.player.stats['Exp'], rpg.player.stats['Exp Cap'])
        self.occupation.txt = "{}".format(rpg.player.stats['Profession'])
        self.gold.txt = "Gold: {}".format(rpg.player.stats['Gold'])
        self.health.txt = "Health: {}/{}".format(rpg.player.stats['Hp'], rpg.player.stats['Max Hp'])
        self.mana.txt = "Mana: {}/{}".format(rpg.player.stats['Mana'], rpg.player.stats['Max Mana'])
        self.stamina.txt = "Stamina: {}/{}".format(rpg.player.stats['Stamina'], rpg.player.stats['Max Stamina'])
        self.skillPoints.txt = "Skill Points: {}".format(rpg.player.stats['Skill Points'])
        self.skillBox1.TextOption1 = 'Strength: {}'.format(rpg.player.stats['Physical Attack'])
        self.skillBox1.ImageOption1 = pygame.image.load('Images\Strength.png')
        self.skillBox1.TextOption2 = 'Agility: {}'.format(rpg.player.stats['Agility'])
        self.skillBox1.ImageOption2 = pygame.image.load('Images\Agility.png')
        self.skillBox2.TextOption1 = 'Intelligence: {}'.format(rpg.player.stats['Magic Attack'])
        self.skillBox2.ImageOption1 = pygame.image.load('Images\Intelligence.png')
        self.skillBox2.TextOption2 = 'Evasion: {}'.format(round(rpg.player.stats['Evasion'], 1))
        self.skillBox2.ImageOption2 = pygame.image.load('Images\Evasion.png')
        self.skillBox3.TextOption1 = 'P. Defense: {}'.format(rpg.player.stats['Physical Defense'])
        self.skillBox3.ImageOption1 = pygame.image.load('Images\PhysicalDefense.png')
        self.skillBox3.TextOption2 = 'Accuracy: {}'.format(round(rpg.player.stats['Accuracy'], 1))
        self.skillBox3.ImageOption2 = pygame.image.load('Images\Accuracy.png')
        self.skillBox4.TextOption1 = 'M. Defense: {}'.format(rpg.player.stats['Magic Defense'])
        self.skillBox4.ImageOption1 = pygame.image.load('Images\MagicDefense.png')
        self.skillBox4.TextOption2 = 'Earth Resist: {}'.format(rpg.player.stats['Earth Resist'])
        self.skillBox4.ImageOption2 = pygame.image.load('Images\EarthResist.png')
        self.skillBox5.TextOption1 = 'P. Penetration: {}'.format(rpg.player.stats['Physical Penetration'])
        self.skillBox5.ImageOption1 = pygame.image.load('Images\ArmorPenetration.png')
        self.skillBox5.TextOption2 = 'Fire Resist: {}'.format(rpg.player.stats['Fire Resist'])
        self.skillBox5.ImageOption2 = pygame.image.load('Images\FireResist.png')
        self.skillBox6.TextOption1 = 'M. Penetration: {}'.format(rpg.player.stats['Magic Penetration'])
        self.skillBox6.ImageOption1 = pygame.image.load('Images\MagicPenetration.png')
        self.skillBox6.TextOption2 = 'Poison Resist: {}'.format(rpg.player.stats['Poison Resist'])
        self.skillBox6.ImageOption2 = pygame.image.load('Images\PoisonResist.png')
        self.skillBox7.TextOption1 = 'Crit Chance: {}'.format(round(rpg.player.stats['Critical Chance']))
        self.skillBox7.ImageOption1 = pygame.image.load('Images\CritChance.png')
        self.skillBox7.TextOption2 = 'Water Resist: {}'.format(rpg.player.stats['Water Resist'])
        self.skillBox7.ImageOption2 = pygame.image.load('Images\WaterResist.png')
        self.skillBox8.TextOption1 = 'Crit Multi: {}'.format(round(rpg.player.stats['Critical Multiplier'], 1))
        self.skillBox8.ImageOption1 = pygame.image.load('Images\CritMultiplier.png')
        self.skillBox8.TextOption2 = 'Wind Resist: {}'.format(rpg.player.stats['Wind Resist'])
        self.skillBox8.ImageOption2 = pygame.image.load('Images\WindResist.png')
        self.skillBox9.TextOption1 = 'Luck: {}'.format(round(rpg.player.stats['Luck']))
        self.skillBox9.ImageOption1 = pygame.image.load('Images\Luck.png')
        self.skillBox9.TextOption2 = ""
        self.skillBox9.ImageOption2 = ""

        txtCenterFunction(self.name, self.name.msg_image_rect, self.name.txt, self.name.font)
        txtCenterFunction(self.level, self.level.msg_image_rect, self.level.txt, self.level.font)
        txtCenterFunction(self.exp, self.exp.msg_image_rect, self.exp.txt, self.exp.font)
        txtCenterFunction(self.occupation, self.occupation.msg_image_rect, self.occupation.txt, self.occupation.font)
        txtCenterFunction(self.gold, self.gold.msg_image_rect, self.gold.txt, self.gold.font)
        txtCenterFunction(self.health, self.health.msg_image_rect, self.health.txt, self.health.font)
        txtCenterFunction(self.mana, self.mana.msg_image_rect, self.mana.txt, self.mana.font)
        txtCenterFunction(self.stamina, self.stamina.msg_image_rect, self.stamina.txt, self.stamina.font)
        txtCenterFunction(self.skillPoints, self.skillPoints.msg_image_rect, self.skillPoints.txt, self.skillPoints.font)
        txtCenterFunction(self.skillBox1, self.skillBox1.msg_image_rect, self.skillBox1.txt, self.skillBox1.font)
        txtCenterFunction(self.skillBox2, self.skillBox2.msg_image_rect, self.skillBox2.txt, self.skillBox2.font)
        txtCenterFunction(self.skillBox3, self.skillBox3.msg_image_rect, self.skillBox3.txt, self.skillBox3.font)
        txtCenterFunction(self.skillBox4, self.skillBox4.msg_image_rect, self.skillBox4.txt, self.skillBox4.font)
        txtCenterFunction(self.skillBox5, self.skillBox5.msg_image_rect, self.skillBox5.txt, self.skillBox5.font)
        txtCenterFunction(self.skillBox6, self.skillBox6.msg_image_rect, self.skillBox6.txt, self.skillBox6.font)
        txtCenterFunction(self.skillBox7, self.skillBox7.msg_image_rect, self.skillBox7.txt, self.skillBox7.font)
        txtCenterFunction(self.skillBox8, self.skillBox8.msg_image_rect, self.skillBox8.txt, self.skillBox8.font)
        txtCenterFunction(self.skillBox9, self.skillBox9.msg_image_rect, self.skillBox9.txt, self.skillBox9.font)

        self.healthBar.width = self.healthBar.width * (rpg.player.stats['Max Hp'] // rpg.player.stats['Hp'])
        self.staminaBar.width = self.staminaBar.width * (rpg.player.stats['Max Stamina'] // rpg.player.stats['Stamina'])
        self.manaBar.width = self.manaBar.width * (rpg.player.stats['Max Mana'] // rpg.player.stats['Mana'])
        
        if self.healthBar.width > 265:
            self.healthBar.width = 265
        elif self.healthBar.width < 0:
            self.healthBar.width = 265
        if self.staminaBar.width > 265:
            self.staminaBar.width = 265
        elif self.staminaBar.width < 0:
            self.staminaBar.width = 265
        if self.manaBar.width > 265:
            self.manaBar.width = 265
        elif self.manaBar.width < 0:
            self.manaBar.width = 265
        
        for box in self.skillBoxList:
            txtCenterFunction(box, box.msg_image_rect, box.txt, box.font)
            if self.set == 0:
                box.txt = box.TextOption1
                box.image = box.ImageOption1
                box.skill = box.skillOption1
            else:
                box.txt = box.TextOption2
                box.image = box.ImageOption2
                box.skill = box.skillOption2
            if rpg.player.stats['Skill Points'] > 0:
                box.clickable = True
            else:
                box.clickable = False
                box.button_color = (0, 0, 0)
        
        mous_pos = pygame.mouse.get_pos()
        for box in self.skillBoxList:
            if box.rect.collidepoint(mous_pos):
                if box.txt != "":
                    self.showDescriptor = True

                    txtCenterFunction(self.statDescriptorTitle, self.statDescriptorTitle.msg_image_rect, self.statDescriptorTitle.txt, self.statDescriptorTitle.font)
                    self.statDescriptor.left, self.statDescriptor.top = box.left + 350, box.top - 200

                    self.statDescriptorTitle.left, self.statDescriptorTitle.top = self.statDescriptor.left, self.statDescriptor.top
                    self.statDescriptorTitle.msg_image_rect.top = self.statDescriptor.top + 20

                    self.statDescriptorLine1.left, self.statDescriptorLine1.top = self.statDescriptor.left, self.statDescriptorTitle.top + 60
                    txtCenterFunction(self.statDescriptorLine1, self.statDescriptorLine1.msg_image_rect, self.statDescriptorLine1.txt, self.statDescriptorLine1.font)
                    self.statDescriptorLine1.msg_image_rect.top = self.statDescriptorLine1.top + 10

                    self.statDescriptorLine2.left, self.statDescriptorLine2.top = self.statDescriptor.left, self.statDescriptorLine1.top + 40
                    txtCenterFunction(self.statDescriptorLine2, self.statDescriptorLine2.msg_image_rect, self.statDescriptorLine2.txt, self.statDescriptorLine2.font)
                    self.statDescriptorLine2.msg_image_rect.top = self.statDescriptorLine2.top + 10

                    self.statDescriptorLine3.left, self.statDescriptorLine3.top = self.statDescriptor.left, self.statDescriptorLine2.top + 40
                    txtCenterFunction(self.statDescriptorLine3, self.statDescriptorLine3.msg_image_rect, self.statDescriptorLine3.txt, self.statDescriptorLine3.font)
                    self.statDescriptorLine3.msg_image_rect.top = self.statDescriptorLine3.top + 10
                    
                    self.statDescriptorLine4.left, self.statDescriptorLine4.top = self.statDescriptor.left, self.statDescriptorLine3.top + 40
                    txtCenterFunction(self.statDescriptorLine4, self.statDescriptorLine4.msg_image_rect, self.statDescriptorLine4.txt, self.statDescriptorLine4.font)
                    self.statDescriptorLine4.msg_image_rect.top = self.statDescriptorLine4.top + 10

                    self.statDescriptorLine5.left, self.statDescriptorLine5.top = self.statDescriptor.left, self.statDescriptorLine4.top + 40
                    txtCenterFunction(self.statDescriptorLine5, self.statDescriptorLine5.msg_image_rect, self.statDescriptorLine5.txt, self.statDescriptorLine5.font)
                    self.statDescriptorLine5.msg_image_rect.top = self.statDescriptorLine5.top + 10

                    if box.skill == 'Physical Attack':
                        self.statDescriptorTitle.txt = "Strength"
                        self.statDescriptorLine1.txt = "Boosts attacks with melee weapons. This would've been useful when my sweetroll was taken :("
                    elif box.skill == "Magic Attack":
                        self.statDescriptorTitle.txt = "Intelligence"
                        self.statDescriptorLine1.txt = "Boosts any mana based attacks. Basically makes boom go bigger boom"
                    elif box.skill == "Physical Defense":
                        self.statDescriptorTitle.txt = "Physical Defense"
                        self.statDescriptorLine1.txt = "Reduces incoming melee damage. Though it'll nothing about the mental trauma"
                    elif box.skill == "Magic Defense":
                        self.statDescriptorTitle.txt = "Magic Defense"
                        self.statDescriptorLine1.txt = "Reduces incoming mana based damage. Again not the mental trauma, unfortunately"
                    elif box.skill == "Physical Penetration":
                        self.statDescriptorTitle.txt = "Physical Penetration"
                        self.statDescriptorLine1.txt = "Melee attacks ignore a perecentage of enemy armor. Reduces the resale of the armor tho"
                    elif box.skill == "Magic Penetration":
                        self.statDescriptorTitle.txt = "Magic Penetration"
                        self.statDescriptorLine1.txt = "Magic attacks ignore a perecentage of enemy's armor. Poor thing worked so hard for nothing"
                    elif box.skill == "Critical Chance":
                        self.statDescriptorTitle.txt = "Critical Chance"
                        self.statDescriptorLine1.txt = "Chance to land critical damage on an enemy. Best be praying to luck gods"
                    elif box.skill == "Critical Multiplier":
                        self.statDescriptorTitle.txt = "Critical Multiplier"
                        self.statDescriptorLine1.txt = "How much is multiplied to your attacks when criting. Just don't over do it champ"
                    elif box.skill == "Luck":
                        self.statDescriptorTitle.txt = "Luck"
                        self.statDescriptorLine1.txt = "Affects monster drops and various other things. Without it you'll get dirt for gold"
                    elif box.skill == "Agility":
                        self.statDescriptorTitle.txt = "Agility"
                        self.statDescriptorLine1.txt = "Affects initiative in battle. Also helps when you doing some cardio"
                    elif box.skill == "Evasion":
                        self.statDescriptorTitle.txt = "Evasion"
                        self.statDescriptorLine1.txt = "Reduces enemy's accuracy. Also really useful when you allegedly committed a \"crime\""
                    elif box.skill == "Accuracy":
                        self.statDescriptorTitle.txt = "Accuracy"
                        self.statDescriptorLine1.txt = "Affects the chance of you hitting the enemy. Or just get some glasses"
                    elif box.skill == "Earth Resist":
                        self.statDescriptorTitle.txt = "Earth Resistance"
                        self.statDescriptorLine1.txt = "Reduces the damage received from earth based attacks. Or learn earth bending and become a cool kid"
                    elif box.skill == "Fire Resist":
                        self.statDescriptorTitle.txt = "Fire Resistance"
                        self.statDescriptorLine1.txt = "Reduces the damage received from fire based attacks. Thank god for oven mits am I right?"
                    elif box.skill == "Poison Resist":
                        self.statDescriptorTitle.txt = "Poison Resistance"
                        self.statDescriptorLine1.txt = "Reduces the damage received from poison based attacks. But just make to sure, stand 6 feet apart from me"
                    elif box.skill == "Water Resist":
                        self.statDescriptorTitle.txt = "Water Resistance"
                        self.statDescriptorLine1.txt = "Reduces the damage received from water based attacks. Or just get good lol"
                    elif box.skill == "Wind Resist":
                        self.statDescriptorTitle.txt = "Wind Resistance"
                        self.statDescriptorLine1.txt = "Reduces the damage received from wind based attacks. That doesn't mean you don't have wear clothes tho"
                    self.statDescriptorLine1.txt, self.statDescriptorLine2.txt = txtSplitter(self.statDescriptorLine1, self.statDescriptorLine1.font, self.statDescriptorLine1.txt, 15)
                    self.statDescriptorLine2.txt, self.statDescriptorLine3.txt = txtSplitter(self.statDescriptorLine2, self.statDescriptorLine2.font, self.statDescriptorLine2.txt, 15)
                    self.statDescriptorLine3.txt, self.statDescriptorLine4.txt = txtSplitter(self.statDescriptorLine3, self.statDescriptorLine3.font, self.statDescriptorLine3.txt, 15)
                    self.statDescriptorLine4.txt, self.statDescriptorLine5.txt = txtSplitter(self.statDescriptorLine4, self.statDescriptorLine4.font, self.statDescriptorLine4.txt, 15)
                break
            else:
                self.showDescriptor = False
                    
    def mouseEvents(self, rpg, mous_pos):
        if rpg.player.stats['Skill Points'] > 0:
            for box in self.skillBoxList:
                if box.rect.collidepoint(mous_pos):
                    if box.skill == 'Critical Chance' or box.skill == 'Luck': 
                        rpg.player.stats[box.skill] += .5
                    elif box.skill == 'Critical Multiplier':
                        rpg.player.stats[box.skill] += .05
                    elif box.skill == 'Accuracy' or box.skill == 'Evasion':
                        rpg.player.stats[box.skill] += .2
                    else:
                        rpg.player.stats[box.skill] += 1
                    rpg.player.stats['Skill Points'] -= 1
                    break
        
        if self.scrollUp.rect.collidepoint(mous_pos):
            self.set -= 1
            if self.set < 0:
                self.set = 0
        if self.scrollDown.rect.collidepoint(mous_pos):
            self.set += 1
            if self.set > 1:
                self.set = 0


    def draw(self, rpg):
        self.update(rpg)

        self.mainBox.draw()
        self.iconBox.draw()
        self.infoBox.draw()
        
        self.name.draw()
        self.level.draw()
        self.exp.draw()
        self.occupation.draw()
        self.gold.draw()
        
        self.healthBar.draw()
        self.staminaBar.draw()
        self.manaBar.draw()
        self.health.draw()
        self.mana.draw()
        self.stamina.draw()
        
        self.skillPoints.draw()
        self.scrollUp.draw()
        self.scrollDown.draw()
        
        self.skillBox1.draw()
        self.skillBox2.draw()
        self.skillBox3.draw()
        self.skillBox4.draw()
        self.skillBox5.draw()
        self.skillBox6.draw()
        self.skillBox7.draw()
        self.skillBox8.draw()
        self.skillBox9.draw()

        if self.showDescriptor == True:
            self.statDescriptor.draw()
            self.statDescriptorTitle.draw()
            self.statDescriptorLine1.draw()
            self.statDescriptorLine2.draw()
            self.statDescriptorLine3.draw()
            self.statDescriptorLine4.draw()
            self.statDescriptorLine5.draw()

