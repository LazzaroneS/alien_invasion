import pygame.font

class Button:
    """Create button"""
    
    def __init__(self, ai_game, msg):
        """Initialize the button's attribute."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Adjust the dimensions and augment other attributes of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Create a rect object of the button, place it on the center of the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # label should be created only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """render text to image and place it to the center."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Create a button that is imbued with colors, and proceed to draw the text upon it."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)