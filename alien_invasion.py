import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""

        # initializes the background setting that Pygame needs to work smoothly
        pygame.init()
        # Keep game running if in active state
        self.running = True
        # Start Alien Invasion in an active state.
        self.game_active = False
        """We make a clock and ensure it ticks once on each pass of the loop. 
        If the loop processes faster than the rate we define, pygame will 
        calculate the correct amount of time to pause so that the game runs 
        at a consistent rate."""
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
        # Create an instance to store game statistics
        self.stats = GameStats(self)
        # Make an instance of Ship after the screen has been created
        # The self argument here refers to an instance of 'AlienInvasion'
        self.ship = Ship(self)
        # Make an instance of pygame.sprite.Group class to store manage all
        # active bullets, and bullets get drawn and updated each loop.
        self.bullets = pygame.sprite.Group()
        # Make another instance of pygame.sprite.Group class to store manage all
        # active aliens
        self.aliens = pygame.sprite.Group()
        # Create the fleet using _create_fleet() method
        self._create_fleet()
        # Create the play button
        self.play_button = Button(self, 'Play', width=280, font_size=48,
                                  button_color=(255, 35, 20),
                                  text_color=(255, 255, 255)
                                  )
        # Make difficulty lvl buttons
        self._make_difficulty_buttons()

    def run_game(self):
        """Start the main loop for the game."""
        '''Watch for keyboard and mouse events. '''
        while self.running:
            self._check_events()

            if self.game_active:
                """Update the location of the ship"""
                self.ship.update()
                """Update position of bullets and get rid of ones past the 
                top"""
                self._update_bullets()
                """Move the alien fleet right and downwards"""
                self._update_alien()

            """Re-draw the screen during each pass through the loop by the 
                       fill method."""
            self._update_screen()
            """the tick() method takes one argument: the frame rate fro the 
            game."""
            self.clock.tick(60)

    def _make_difficulty_buttons(self):
        """Make buttons that allow player to select diff lvls"""
        self.easy_button = Button(self, 'Easy')
        self.medium_button = Button(self, 'Medium')
        self.challenge_button = Button(self, 'Difficult')

        # Position all 3 buttons to align
        self.easy_button.rect.top = (
            self.play_button.rect.top + 1.5 * self.play_button.rect.height
        )
        self.easy_button._update_msg_position()

        self.medium_button.rect.top = (
            self.easy_button.rect.top + 1.5 * self.easy_button.rect.height
        )
        self.medium_button._update_msg_position()

        self.challenge_button.rect.top = (
            self.medium_button.rect.top + 1.5 * self.medium_button.rect.height
        )
        self.challenge_button._update_msg_position()

    def _update_bullets(self):
        """Update position of bullets and get rid of ones past the top"""
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                # If a bullet reaches top, remove
                self.bullets.remove(bullet)
        # A print to show how many bullets current exist in the game
        # print(len(self.bullets))

        # Deal with bullet-alien collisions and when fleet is empty, kill all
        # bullets and repop a new fleet.
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collision"""
        # Remove any bullets and aliens in collisions
        # return a dictionary with key being the
        #         # colliding bullets and value being the colliding alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,
                                                True, True)
        # check if the aliens group empty
        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()  # .empty method empty the sprites group
            self._create_fleet()
            self.settings.increase_speed()

    def _check_events(self):
        """Respond to key-presses and mouse events."""

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
            # Use a mousebuttondown to look for click
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mousebuttondown_events()

    def _create_fleet(self):
        """Create the fleet of aliens"""

        # Create an alien and keep adding aliens until no room
        # Spacing between aliens is one alien's width and one alien's height
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # register the x and y location to add a new alien
        # assign the first location as 1 width from the left
        current_x, current_y = alien_width, alien_height
        # A rect's size attribute is a tuple containing its width and height.

        # so long as there's room vertically
        while current_y < (self.settings.screen_height - 4 * alien_height):
            # So long as the location to add can fit one more alien
            while current_x < (self.settings.screen_width - 2 * alien_width):
                # Create new alien at the current_x and current_y
                self._create_alien(current_x, current_y)
                # Increment the location to work by 2 width
                current_x += 2 * alien_width

            # Finished a row; reset x_value, and increment y_value by 2 heights
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_pos, y_pos):
        """Create an alien and place it in the row's x position on the y
        positioned row"""
        # Add a new alien instance
        new_alien = Alien(self)

        # Align the pos of new alien and the location to add
        # do the same for the rectangle of new alien
        new_alien.x, new_alien.y = x_pos, y_pos
        new_alien.rect.x, new_alien.rect.y = x_pos, y_pos

        # Add the new alien to the group that manages the fleet.
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():  # True if an alien is at edges and fleet
                # need to turn
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            # Drop the entire fleet
            alien.rect.y += self.settings.fleet_drop_speed
        # Invert the fleet movement direction
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        # Decrement ships_left.
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            # Get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()
            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            # Pause
            sleep(0.5)
        else:
            self.game_active = False
            # Make the cursor visible again
            pygame.mouse.set_visible(True)

    def _update_alien(self):
        """ Check if the fleet is at an edge,Update the positions of the
        alien fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for any alien to ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Check if any aliens reached the bottom of the screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this event the same as if ship got hit
                self._ship_hit()
                break

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""

        self.screen.fill(self.settings.bg_color)

        """Update the fired bullets"""
        # bullet.sprites() method returns a list of all sprites in the group of
        # bullets. loop through them and do .draw_bullet()
        # placed before the ship, so bullets do not start out on top of ship
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        """draw the ship on the background"""
        self.ship.blitme()

        """Draw the aliens fleet on the bkg. When you can draw() on a group, 
        Pygame draws each element at the position defined by its .rect attr. 
        The draw() requires one argument: a surface to draw on."""
        self.aliens.draw(self.screen)

        """Draw the play button if the game is inactive. We draw it after all
        other elements have been draw but b4 flipping a new screen, so that the
        play button remains visible above all."""
        if not self.game_active:
            self.play_button.draw_button()
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.challenge_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _check_keydown_events(self, event):
        """Respond to keydown events"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        # Start on P
        elif event.key == pygame.K_p and not self.game_active:
            self._start_game()

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

    def _check_mousebuttondown_events(self):
        # Get the mouse position, which returns a tuple of x- and y- pos when
        # mouse is clicked
        mouse_pos = pygame.mouse.get_pos()
        # Send the coordinates to the new method _check_play_button()
        self._check_play_button(mouse_pos)
        # send the coor to the new method _check_diff_lvl()
        self._check_diff_lvl(mouse_pos)


    def _check_play_button(self, mouse_pos):
        """Start a new game when the play clicks Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        # Game will only restart if clicked and game is INactive
        if button_clicked and not self.game_active:
           self._start_game()

    def _start_game(self):
        """Restart the game"""
        # Reset the game stats
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.game_active = True

        # Remove any remaining bullets and aliens
        self.bullets.empty()
        self.aliens.empty()

        # Repop a new phalanx and center the ship
        self._create_fleet()
        self.ship.center_ship()

        # Hide the mouse cursor
        pygame.mouse.set_visible(False)

    def _check_diff_lvl(self, mouse_pos):
        """Set the corresponding difficult lvl"""
        ez_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        me_clicked = self.medium_button.rect.collidepoint(mouse_pos)
        hd_clicked = self.challenge_button.rect.collidepoint(mouse_pos)

        if ez_clicked:
            self.settings.difficulty_lvl = 'easy'
        elif me_clicked:
            self.settings.difficulty_lvl = 'medium'
        elif hd_clicked:
            self.settings.difficulty_lvl = 'challenging'

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
