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

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        # checking if the fleet is still bounded
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        # moving the fleets left& right
        self.x += (self.settings.alien_speed*self.settings.fleet_direction)
        self.rect.x = self.x
