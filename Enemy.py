import pygame
import random
from Block import Block
from config import *


def play_sound() -> None:
    sound = pygame.mixer.Sound(get_next_collect_sound())
    pygame.mixer.Channel(COLLECT_CHANNEL_INDEX).play(sound)


class Enemy(pygame.sprite.Sprite):

    def __init__(self, screen) -> None:
        super().__init__()
        self.image = pygame.image.load(random.choice(enemy_collection))
        self.upper_limit = self.image.get_height() * -1
        self.rect = self.image.get_rect()
        self.left = random.randint(0, (WIDTH - self.image.get_width()))
        self.top = self.upper_limit
        self.screen = screen
        self.degree = random.randint(-1, 1)
        self.direction = random.choice(['top', 'bottom'])
        if self.direction == 'top':
            self.top = HEIGHT
        self.rect.topleft = (self.left, self.top)

    def update(self, block_rect: Block) -> None:
        if self.direction == 'top':
            self.top -= 1
        else:
            self.top += 1
        self.left += self.degree
        is_went_out = self.top > HEIGHT or self.top < self.upper_limit or \
                      self.left > WIDTH or self.left < (self.image.get_width() * -1)

        if is_went_out:
            self.kill()

        self.rect.topleft = (self.left, self.top)
        is_collide = self.rect.colliderect(block_rect.rect)
        if is_collide:
            pygame.event.post(pygame.event.Event(EVENT_ENEMY_TOUCHED))

