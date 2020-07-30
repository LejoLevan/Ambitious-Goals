"""This file contains classes and function 
making up the game's gui"""

import pygame
import time
import sys

from Images.searchUp import searchUp

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
        if (self.clickable == True):
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.button_color = (200, 200, 200)
            else:
                self.button_color = (0, 0, 0)
        if self.transparent == False:
            self.screen.fill(self.button_color, self.rect)
        try:
            self.msg_image = self.font.render(self.txt, True, self.text_color)
            self.screen.blit(self.msg_image, self.msg_image_rect)
        except:
            pass
        try:
            #self.image = pygame.transform.scale(self.image, (self.width, self.height))
            self.screen.blit(self.image, self.rect)
        except:
            pass

class dialogueBlock:
    def __init__(self, rpg):
        self.dialogueBlock = buildingBlocks(rpg)

        self.dialogueBlock.width, self.dialogueBlock.height = 1917, 418.5
        self.dialogueBlock.top, self.dialogueBlock.left = 661.5, 1.5

        self.dialogueBlock.border = True


        self.iconBlock = buildingBlocks(rpg)

        self.iconBlock.width, self.iconBlock.height = 668.5, 418.5
        self.iconBlock.top, self.iconBlock.left = 661.5, 1.5

        self.iconBlock.border = True


        self.txtSlot1 = buildingBlocks(rpg)
        
        self.txtSlot1.txt = "Welcome young adventurer"

        self.txtSlot1.width, self.txtSlot1.height = 1248.5, 83.7
        self.txtSlot1.top, self.txtSlot1.left = 661.5, 670

        self.txtSlot1.msg_image_rect.top, self.txtSlot1.msg_image_rect.left = 683.85, 720

        self.txtSlot2 = buildingBlocks(rpg)

        self.txtSlot2.txt = "rise to the top of societ\""

        self.txtSlot2.width, self.txtSlot2.height = 1248.5, 83.7
        self.txtSlot2.top, self.txtSlot2.left = 745.2, 670

        self.txtSlot2.msg_image_rect.top, self.txtSlot2.msg_image_rect.left = 769.55, 720

        self.txtSlot3 = buildingBlocks(rpg)

        self.txtSlot3.txt = "rise to the top of society.\""

        self.txtSlot3.width, self.txtSlot3.height = 1248.5, 83.7
        self.txtSlot3.top, self.txtSlot3.left = 828.9, 670

        self.txtSlot3.msg_image_rect.top, self.txtSlot3.msg_image_rect.left = 853.25, 720

        self.txtSlot4 = buildingBlocks(rpg)

        self.txtSlot4.txt = "rise to the top of \""

        self.txtSlot4.width, self.txtSlot4.height = 1248.5, 83.7
        self.txtSlot4.top, self.txtSlot4.left = 912.6, 670

        self.txtSlot4.msg_image_rect.top, self.txtSlot4.msg_image_rect.left = 936.95, 720

        self.txtSlot5 = buildingBlocks(rpg)
        
        self.txtSlot5.txt = "rise to the top of \""

        self.txtSlot5.width, self.txtSlot5.height = 1248.5, 83.7
        self.txtSlot5.top, self.txtSlot5.left = 996.3, 670

        self.txtSlot5.msg_image_rect.top, self.txtSlot5.msg_image_rect.left = 1020.65, 720
    
    def wipe(self):
        self.txtSlot1.txt = ""
        self.txtSlot2.txt = ""
        self.txtSlot3.txt = ""
        self.txtSlot4.txt = ""
        self.txtSlot5.txt = ""
    
    def fitImage(self):
        

        if self.iconBlock.image.get_rect()[0] > 418.5:
            pass
        
        if self.iconBlock.image.get_rect()[1] > 668.5:
            pass

    def draw(self):
        self.dialogueBlock.draw()
        self.iconBlock.draw()
        self.txtSlot1.draw()
        self.txtSlot2.draw()
        self.txtSlot3.draw()
        self.txtSlot4.draw()
        self.txtSlot5.draw()
