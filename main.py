"""main file, contains the main class"""

import sys
import pygame

from settings import Settings
from Images.searchUp import searchUp
from gui import dialogueBlock, optionMenu, Inventory, playerStats, combatGUI
from usefulFunctions import speak, playerInteract
from player import player
from combatFunctions import combatFunction
class RPG:
    """Overall class to mangage game assets and behavior."""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode([self.settings.screen_width, self.settings.screen_height], pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Ambitious Goals!!")

        self.game_active = False
        self.menuOpen = False
        self.inventoryOpen = False
        self.statsOpen = False
        self.combatOpen = False
        self.showDialogueBlock = False

        self.player = player()
        self.dialogueBlock = dialogueBlock(self)
        self.optionMenu = optionMenu(self)
        self.Inventory = Inventory(self)
        self.statSheet = playerStats(self)
        self.combatGUI = combatGUI(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            if self.game_active:
                pass
            self._update_screen()
    
    def run_game_withoutloop(self):
        """Start the main loop for the game"""
        self._check_events()
        if self.game_active:
            pass
        self._update_screen()

    def _check_events(self):
        """Method checks for player inputs"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mous_pos = pygame.mouse.get_pos()
                self._check_mouseclick(mous_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_mouseclick(self, mous_pos):
        """Method checks what object was clicked on

        Args:
            mous_pos (Integer): x and y positions of the mouse
        """   
        if self.menuOpen == True:
            self.optionMenu.mouseEvents(self, mous_pos)
        if self.inventoryOpen == True:
            self.Inventory.mouseEvents(mous_pos)
        if self.statsOpen == True:
            self.statSheet.mouseEvents(self, mous_pos)
        
    def _check_keydown_events(self, event):
        """Method checks what button on the keyboard was pressed

        Args:
            event (Unclear): basically what key was pressed
        """
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_w:
            self.player.stats['Weapon'] = self.player.inventory['Weapons']['Iron Sword']
            self.combatOpen = True
            combatFunction(self)
        elif event.key == pygame.K_z:
            speak(self, 'Images\Medusa.png', "Yacky is not a yacky yack yack. In yack he's a back yack. Trees are green, leaves are black. and tea is green. Daren is a guy who is a thiccccc panda, and Jason is a gril who likes ot eat cheese nuggets of weed. Weed is green and tree's are black which means happy thoughts for green treees. Yackerty is backer jtdlkadjsafkl;j;slkfjasf;dlkjfa;slkfjcxzvnm,ndudwuriuqwepurio. Treees are wacky wack.")
            things = ["1.) Aye Sir", "2.) I dunno", "3.) What in tarnation", "4.) How quant", "5.) Lalala", "6.) Allo"]
            playerInteract(things, self)
        elif event.key == pygame.K_ESCAPE:
            while self.optionMenu.stopLoop == False:
                self.menuOpen = True
                self._check_events()
                self._update_screen()
            self.menuOpen = False
            self.optionMenu.stopLoop = False
        elif event.key == pygame.K_TAB:
            if self.inventoryOpen == False:
                self.inventoryOpen = True
            else:
                self.inventoryOpen = False
        elif event.key == pygame.K_c:
            if self.statsOpen == False:
                self.statsOpen = True
            else:
                self.statsOpen = False
        if self.menuOpen == True:   
            self.optionMenu.keyEvents(event)

    def _update_screen(self):
        """Method updates screen"""
        self.screen.fill(self.settings.bg_color)
        if not self.game_active:
            pass
        else:
            pass
        if self.combatOpen == True:
            self.combatGUI.draw(self)
        if self.inventoryOpen == True:
            self.Inventory.draw(self)
        if self.statsOpen == True:
            self.statSheet.draw(self)
        if self.menuOpen == True:
            self.optionMenu.draw()
        if self.showDialogueBlock == True:
            self.dialogueBlock.draw()
        pygame.display.flip()

if __name__ == '__main__':
    game = RPG()
    game.run_game()