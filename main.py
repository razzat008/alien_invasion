import sys

import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()
        x = self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (x.screen_width, x.screen_height))

        self.bg_color = x.bg_color
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _update_screen(self):
        """update screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

    def _check_events(self):
        """Respond to keypressess and mouse events"""
        for event in pygame.event.get():
            if pygame.display.get_focused():
                print("Window has focus")
            else:
                print("Window does not have focus")
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_down_events(event)

            elif event.type == pygame.KEYUP:
                self._check_up_events(event)

    def _check_down_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.x += self.

    def _check_up_events(self, event):


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
