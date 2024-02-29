import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, aigame):
        super().__init__()
        self.screen = aigame.screen
        self.settings = aigame.settings
        self.color = self.settings.bullet_color

        # create a bullet rect at (0,0) and then set current position
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = aigame.ship.rect.midtop

        self.y = float(self.rect.y)

    def update_bullet(self):
        """move the bullet up the screen"""
        self.y -= self.settings.bullet_speed

        # update the position of the bullet
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet"""
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)
