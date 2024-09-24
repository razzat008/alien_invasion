import sys

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:

    movement_keys = {
        (pygame.K_RIGHT, pygame.K_l): "moving_right",
        (pygame.K_LEFT, pygame.K_h): "moving_left",
        (pygame.K_UP, pygame.K_k): "moving_up",
        (pygame.K_DOWN, pygame.K_j): "moving_down",
    }

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        """to make the game fullscreen"""
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        self.bg_color = self.settings.bg_color
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

    def _update_screen(self):
        """update screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def fire_bullets(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _check_events(self):
        """Respond to keypress and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_down_events(event)
            elif event.type == pygame.KEYUP:
                self._check_up_events(event)

    def _check_down_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullets()
        for keys, attr in self.movement_keys.items():
            for key in keys:
                if event.key == key:
                    setattr(self.ship, attr, True)
                    break

    def _check_up_events(self, event):
        for keys, attr in self.movement_keys.items():
            for key in keys:
                if event.key == key:
                    setattr(self.ship, attr, False)
                    break


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
