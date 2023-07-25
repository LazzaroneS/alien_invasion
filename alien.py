import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Indicating a single alien"""
    
    def __init__(self, ai_game):
        """initialize a alien and give it a position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # load the alien image and set rect attribute
        self.image = pygame.image.load('images/alien001.png')
        self.rect = self.image.get_rect()
        
        # Every alien initially resides in the upper left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the position of the alien
        self.x = float(self.rect.x)

    def update(self):
        """The fleet is to be moved towards the right."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """If an alien moves to the edge of the screen, then return True."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)