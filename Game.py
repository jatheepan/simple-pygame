import pygame
import sys
from random import random
from config import *
from Block import Block
from Item import Item
from Enemy import Enemy
from datetime import datetime, timedelta


class Game:
    started = False
    score = 0
    last_spawn_at: datetime = None

    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(1, 40)
        self.font = pygame.font.SysFont(None, 23)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.mixer.music.load('assets/music.mp3')
        self.clock = pygame.time.Clock()
        self.block = Block(self.screen)
        self.item_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.create_item()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.started:
                    self.started = True
                    # pygame.mixer.music.play(-1)

                if not self.started:
                    continue

                if event.type == pygame.KEYDOWN:
                    self.listen_keyboard_events(event)

                if event.type == EVENT_ITEM_COLLECTED:
                    self.score += 1
                    self.create_item()

            self.screen.fill("black")
            self.block.draw()
            self.draw_welcome_message()
            self.draw_score()
            self.draw_level()
            if self.started:
                self.item_group.draw(self.screen)
                self.item_group.update(self.block)
                self.enemy_group.draw(self.screen)
                self.enemy_group.update(self.block)
                self.spawn_enemy()

            pygame.display.update()
            self.clock.tick(FPS)

    def create_item(self):
        item = Item(self.screen)
        self.item_group.add(item)

    def spawn_enemy(self):
        now = datetime.now()
        if not self.last_spawn_at:
            self.last_spawn_at = now - timedelta(0, 2)

        delta_in_millis = (now - self.last_spawn_at).total_seconds() * 1000

        per = 1.0 - ((self.get_level() - 1) * 0.2)
        wait_duration = 2000 * per
        print(wait_duration)
        if delta_in_millis < wait_duration:
            return

        enemy = Enemy(self.screen)
        self.enemy_group.add(enemy)
        self.last_spawn_at = now

    def listen_keyboard_events(self, event) -> None:
        if event.key == pygame.K_LEFT:
            self.block.move('left')
        if event.key == pygame.K_RIGHT:
            self.block.move('right')
        if event.key == pygame.K_DOWN:
            self.block.move('down')
        if event.key == pygame.K_UP:
            self.block.move('up')

    def draw_welcome_message(self) -> None:
        if self.started:
            return
        img = self.font.render("Press Spacebar to start".upper(), True, WHITE)
        top = HEIGHT / 2
        left = (WIDTH - img.get_width()) / 2
        offset = self.block.image.get_height() / 2
        top += offset
        self.screen.blit(img, (left, top))

    def draw_score(self) -> None:
        if not self.started:
            return
        score = f"Score: {self.score}"
        img = self.font.render(score, True, WHITE)
        margin = 2
        top = 0 + margin
        left = WIDTH - img.get_width() - margin
        self.screen.blit(img, (left, top))

    def draw_level(self) -> None:
        if not self.started:
            return
        score = f"Level: {self.get_level()}"
        img = self.font.render(score, True, WHITE)
        margin = 2
        top = 0 + margin
        left = 0 + margin
        self.screen.blit(img, (left, top))

    def get_level(self):
        return int(self.score / 5) + 1


if __name__ == "__main__":
    game = Game()
    game.run()
