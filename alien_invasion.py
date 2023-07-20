import sys

import pygame

from settings import Settings

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

        # set background color
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        """Main loop of the beginning game."""
        while True:
            # Monitor of keyboard and mouse.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redrawing screen in every loop
            self.screen.fill(self.bg_color)
                    
            # Make the recently depicted screen visible.
            pygame.display.flip()
            self.clock.tick(60)
            
if __name__ == '__main__':
    # Create a instance of the game and run it.
    ai = AlienInvasion()
    ai.run_game()