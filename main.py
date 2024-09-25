import sys

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """For movement"""
    movement_keys = {
        (pygame.K_RIGHT, pygame.K_l): "moving_right",
        (pygame.K_LEFT, pygame.K_h): "moving_left",
        (pygame.K_UP, pygame.K_k): "moving_up",
        (pygame.K_DOWN, pygame.K_j): "moving_down",
    }

    """All initializations"""

    def __init__(self):

        pygame.init()
        self.settings = Settings()
        # to make the game fullscreen
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        self.bg_color = self.settings.bg_color
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        """Grouping sprites"""

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def _create_fleet(self):
        """For creating fleet of aliens"""
        alien = Alien(self)
        alien_width = alien.rect.width
        avaliable_space_horiz = self.settings.screen_width - \
            (2*alien_width)  # checking for available space in the screen

        # no of aliens that can fit in the screen (accounting for margins too)
        number_of_aliens = avaliable_space_horiz // (2*alien_width)

        for alien_number in range(number_of_aliens):
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)

    """The infinite loop"""

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    """For updating bullets position"""

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            print(f"Bullets remaining: {len(self.bullets)}")

    """Updating screen"""

    def _update_screen(self):
        """update screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()

    """Firing bullets"""

    def fire_bullets(self):
        # allow limited bullets only
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    """Check for keypresses"""

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
        elif event.key == (pygame.K_SPACE):
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
