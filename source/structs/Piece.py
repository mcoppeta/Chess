import pygame

from source.assist import Colors, Constants, MathHelp

from source.enums import GamePiece


class Piece:
    def __init__(self, piece_type: GamePiece, player: int, color: pygame.Color, row: int, col: int, board_pos: tuple):

        self.row = row
        self.col = col
        self.type = piece_type

        self.player = player
        self.color = color

        self.font = pygame.font.SysFont("/fonts/LemonMilk.otf", 30)

        self.image = self.font.render(self.type.name[0], True, self.color)

        boardx, boardy = board_pos
        self.x, self.y = MathHelp.snap_topleft(Constants.TILE_SIZE, (boardx + self.col * Constants.TILE_LENGTH,
                                                                     boardy + self.row * Constants.TILE_LENGTH),
                                               self.image.get_size())

        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
