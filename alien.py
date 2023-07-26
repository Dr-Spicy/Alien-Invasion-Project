import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""

        # Inherit from the parent class
        super().__init__()

        # Get the screen and settings from the game instance
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top-left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal location for precise control
        self.x = float(self.rect.x)

    def update(self):
        """Move aliens to the right"""

        # Move the alien to the right by the speed defined in settings
        # mulitple by the direction indicator, 1 for right, -1 for left
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        # update the alien's rectangle position as well
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        # alien is at edge if its rect crossed the screen's right
        # or its rect's left crossed the screen's left
        # will return True if at either edge
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
