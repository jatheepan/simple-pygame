import pygame
import sys
from random import random
from config import *
from Block import Block
from Item import Item


class Game:
    started = False

    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont(None, 26)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.mixer.music.load('assets/music.mp3')
        self.clock = pygame.time.Clock()
        self.block = Block(self.screen)
        self.item = Item(self.screen)
        self.item_group = pygame.sprite.Group()
        self.item_group.add(self.item)
        pygame.key.set_repeat(1, 60)

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

            self.screen.fill("black")
            self.block.draw()
            self.draw_welcome_message()
            if self.started:
                self.item_group.draw(self.screen)
                self.item_group.update(self.block.rect)

            pygame.display.update()
            self.clock.tick(FPS)

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


if __name__ == "__main__":
    game = Game()
    game.run()
