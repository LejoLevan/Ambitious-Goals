"""This file contains classes and function 
making up the game's gui"""

import pygame
import time
import sys

from Images.searchUp import searchUp

# pylint: disable=invalid-name

def txtSplitter(Object, font, txt, fontSize):
    """Useful function for whenever the player or an npc speaks

    Args:
        Object: the surface the txt is printed on
        font: pygame stuff 
        txt (string): txt to be split
        fontSize (number): Size of the font
    """    
    
    txtSize = font.size(txt)

    sentence1 =  txt.split()
    sentence2 = []

    while txtSize[0] > Object.width - (fontSize + (Object.msg_image_rect.left - Object.left)):
        sentence2.insert(0, sentence1.pop())
        txtSize = font.size(" ".join(sentence1))
    
    return(" ".join(sentence1), " ".join(sentence2))

def speak(rpg, dialogue):
    flagDone = False
    line1 = dialogue

    rpg.dialogueBlock.iconBlock.image = pygame.image.load("Images\PlayerAssets\Pikachu.jpg")

    while flagDone == False:
        line1, line2 = txtSplitter(rpg.dialogueBlock.txtSlot1, rpg.dialogueBlock.txtSlot1.font, line1, 20)
        line2, line3 = txtSplitter(rpg.dialogueBlock.txtSlot2, rpg.dialogueBlock.txtSlot2.font, line2, 20)
        line3, line4 = txtSplitter(rpg.dialogueBlock.txtSlot3, rpg.dialogueBlock.txtSlot3.font, line3, 20)
        line4, line5 = txtSplitter(rpg.dialogueBlock.txtSlot4, rpg.dialogueBlock.txtSlot4.font, line4, 20)
        line5, line6 = txtSplitter(rpg.dialogueBlock.txtSlot5, rpg.dialogueBlock.txtSlot5.font, line5, 20)


        dialogueSplitter(rpg, rpg.dialogueBlock.txtSlot1, line1.split())
        dialogueSplitter(rpg, rpg.dialogueBlock.txtSlot2, line2.split())
        dialogueSplitter(rpg, rpg.dialogueBlock.txtSlot3, line3.split())
        dialogueSplitter(rpg, rpg.dialogueBlock.txtSlot4, line4.split())
        dialogueSplitter(rpg, rpg.dialogueBlock.txtSlot5, line5.split())

        if line6 != "":
            line1 = line6
            holdUp(rpg)
            rpg.dialogueBlock.wipe()
            continue
        
        flagDone = True
    
    holdUp(rpg)
    rpg.dialogueBlock.wipe()

    

def dialogueSplitter(rpg, txtSlot, dialogue):
    """Gets the text to display gradually (one at  a time) which is more akin to a real rpg

    Args:
        rpg: Used to get methods recorded in the variable
        txtSlot: What object's text is being modified
        dialogue (list): List filled with strings
    """
    i = 0
    templist = []
    tempNum = len(dialogue)

    while i != tempNum:
        templist.insert(i, dialogue.pop(0))
        txtSlot.txt = " ".join(templist)
        rpg._update_screen()
        time.sleep(.055)
        i += 1



#Note when coming back: Make the while statement into a function 




"""^^ Notes for me :D : keeps spitting out lines (10 until user has to click for more). If statement at the end that calls the function again until no more 

needs split() and join() for if

https://stackoverflow.com/questions/3627270/python-how-exactly-can-you-take-a-string-split-it-reverse-it-and-join-it-back"""

def holdUp(rpg):
    clicked = False
    while clicked == False:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mous_pos = pygame.mouse.get_pos()
                if rpg.dialogueBlock.dialogueBlock.rect.collidepoint(mous_pos):
                    clicked = True

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
