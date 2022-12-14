import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/spacecraft.png').convert()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        # start each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # Draw the ship at its current position
        self.screen.blit(self.image, self.rect)
