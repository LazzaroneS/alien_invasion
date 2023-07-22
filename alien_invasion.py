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
        
        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height
        ))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # set background color
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        """Main loop of the beginning game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Responding to key and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

                
    def _update_screen(self):
        """update images on the screen and swich to new screen"""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        
        pygame.display.flip()
        
            
if __name__ == '__main__':
    # Create a instance of the game and run it.
    ai = AlienInvasion()
    ai.run_game()