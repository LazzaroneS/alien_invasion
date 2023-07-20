import pygame

class Ship:
    """Ship is responsible for the management of spacecraft."""
    def __init__(self, ai_game):
        """Initialize ship and set its initial location."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # load the ship image and retrieve its bounding rectangle
        self.image = pygame.image.load('image/redfighter0005.png')
        self.rect = self.image.get_rect()
        
        # Each new ship is situated at the central bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """Drawing the ship at the designated location."""
        self.screen.blit(self.image, self.rect)