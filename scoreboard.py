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

        # Prepare the initial score info
        self.prep_score()

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

    def show_score(self):
        """Draw score to screen"""
        self.screen.blit(self.score_image, self.score_rect)
