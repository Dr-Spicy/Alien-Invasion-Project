import pygame.font

class Button:
    """A class to build buttons for the game"""

    def __init__(self, ai_game, msg, width=200, height=50, font_size = 40,
                 button_color=(0, 35, 120), text_color=(255, 255, 255),
                 ):
        """Initialize button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = width, height
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(None, font_size)

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw msg on the button"""
        # use screen.fill() to draw the rectangular portion of the button
        self.screen.fill(self.button_color, self.rect)
        # call screen.blit() to draw the button text image to the screen at the
        # msg_image_rect position
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def _update_msg_position(self):
        """If the button has been moved, the text needs to be moved as well."""
        self.msg_image_rect.center = self.rect.center
