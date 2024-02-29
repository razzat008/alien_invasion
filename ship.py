import pygame


class Ship:
    def __init__(self, aigame):
        self.screen = aigame.screen
        self.screen_rect = aigame.screen.get_rect()
        self.settings = aigame.settings

        # self.image = pygame.image.load_basic('images/ship.bmp')
        picture = pygame.image.load_basic('images/ship.bmp')
        self.image = pygame.transform.scale(
            picture, (100, 150))  # to scale the image
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # movement flag for continuous movement
        self.movingright = False
        self.movingleft = False
        self.movingup = False
        self.movingdown = False
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        # to not let the rocket pass the visible screen
        if self.movingright and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        elif self.movingleft and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        elif self.movingup and self.screen_rect.top < self.rect.top:
            self.y -= self.settings.ship_speed

        elif self.movingdown and self.screen_rect.bottom > self.rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
