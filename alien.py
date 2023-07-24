import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Indicating a single alien"""
    
    def __init__(self, ai_game):
        """initialize a alien and give it a position"""
        super().__init__()
        self.screen = ai_game.screen
        
        # load the alien image and set rect attribute
        self.image = pygame.image.load('images/alien001.png')
        self.rect = self.image.get_rect()
        
        # Every alien initially resides in the upper left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the position of the alien
        self.x = float(self.rect.x)