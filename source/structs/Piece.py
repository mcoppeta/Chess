import pygame

from source.assist import Colors, Constants, MathHelp

from source.enums import GamePiece


class Piece(pygame.sprite.Sprite):
    def __init__(self, piece_type: GamePiece, row: int, col: int):
        pygame.sprite.Sprite.__init__(self)

        self.row = row
        self.col = col
        self.type = piece_type

        self.font = pygame.font.SysFont("/fonts/LemonMilk.otf", 20)

        self.image = self.font.render(self.type.name[0], True, Colors.RED)
        self.rect = self.image.get_rect()
