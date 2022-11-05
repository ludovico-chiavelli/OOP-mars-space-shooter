import pygame


class ValueTracker(pygame.sprite.Sprite):
    """General value tracker class built upon Score class found at https://github.com/pygame/pygame/blob/main/examples/aliens.py
    Meant for displaying dashboard values sourced from various places."""

    def __init__(self, posx: int, posy: int):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.font = pygame.font.Font(None, 20)
        self.color = pygame.Color("red")
        self.lastvalue = -1
        # Starting value of 0 for dashboard values is fine as it'll get updated almost immediately.
        self.value = 0
        self.update()
        self.rect = self.image.get_rect().move(posx, posy)

    def update(self):
        """We only update the score in update() when it has changed."""
        if self.value != self.lastvalue:
            self.lastvalue = self.value
            # When rendering format the self.value to be always 3 digits
            # this link helped with understandting the formatting https://stackoverflow.com/questions/134934/display-number-with-leading-zeros
            self.image = self.font.render(f"{self.value:03d}", 0, self.color)
