import pygame
import sys
from random import random
from config import *
from Block import *


class Game:
    started = False

    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont(None, 40)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.block = Block(self.screen)
        pygame.key.set_repeat(1, 60)
        # self.group = pygame.sprite.Group()
        # self.group.add(block)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.started:
                    self.started = True

                if not self.started:
                    continue

                if event.type == pygame.KEYDOWN:
                    self.listen_keyboard_events(event)

            self.screen.fill("black")
            self.block.draw()
            self.draw_welcome_message()
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
        img = self.font.render("Press Spacebar", True, WHITE)
        self.screen.blit(img, (0, 0))

if __name__ == "__main__":
    game = Game()
    game.run()
