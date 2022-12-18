import pygame

WIDTH = 1280 / 2
HEIGHT = 720 / 2
FPS = 60

WHITE = (255, 255, 255)
COLLECT_CHANNEL_INDEX = 0
LOSE_CHANNEL_INDEX = 1

EVENT_ITEM_COLLECTED = pygame.USEREVENT + 1
EVENT_ENEMY_TOUCHED = pygame.USEREVENT + 2
sound_index = -1
sound_collection = [
    'assets/collect.wav',
    'assets/collect1.wav',
    'assets/collect2.wav',
    'assets/collect3.wav',
    'assets/collect4.wav',
    'assets/collect5.wav',
    'assets/collect6.wav',
]

enemy_collection = [
    'assets/enemyblue.png',
    'assets/enemygreen.png',
    'assets/enemyorange.png',
    'assets/enemyyellow.png',
]


def get_block_images(picture_type: str) -> str:
    return 'assets/block' + picture_type + '.png'


def get_next_collect_sound() -> str:
    global sound_index
    sound_index += 1
    is_last_sound = sound_index == len(sound_collection)
    if is_last_sound:
        sound_index = 0

    return sound_collection[sound_index]
