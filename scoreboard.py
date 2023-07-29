import pygame.font


class Scoreboard:
    """A class to report score info"""

    def __init__(self, game):
        """Initialize scorekeeping attrs"""
        self.score_image = None
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        # Font settings for score info
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 40)

        # Prepare the initial score/high score/lvl info
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Turn the score into a rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = f"Score: {rounded_score:,}"
        self.score_image = self.font.render(score_str, True,
                                            self.text_color,
                                            self.settings.bg_color)
        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_high_score(self):
        """Turn the high score into a rendered image"""
        rounded_high_score = round(self.stats.high_score, -1)
        high_score_str = f"High Score: {rounded_high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color,
                                                 self.settings.bg_color)
        # Center the high score at the top of screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """"Check to see if there's a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            # prep the new high score image
            self.prep_high_score()

    def prep_level(self):
        """Turn the level into a rendered image"""
        lvl_str = f"Lv: {self.stats.level}"
        self.lvl_image = self.font.render(lvl_str, True, self.text_color,
                                          self.settings.bg_color)
        # Display the lvl at below the score
        self.lvl_rect = self.lvl_image.get_rect()
        self.lvl_rect.right = self.score_rect.right
        self.lvl_image.top = self.score_rect.bottom + 10

    def show_score(self):
        """Draw score/high score/lvl/ to screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.lvl_image, self.lvl_rect)

