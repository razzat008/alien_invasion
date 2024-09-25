import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, aigame):
        super().__init__()
        self.screen = aigame.screen
        self.settings = aigame.settings
        alien_image = pygame.image.load("./media/alien.png")
        self.image = pygame.transform.scale(alien_image, (85, 90))

        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # alien's horizontal position
        self.x = float(self.rect.x)

    def update(self):
        # screen starts at 0,0 from top left
        self.x += self.settings.bullet_speed
        # update the position of the bullet
        self.rect.y = self.y

    """Drawing aliens"""

    # def draw_alien(self):
