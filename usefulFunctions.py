"""A file simply to hold useful functions for me to use while developing
    this game
"""
import sys

import pygame
import time
import math

from Images.searchUp import searchUp

# pylint: disable=invalid-name


def playerInteract(choices, rpg):
    """Useful function that controls the gui so that the player can interact with 
        the game

    Args:
        choices (List): list of choices
        rpg: variable containing the entire game
    """
    
    multiplePage = False
    choicesDone = False
    Slot1 = False
    Slot2 = False
    Slot3 = False
    Slot4 = False
    Slot5 = False

    choiceSet = 0 
    choiceSetLimit = 0
    choiceSetLimit = math.ceil(len(choices) / 5)

    rpg.dialogueBlock.txtSlot1.clickable = True
    rpg.dialogueBlock.txtSlot2.clickable = True
    rpg.dialogueBlock.txtSlot3.clickable = True
    rpg.dialogueBlock.txtSlot4.clickable = True
    rpg.dialogueBlock.txtSlot5.clickable = True


    if choiceSetLimit > 1:
        multiplePage = True

    while choicesDone != True:
        try:
            rpg.dialogueBlock.txtSlot1.txt = choices[choiceSet]
        except:
            rpg.dialogueBlock.txtSlot1.txt = ""
        try:
            rpg.dialogueBlock.txtSlot2.txt = choices[choiceSet + 1]
        except:
            rpg.dialogueBlock.txtSlot2.txt = ""
        try:
            rpg.dialogueBlock.txtSlot3.txt = choices[choiceSet + 2]
        except:
            rpg.dialogueBlock.txtSlot3.txt = ""
        try:
            rpg.dialogueBlock.txtSlot4.txt = choices[choiceSet + 3]
        except:
            rpg.dialogueBlock.txtSlot4.txt = ""
           
        if multiplePage == False:
            try:
                rpg.dialogueBlock.txtSlot5.txt = choices[choiceSet + 4]
            except:
                rpg.dialogueBlock.txtSlot5.txt = ""
        else:
            if rpg.dialogueBlock.txtSlot1.txt == "":
                rpg.dialogueBlock.txtSlot1.txt = "{}.) More Options".format(choiceSet + 1)
                Slot1 = True
            elif rpg.dialogueBlock.txtSlot2.txt == "":
                rpg.dialogueBlock.txtSlot2.txt = "{}.) More Options".format(choiceSet + 2)
                Slot2 = True
            elif rpg.dialogueBlock.txtSlot3.txt == "":
                rpg.dialogueBlock.txtSlot3.txt = "{}.) More Options".format(choiceSet + 3)
                Slot3 = True
            elif rpg.dialogueBlock.txtSlot4.txt == "":
                rpg.dialogueBlock.txtSlot4.txt = "{}.) More Options".format(choiceSet + 4)
                Slot4 = True
            elif rpg.dialogueBlock.txtSlot5.txt == "":
                rpg.dialogueBlock.txtSlot5.txt = "{}.) More Options".format(choiceSet + 5)
                Slot5 = True
    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                mous_pos = pygame.mouse.get_pos()
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    choiceSet += 4
                    if choiceSet >= (choiceSetLimit * 4):
                        choiceSet = 0
                    rpg.dialogueBlock.wipe()
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    choiceSet -= 4
                    if choiceSet < 0:
                        choiceSet = 0
                    rpg.dialogueBlock.wipe()
               

            if event.type == pygame.MOUSEBUTTONDOWN:
                mous_pos = pygame.mouse.get_pos()
                if rpg.dialogueBlock.txtSlot1.rect.collidepoint(mous_pos):
                    if Slot1 == False:
                        if rpg.dialogueBlock.txtSlot1.txt != "":
                            choicesDone = True
                            returnNum = choiceSet + 1
                    else:
                        choiceSet += 4
                        if choiceSet >= (choiceSetLimit * 4):
                            choiceSet = 0
                        rpg.dialogueBlock.wipe()
                elif rpg.dialogueBlock.txtSlot2.rect.collidepoint(mous_pos):
                    if Slot2 == False:
                        if rpg.dialogueBlock.txtSlot2.txt != "":
                            choicesDone = True
                            returnNum = choiceSet + 2
                    else:
                        choiceSet += 4
                        if choiceSet >= (choiceSetLimit * 4):
                            choiceSet = 0
                        rpg.dialogueBlock.wipe()
                elif rpg.dialogueBlock.txtSlot3.rect.collidepoint(mous_pos):
                    if Slot3 == False:
                        if rpg.dialogueBlock.txtSlot3.txt != "":
                            choicesDone = True
                            returnNum = choiceSet + 3
                    else:
                        choiceSet += 4
                        if choiceSet >= (choiceSetLimit * 4):
                            choiceSet = 0
                        rpg.dialogueBlock.wipe()
                elif rpg.dialogueBlock.txtSlot4.rect.collidepoint(mous_pos):
                    if Slot4 == False:
                        if rpg.dialogueBlock.txtSlot5.txt != "":
                            choicesDone = True
                            returnNum = choiceSet + 4
                    else:
                        choiceSet += 4
                        if choiceSet >= (choiceSetLimit * 4):
                            choiceSet = 0
                        rpg.dialogueBlock.wipe()
                elif rpg.dialogueBlock.txtSlot5.rect.collidepoint(mous_pos):
                    if Slot5 == False:
                        if rpg.dialogueBlock.txtSlot5.txt != "":
                            choicesDone = True
                            returnNum = choiceSet + 5
                    else:
                        choiceSet += 4
                        if choiceSet >= (choiceSetLimit * 4):
                            choiceSet = 0
                        rpg.dialogueBlock.wipe()
            
        rpg._update_screen()

    rpg.dialogueBlock.wipe()
    rpg.dialogueBlock.txtSlot1.clickable = False
    rpg.dialogueBlock.txtSlot1.button_color = (0, 0, 0)
    rpg.dialogueBlock.txtSlot2.clickable = False
    rpg.dialogueBlock.txtSlot2.button_color = (0, 0, 0)
    rpg.dialogueBlock.txtSlot3.clickable = False
    rpg.dialogueBlock.txtSlot3.button_color = (0, 0, 0)
    rpg.dialogueBlock.txtSlot4.clickable = False
    rpg.dialogueBlock.txtSlot4.button_color = (0, 0, 0)
    rpg.dialogueBlock.txtSlot5.clickable = False
    rpg.dialogueBlock.txtSlot5.button_color = (0, 0, 0)
    
    #return(returnNum)


def interactResults(results, choices, rpg):
    #slotClicked = playerInteract(choices, rpg)
    #results[slotClicked]
    pass


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
    """Useful function whenever I need a npc to talk to the player

    Args:
        rpg: variable containing the entire game
        dialogue (string): whatever the npc is going to say
    """
    flagDone = False
    line1 = dialogue

    rpg.dialogueBlock.txtSlot1.msg_image_rect.top, rpg.dialogueBlock.txtSlot1.msg_image_rect.left = 683.85, 720
    rpg.dialogueBlock.txtSlot2.msg_image_rect.top, rpg.dialogueBlock.txtSlot2.msg_image_rect.left = 769.55, 720
    rpg.dialogueBlock.txtSlot3.msg_image_rect.top, rpg.dialogueBlock.txtSlot3.msg_image_rect.left = 853.25, 720
    rpg.dialogueBlock.txtSlot4.msg_image_rect.top, rpg.dialogueBlock.txtSlot4.msg_image_rect.left = 936.95, 720
    rpg.dialogueBlock.txtSlot5.msg_image_rect.top, rpg.dialogueBlock.txtSlot5.msg_image_rect.left = 1020.65, 720

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
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                rpg.settings.txtSpeed = .055
            elif  event.type == pygame.KEYUP:
                rpg.settings.txtSpeed = .1
        time.sleep(rpg.settings.txtSpeed)
        i += 1

def holdUp(rpg):
    """Useful function for whenever I need the game to freeze

    Args:
        rpg: variable containing the entire game
    """
    clicked = False
    while clicked == False:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mous_pos = pygame.mouse.get_pos()
                if rpg.dialogueBlock.dialogueBlock.rect.collidepoint(mous_pos):
                    clicked = True

def txtCenterFunction(Object, txtObject, Text, font):
    subtractive = font.size(Text)[0] / 2
    txtObject.left = (Object.left + (Object.width / 2)) - subtractive