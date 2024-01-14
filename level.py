import pygame
from tiles import Tiles
from player import Player


class Level:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = YSortCamera()
        self.obstacle_sprites = pygame.sprite.Group()
        self.player = Player((64, 64), [self.visible_sprites], self.obstacle_sprites)

        self.create_map()

    def create_map(self):
        for x in range(0, 1920 + 64, 64):
            for y in range(0, 768 + 64, 64):
                if (
                    x == 0
                    or y == 0
                    or y == 768
                    or x == 1920
                    or (x % 128 == 0 and y % 128 == 0)
                ):
                    Tiles((x, y), [self.visible_sprites, self.obstacle_sprites])

    def run(self):
        self.visible_sprites.customer_draw(self.player)
        self.visible_sprites.update()


class YSortCamera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def customer_draw(self, player):
        # self.offset.x = player.rect.centerx
        # self.offset.y = player.rect.centery - self.half_height
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
