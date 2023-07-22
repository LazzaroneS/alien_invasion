import pygame

class Ship:
    """Ship is responsible for the management of spacecraft."""
    def __init__(self, ai_game):
        """Initialize ship and set its initial location."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        # load the ship image and retrieve its bounding rectangle
        self.image = pygame.image.load('images/redfighter0005.png')
        self.rect = self.image.get_rect()
        
        # Each new ship is situated at the central bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float number in the attribute x of the ship
        self.x = float(self.rect.x)

        # Moving sign(Do not move initially)
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Reposition of the ship in accordance with the moving sign."""
        # update the ship's x value instead of the rect object's x value.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update object 'rect' in accordance with self.x
        self.rect.x = self.x
        
    def blitme(self):
        """Drawing the ship at the designated location."""
        self.screen.blit(self.image, self.rect)