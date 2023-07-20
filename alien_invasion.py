import sys
import pygame

from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        # initializes the background setting that Pygame needs to work smoothly
        pygame.init()
        """
        We make a clock and ensure it ticks once on each pass of the loop. If 
        the loop processes faster than the rate we define, pygame will calculate
        the correct amount of time to pause so that the game runs at a consiste
        nt rate. 
        """
        self.clock = pygame.time.Clock()

        self.settings = Settings()

        # Call this display.set_mode to create a display window, on which we
        # sho w the graphics of the game. We assign this display window to
        # the self. display window, and it will be available in all methods
        # in the class.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        # This attribute is called a surface, aka a part of the screen where
        # game elements are displayed. The surface returned by
        # display.set_mode reps the entire game window. Once the game's
        # animation loop gets activated the surface will be redrawn on each
        # pass of the loop, so it can be updated with any changes trigger by
        # user input
        pygame.display.set_caption("Alien Invasion")
        # Set the background color.
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                # The pygame.event.get() returns a list of events that have taken
                # place since the last time this function called.
                if event.type == pygame.QUIT:
                    sys.exit()
            """Re-draw the screen during each pass through the loop by the fill method."""
            self.screen.fill(self.bg_color)
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            """the tick() method takes one argument: the frame rate fro the game. """
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
