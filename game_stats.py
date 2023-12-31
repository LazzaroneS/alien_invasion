class GameStats:
    """Tracking game statistics."""
    
    def __init__(self, ai_game):
        """Initialize statistics info."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Under no circumstances should the highest score be reset.
        self.high_score = 0
        
    def reset_stats(self):
        """Initialize the statistical infomation that may vary furing the runtime of the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1