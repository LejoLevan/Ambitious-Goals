"""main file, contains the main class"""

import sys
import pygame

from settings import Settings
from Images.searchUp import searchUp
from gui import dialogueBlock
from usefulFunctions import speak

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

        self.dialogueBlock = dialogueBlock(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
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
        
    def _check_keydown_events(self, event):
        """Method checks what button on the keyboard was pressed

        Args:
            event (Unclear): basically what key was pressed
        """
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_w:
            speak(self, "Hi my name is billy bob joe, and you may ask who tf is billy bob joe? And I say...don't swear at me meanine :( that's mean. Btw the grammar in this string is terrible just plain terrible terrible enough that a english teacher might have a heart attack :P which is kinda cool to be fair. Welp I gotta type so more stuff cuz just copy and pasting doesn't help me at all in fact I'm just confused as confused as confusion which is pokemon move. And guess what it's me again to test another thing cuz apparenlty ddfdfejwip. Whoops feel asleep or did I? I dunnoq")

    def _update_screen(self):
        """Method updates screen"""
        self.screen.fill(self.settings.bg_color)
        if not self.game_active:
            self.dialogueBlock.draw()
        else:
            pass
        pygame.display.flip()

if __name__ == '__main__':
    game = RPG()
    game.run_game()