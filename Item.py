import pygame
from random import randint
from Block import Block
from config import *


def play_sound() -> None:
    sound = pygame.mixer.Sound(get_next_collect_sound())
    pygame.mixer.Channel(COLLECT_CHANNEL_INDEX).play(sound)


class Item(pygame.sprite.Sprite):
    width = 32
    height = 26

    def __init__(self, screen) -> None:
        super().__init__()
        image = pygame.image.load('assets/items.png').convert()
        position = randint(0, int(image.get_width() / self.width) - 1)
        left = position * self.width
        top = 292
        self.image = image.subsurface(left, top, self.width, self.height)
        self.rect = self.image.get_rect()
        self.left = randint(0, (WIDTH - self.image.get_width()))
        self.top = randint(0, (HEIGHT - self.image.get_height()))
        self.rect.topleft = (self.left, self.top)
        self.screen = screen

    def update(self, block_rect: Block) -> None:
        is_collide = self.rect.colliderect(block_rect.rect)
        if is_collide:
            pygame.event.post(pygame.event.Event(EVENT_ITEM_COLLECTED))
            play_sound()
            self.kill()

