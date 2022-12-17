import pygame
from random import randint
from config import *


class Item(pygame.sprite.Sprite):
    img = pygame.image.load('assets/blockup.png')
    left = randint(0, (WIDTH - img.get_width()))
    top = randint(0, (HEIGHT - img.get_height()))
    sound_index = 0
    sound_collection = []

    def __init__(self, screen) -> None:
        super().__init__()
        self.image = self.img
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.left, self.top)
        self.screen = screen
        self.sound_collection = [
            pygame.mixer.Sound('assets/collect.wav'),
            pygame.mixer.Sound('assets/collect1.wav'),
            pygame.mixer.Sound('assets/collect2.wav'),
            pygame.mixer.Sound('assets/collect3.wav'),
            pygame.mixer.Sound('assets/collect4.wav'),
            pygame.mixer.Sound('assets/collect5.wav'),
            pygame.mixer.Sound('assets/collect6.wav'),
        ]
        pygame.display.flip()

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self, block_rect: pygame.Rect) -> None:
        is_collide = self.rect.colliderect(block_rect)
        if is_collide:
            self.play_sound()
            self.kill()

    def play_sound(self) -> None:
        sound = self.sound_collection[self.sound_index]
        pygame.mixer.Channel(COLLECT_CHANNEL_INDEX).play(sound)
        self.sound_index += 1
        is_last_sound = self.sound_index >= len(self.sound_collection)
        if is_last_sound:
            self.sound_index = 0

