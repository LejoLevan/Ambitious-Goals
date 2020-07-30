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

def holdUp(rpg):
    clicked = False
    while clicked == False:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mous_pos = pygame.mouse.get_pos()
                if rpg.dialogueBlock.dialogueBlock.rect.collidepoint(mous_pos):
                    clicked = True