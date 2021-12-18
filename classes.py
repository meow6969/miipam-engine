import pygame
import random


class rikachan(pygame.sprite.Sprite):
    """represents m-m-my rika chan.... m-my beloved...."""

    def __init__(self, window, x, y):
        super().__init__()
        self.window = window

        r = random.randint(0, 1)

        img = random.randint(0, 3)
        # content/idle3.png added twice to make it more common then the others
        images = ['content/idle1.png', 'content/idle2.png', 'content/idle3.png', 'content/idle3.png']
        self.image_file = images[img]
        rare_rika = random.randint(0, 99)
        if rare_rika == 69:
            self.image_file = 'content/rare_rika_idle.png'
        if r == 1:
            self.image = pygame.image.load(self.image_file)
            self.invert = False
        else:
            self.invert = True
            self.image = pygame.transform.flip(pygame.image.load(self.image_file), True, False)
        self.timer = random.randint(1000, 3000)
        self.x = x
        self.y = y
        self.top_left = (x, y)
        self.bottom_right = (x + 640, y + 480)
        self.right = x + 640
        self.bottom = y + 480
        self.miipaaa = random.randint(1000, 2000)

        self.mouth = 0
        self.mouth_state = False

        self.rect = pygame.Rect(self.x, self.y, 640, 480)

    def draw(self):
        self.window.blit(self.image, self.rect)

