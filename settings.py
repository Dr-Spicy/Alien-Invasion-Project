class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1150
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 2.5

        # Bullet settings
        self.bullet_speed = 4.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.buttets_allowed = 6

        # Alien settings
        self.alien_speed = 1.
        # fleet_drop_spd controls how quickly it drops when hitting the right edge
        self.fleet_drop_speed = 10

        # fleet direction of 1 represents right, ; -1 reps left
        # This is more elegent than using a if-elif statement
        self.fleet_direction = 1