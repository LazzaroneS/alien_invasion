import sys

import pygame

class AlienInvasion:
    """AlienInvasion is created for manage resources and action of the game"""
    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Main loop of the beginning game."""
        while True:
            # Monitor of keyboard and mouse.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            # Make the recently depicted screen visible.
            pygame.display.flip()
            
if __name__ == '__main__':
    # Create a instance of the game and run it.
    ai = AlienInvasion()
    ai.run_game()