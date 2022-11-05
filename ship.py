import pygame
import random


class Ship(pygame.sprite.Sprite):
    """A ship that will move according to key inputs on the screent
    Functions: up(), down(), left(), right(), shoot(), gunpos(), update()
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        # Load the image of the ship and set it as the image for this sprite.
        self.image = pygame.image.load("media/starship.png")
        self.rect = self.image.get_rect()
        # Screen data.
        screen = pygame.display.get_surface()
        self.screen_rect = screen.get_rect()
        # Ship attributes
        self.speed = 5
        self.damage = 0
        self.bitcoin_mining = 0
        # Set firing status.
        self.firing = False
        # Set ship starting position.
        self.start_pos = [200, screen.get_height() / 2]
        self.rect.move_ip(self.start_pos[0], self.start_pos[1])

    def up(self):
        self.rect.move_ip(0, -self.speed)
        self.rect.clamp_ip(self.screen_rect)

    def down(self):
        self.rect.move_ip(0, self.speed)
        self.rect.clamp_ip(self.screen_rect)

    def left(self):
        self.rect.move_ip(-self.speed, 0)
        self.rect.clamp_ip(self.screen_rect)

    def right(self):
        self.rect.move_ip(self.speed, 0)
        self.rect.clamp_ip(self.screen_rect)

    def shoot(self):
        # Randomly choose between bitcoin and super bitcoin. Since there are only two options it's 50% chance each.
        shot_type = random.choice(["bitcoin", "super_bitcoin"])
        return (self.firing, shot_type)

    def gunpos(self):
        """Return the current position of the ships gun (positioned at the center of the ship)"""
        return (self.rect.centerx, self.rect.centery)

    def update(self):
        if self.bitcoin_mining < 100:
            self.bitcoin_mining += 1
