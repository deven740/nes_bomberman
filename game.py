"""Game file"""

import pygame
import sys
from constants import WIDTH, HEIGHT, FPS, TILESIZE
from level import Level


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # self.screen.fill((56, 135, 1))
            self.screen.fill("black")
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
