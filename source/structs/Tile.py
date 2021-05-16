import pygame
from source.assist import Constants


class Tile:
    def __init__(self, color: pygame.color.Color, x: int, y: int):
        self.image = pygame.Surface(Constants.TILE_SIZE).convert()
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def blit(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect.topleft)


class LetterTile:
    def __init__(self, bg_color: pygame.color.Color, letter: str, lbl_color: pygame.color.Color,
                 font: pygame.font.Font, x: int, y: int):
        self.image = pygame.Surface(Constants.TILE_SIZE).convert()
        self.image.fill(bg_color)

        self.label = font.render(letter, True, lbl_color)
        self.label_w, self.label_h = font.size(letter)
        self.label_pos = (x + int((Constants.TILE_LENGTH - self.label_w) / 2),
                          y + int((Constants.TILE_LENGTH - self.label_h) / 2))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def blit(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect.topleft)
        surface.blit(self.label, self.label_pos)
