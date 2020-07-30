"""contains settings class"""

class Settings: # pylint: disable=too-few-public-methods
    """A class to store all settings for game"""
    def __init__(self):
        """Initialize the game's settings"""
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (0, 0, 0)