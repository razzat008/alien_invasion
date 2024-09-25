import pygame


class Ship:
    def __init__(self, aigame):
        self.screen = aigame.screen
        self.screen_rect = aigame.screen.get_rect()
        self.settings = aigame.settings

        # self.image = pygame.image.load_basic('images/ship.bmp')
        picture = pygame.image.load_basic('media/ship.bmp')
        self.image = pygame.transform.scale(
            picture, (75, 100))  # to scale the image
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # store decimal value for the ships horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # for continuous movement of the ship (movement flags)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.speed = self.settings.ship_speed

    def update(self):
        """update the ship's position based on movement flags"""
        # update ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.speed
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            """self.rect.bottom is lower boundary of the game screen &
            self.screen_rect.bottom is the position of the
            lower end of the ship"""
            self.y += self.speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
