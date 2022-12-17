import pygame
import sys
from random import random
from config import *
from Block import *


class Game:
    def __init__(self):
        pygame.init()
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

                if event.type == pygame.KEYDOWN:
                    print(random())
                    self.listen_keyboard_events(event)
                self.screen.fill("black")
                self.block.draw()
                pygame.display.update()
                self.clock.tick(FPS)

    def listen_keyboard_events(self, event):
        if event.key == pygame.K_LEFT:
            self.block.move('left')
        if event.key == pygame.K_RIGHT:
            self.block.move('right')
        if event.key == pygame.K_DOWN:
            self.block.move('down')
        if event.key == pygame.K_UP:
            self.block.move('up')


if __name__ == "__main__":
    game = Game()
    game.run()
