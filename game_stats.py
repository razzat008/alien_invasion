import pygame


class GameStats:
    """Statistics for the game"""

    def __init__(self, aigame):
        self.settings = aigame.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Initialize reset status"""
        self.ships_left = self.settings.ships_limit
