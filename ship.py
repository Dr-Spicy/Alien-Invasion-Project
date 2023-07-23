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

        self.screen = ai_game.screen
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

        # Movement flag: start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's location based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
