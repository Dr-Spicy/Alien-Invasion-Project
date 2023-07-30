class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1150
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Bullet settings
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.buttets_allowed = 5

        # Alien settings
        # fleet_drop_spd controls how quickly it drops when hitting the right
        # edge
        self.fleet_drop_speed = 10

        # Initialize the game's dynamic
        # set the diff lvl
        self.difficulty_lvl = 'medium'
        # how quickly the game speeds up
        self.speedup_scale = 1.2
        # How quickly the alien point values increase
        self.score_scale = 1.5
        # init the attr that need to change throughout the game
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout games"""
        if self.difficulty_lvl == 'easy':
            self.ship_limit = 3
            self.bullet_allowed = 7
            self.ship_speed = .75
            self.bullet_speed = 1.5
            self.alien_speed = 0.5
        elif self.difficulty_lvl == 'medium':
            self.ship_limit = 2
            self.bullet_allowed = 5
            self.ship_speed = 1.5
            self.bullet_speed = 3.
            self.alien_speed = 1.
        elif self.difficulty_lvl == 'challenging':
            self.ship_limit = 1
            self.bullet_allowed = 3
            self.ship_speed = 3.
            self.bullet_speed = 6.
            self.alien_speed = 2.5

        # fleet direction of 1 represents right, ; -1 reps left
        # This is more elegent than using a if-elif statement
        self.fleet_direction = 1

        # Scoreing settings
        self.alien_pts = 50

    def increase_speed(self):
        """Increase the speed settings and alien pts value"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_pts = int(self.alien_pts * self.score_scale)
        # check the alien pts
        # print(self.alien_pts)

    def set_difficulty(self, diff_set):
        if diff_set == 'easy':
            print('easy')
        elif diff_set == 'medium':
            print('medium')
        elif diff_set == 'challenging':
            print('challenging')

