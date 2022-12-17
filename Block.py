import pygame
from config import WIDTH, HEIGHT, get_block_images


class Block(pygame.sprite.Sprite):
    top = 0
    left = 0
    max_top = 0
    max_left = 0
    up_img = pygame.image.load(get_block_images('up'))
    down_img = pygame.image.load(get_block_images('down'))
    left_img = pygame.image.load(get_block_images('left'))
    right_img = pygame.image.load(get_block_images('right'))

    def __init__(self, screen) -> None:
        super().__init__()
        self.image = self.up_img
        self.rect = self.image.get_rect()
        self.left = (WIDTH - self.image.get_width()) / 2
        self.top = (HEIGHT - self.image.get_height()) / 2
        self.max_left = WIDTH - self.image.get_width()
        self.max_top = HEIGHT - self.image.get_height()
        self.rect.topleft = (self.left, self.top)
        self.screen = screen

    def draw(self):
        self.rect.topleft = (self.left, self.top)
        self.screen.blit(self.image, self.rect)

    def move(self, direction: str) -> None:
        picture = get_block_images(direction)

        if direction == 'up':
            self.image = self.up_img
            self.top -= 10
        if direction == 'down':
            self.image = self.down_img
            self.top += 10
        if direction == 'left':
            self.image = self.left_img
            self.left -= 10
        if direction == 'right':
            self.image = self.right_img
            self.left += 10
        if self.left < 0:
            self.left = 0
        if self.left > self.max_left:
            self.left = self.max_left
        if self.top < 0:
            self.top = 0
        if self.top > self.max_top:
            self.top = self.max_top
        self.draw()

