import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """AlienInvasion is created for manage resources and action of the game"""
    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # set background color
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        """Main loop of the beginning game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Responding to key and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Response for keydown"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Response for release"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
                
    def _update_screen(self):
        """update images on the screen and swich to new screen"""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        
        pygame.display.flip()
        
            
if __name__ == '__main__':
    # Create a instance of the game and run it.
    ai = AlienInvasion()
    ai.run_game()