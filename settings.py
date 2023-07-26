class Settings:
    """Settings is used for storing all settings in <alien invasion>."""
    def __init__(self):
        """Initialize game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 3
        self.ship_limit = 3

        # Bullet settings
        self.Bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        # intensify rate of game speed
        self.speedup_scale = 1.2
        # intensify rate of a alien score
        self.score_scale = 1.5
        
        # Path of high score's json.
        self.path_of_high_score = 'high_score.json' 
        
        self.initailize_dynamic_settings()

    def initailize_dynamic_settings(self):
        """The initialization settings that change with the progress of the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # The value of "fleet_direction" equals 1 indicates the movement towards the right,
        # whereas it equals -1 signifies the movement towards the left.
        self.fleet_direction = 1

        # Score settings
        self.alien_points = 50

    def increase_speed(self):
        """Speed up dynamic settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)