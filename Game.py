import pygame
import sys
from random import random
from config import *
from Block import Block
from Item import Item
from Enemy import Enemy
from datetime import datetime, timedelta


class Game:

    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(1, 40)
        self.font = pygame.font.SysFont(None, 23)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("black")
            pygame.display.update()
            self.clock.tick(FPS)

    def spawn_item(self):
        pass

    def spawn_enemy(self):
        pass

    def listen_keyboard_events(self, event) -> None:
        pass

    def draw_welcome_message(self) -> None:
        pass

    def draw_score(self) -> None:
        pass

    def draw_level(self) -> None:
        pass

    def get_level(self):
        pass

    def reset(self):
        pass


if __name__ == "__main__":
    game = Game()
    game.run()
