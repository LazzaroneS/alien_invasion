import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Manage bullets"""
    def __init__(self, ai_game):
        """Create a bullet instance at ship's position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # Create a rectangular representing a bullet at (0, 0)
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position
        self.y = float(self.rect.y)

    def update(self):
        """Move up the bullet"""
        # Reposition of the bullet
        self.y -= self.settings.Bullet_speed
        # Repositon of the bullet's rect 
        self.rect.y  = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)