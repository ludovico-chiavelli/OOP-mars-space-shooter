import pygame

WHITE = (255, 255, 255)


class Settings:
    """A class to store all settings for the game."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 750
        # FPS constant should live in settings so it's here
        self.FPS = 60

        # Background image with convert() method to make it quicker.
        self.screen_backgrnd = pygame.image.load("media/mars_background.png")
        self.bg_color = WHITE

        # Load a sound to play on impacts between sprites
        self.boom_sound = pygame.mixer.Sound("media/boom.wav")

        # Game settings
        self.lives = 3
        self.score = 0
        # MAX_ALIENS constant should live in settings so it's here. This way it's simple
        # to change the maximum amount of aliens.
        self.MAX_ALIENS = 20
