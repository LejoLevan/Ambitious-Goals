"""Contains function that searchs for an image within this folder"""
import pygame

def playerSearchUp(filename):
    """Function searches for image within Player Assets folder"""
    try:
        return(pygame.image.load(".jpg", namehint = filename))
    except:
        pass