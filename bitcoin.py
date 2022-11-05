import pygame

import random
import math


class Bitcoin(pygame.sprite.Sprite):
    """The 'bullet' for the ship. It moves straight to the right when space is pressed.
    Is destroyed on impact with an alien."""

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("media/bitcoin.png")
        self.rect = self.image.get_rect()
        # Screen data
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.speed = 10
        # Spawn bitcoin and pass current pos for starting location
        self.spawn(pos)

    def spawn(self, pos):
        """Makes bitcoin spawn at the center of the ship"""
        centerx, centery = pos
        self.rect.move_ip(centerx, centery)

    def update(self):
        # Make the bitcoin roadster move right
        self.rect.move_ip(self.speed, 0)

        # Delete the bitcoin if it's off screen
        if not self.screen_rect.contains(self.rect):
            self.kill()


class SuperBitcoin(Bitcoin):
    """Same as Bitcoin but doesn't get destroyed on impact and instead moves in
    a new random direction."""

    def __init__(self, pos):
        super().__init__(pos)
        self.calc_new_vector()

    # Built upon Ball class from https://www.pygame.org/docs/tut/tom_games6.html#makegames-6-3
    def update(self):
        newpos = self.calc_new_pos(self.rect, self.vector)
        self.rect = newpos

        # Delete the bitcoin if it's off screen
        if not self.screen_rect.contains(self.rect):
            self.kill()

    # Taken from Ball class from https://www.pygame.org/docs/tut/tom_games6.html#makegames-6-3
    def calc_new_pos(self, rect, vector):
        """Calculate new position of the object and return the rect's updated coordinates"""
        (angle, z) = vector
        (dx, dy) = (z * math.cos(angle), z * math.sin(angle))
        return rect.move(dx, dy)

    def calc_new_vector(self):
        """Calculate new vector of the object"""
        angle_deg = random.randint(0, 359)
        # Convert angle to radians
        angle_rad = math.radians(angle_deg)
        self.vector = (angle_rad, self.speed)
