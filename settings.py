class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1150
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 1

        # Bullet settings
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.buttets_allowed = 5

        # Alien settings
        # fleet_drop_spd controls how quickly it drops when hitting the right
        # edge
        self.fleet_drop_speed = 10


        # how quickly the game speeds up
        self.speedup_scale = 1.2
        # init the attr that need to change throughout the game
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout games"""
        self.ship_speed = 2. +5
        self.bullet_speed = 3.
        self.alien_speed = 1.0
        # fleet direction of 1 represents right, ; -1 reps left
        # This is more elegent than using a if-elif statement
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase the speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
