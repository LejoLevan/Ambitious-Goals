"""Contains function that searches for an image
based on file name"""

import pygame

from Images.PlayerAssets.playerSearchUp import playerSearchUp

def searchUp(filename):
    """calls different functions hidden in image folders with file name"""
    try:
        image = playerSearchUp(filename)
    except:
        try:
            pass
        except:
            pass
    
    try:
        return(image)
    except:
        pass