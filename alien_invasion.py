import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        # initializes the background setting that Pygame needs to work smoothly
        pygame.init()
        self.running = True
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
            (self.settings.screen_width, self.settings.screen_height))

        """If we wanna run in full-screen, use the rest codes."""
        '''
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        '''

        # This attribute is called a surface, aka a part of the screen where
        # game elements are displayed. The surface returned by
        # display.set_mode reps the entire game window. Once the game's
        # animation loop gets activated the surface will be redrawn on each
        # pass of the loop, so it can be updated with any changes trigger by
        # user input
        pygame.display.set_caption("Alien Invasion")

        # Make an instance of Ship after the screen has been created
        # The self argument here refers to an instance of 'AlienInvasion'
        self.ship = Ship(self)
        # Make an instance of pygame.sprite.Group class to store manage all
        # active bullets, and bullets get drawn and updated each loop.
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game."""
        while self.running:
            '''Watch for keyboard and mouse events. '''
            self._check_events()
            """Update the location of the ship"""
            self.ship.update()
            """Update the locations of the bullets n remove old ones"""
            self.bullets.update()
            """Get rid of bullets out of screen"""
            self._update_bullets()
            """Re-draw the screen during each pass through the loop by the 
                       fill method."""
            self._update_screen()
            """the tick() method takes one argument: the frame rate fro the 
            game."""
            self.clock.tick(60)


    def _update_bullets(self):
        """Update position of bullets and get rid of ones past the top"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                # If a bullet reaches top, remove
                self.bullets.remove(bullet)
        # A print to show how many bullets current exist in the game
        # print(len(self.bullets))
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # Set the method to control the FLAG of ship to move right
            # Use a single keydown to register a single movement
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # Use a keyup to reflect a continuous movement
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        """Update the fired bullets"""
        # bullet.sprites() method returns a list of all sprites in the group of
        # bullets. loop thru them and do .draw_bullet()
        # placed before the ship, so bullets do not start out on top of ship
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        """draw the ship on the background"""
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _check_keydown_events(self, event):
        """Respond to keydown events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # Quit on ESC
        elif event.key == pygame.K_ESCAPE:
            self.running = False
        # Firing bullets on SPACE
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to keyup events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        # make an instance of bullet and call it new_bullet
        if len(self.bullets) < self.settings.buttets_allowed:
            new_bullet = Bullet(self)
            # Add to the group bullets by .add(), who is similar to append() but
            # specific for Pygame groups.
            self.bullets.add(new_bullet)






if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
