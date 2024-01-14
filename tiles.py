import pygame


class Tiles(pygame.sprite.Sprite):
    def __init__(self, pos, groups) -> None:
        super().__init__(groups)
        self.image = pygame.image.load("images/sprite_045.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
