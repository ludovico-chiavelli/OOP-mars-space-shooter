import pygame
import random


class Alien(pygame.sprite.Sprite):
    """Alien class for spawning aliens. The class itself keeps track of how many
    aliens are on screen"""

    # Keep track of aliens on screen
    current_alien_count = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("media/roadster.png")
        self.rect = self.image.get_rect()
        # Screen data
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        # Set a random speed for the alien
        self.speed = random.randint(2, 10)
        self.spawn()

    def spawn(self):
        """Makes the alien roadster spawn on the right of the screen at a random height"""
        self.rect.move_ip(
            # The offset of 50px is needed otherwise the aliens get deleted immediately because
            # they technically spawn off screen. I found this value through trial and error.
            self.screen.get_width() - 50,
            random.randint(0, self.screen.get_height()),
        )

    def update(self):
        # Make the alien roadster move left
        self.rect.move_ip(-self.speed, 0)

        # Delete the alien if it's of screen
        if not self.screen_rect.contains(self.rect):
            self.kill()
            # Make sure the count never goes negative
            if not Alien.current_alien_count < 0:
                Alien.current_alien_count -= 1
