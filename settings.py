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
        # The value of "fleet_direction" equals 1 indicates the movement towards the right,
        # whereas it equals -1 signifies the movement towards the left.
        self.fleet_direction = 1