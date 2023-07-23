import pygame


class Ship:
    """A class to manage the ship."""
    """
    Pygame is efficient b/c it treats all shaped elements as rectangles(rects).
    Especially when computing the collide
    """

    def __init__(self, ai_game):  # ai_game refer to the current instance of the
        # AlienInvasion class.
        """Initialize the ship and set its starting position."""
        # The screen background is inherited from the game as well as the
        # settings
        self.screen, self.settings = ai_game.screen, ai_game.settings
        # We access the screen's 'rect' attr using the get_rect() method
        # Doing so allows us to place the ship in the right place on the screen
        self.screen_rect = ai_game.screen.get_rect()

        ''' Load the ship image and get its rect.'''
        # This returns a surface reps the ship.
        self.image = pygame.image.load('images/ship.bmp')
        # We get the ship surface's rectangle here
        self.rect = self.image.get_rect()

        """
                When you’re working with a rect object, you can use the
        x- and y-coordinates of the top, bottom, left, and right edges
        of the rectangle, as well as the center, to place the object.
        You can set any of these values to establish the current
        position of the rect. When you’re centering a game element,
        work with the center, centerx, or centery attributes of a rect.
        When you’re working at an edge of the screen, work with
        the top, bottom, left, or right attributes. There are also
        attributes that combine these properties, such as midbottom,
        midtop, midleft, and midright. When you’re adjusting the
        horizontal or vertical placement of the rect, you can just use
        the x and y attributes, which are the x- and y-coordinates of
        its top-left corner. These attributes spare you from having to
        do calculations that game developers formerly had to do
        manually, and you’ll use them often.
        
        In Pygame, the top-left is (0,0), whereas the bottom-right is (
        +width, +height)
        """

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal location.
        # self.rect.x only works with integers
        self.x = float(self.rect.x)

        # Movement flag: start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's location based on the movement flag."""
        # Update the ship's x_value by ship speed instead of the rect.x
        # Confine the ship's range
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
