import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """Indicating a star."""

    def __init__(self, ai_game):
        """Initialize a star and give it a position."""
        super().__init__()
        self.screen = ai_game.screen
        
        # load the star image
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        # Every star initially resides in the upper left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the position of the star
        self.x = float(self.rect.x)