import pygame

from source.assist import Colors, Constants, MathHelp

from source.enums import GamePiece


class Piece:
    def __init__(self, piece_type: GamePiece, row: int, col: int, x: int, y: int):

        self.row = row
        self.col = col
        self.x = x
        self.y = y
        self.type = piece_type

        self.font = pygame.font.SysFont("/fonts/LemonMilk.otf", 20)

        self.image = self.font.render(self.type.name[0], True, Colors.RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
