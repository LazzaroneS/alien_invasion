import pygame.font

class Scoreboard:
    """Display score info."""
    
    def __init__(self, ai_game):
        """The initialization of these parameter that is relevant to display score."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings used to display score info
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare image of initialized score
        self.prep_score()

    def prep_score(self):
        """Render score into image."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, 
            self.text_color, 
            self.settings.bg_color
            )

        # Display score at top right corner.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def show_score(self):
        """Display score on the screen."""
        self.screen_blit(self.score_image, self.score_rect)
        