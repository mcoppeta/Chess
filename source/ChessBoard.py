import pygame

import Constants
import MathHelp

import Tile


class ChessBoard:
    def __init__(self, x: int, y: int):
        self.image = pygame.Surface(MathHelp.scale_tuple(2 + Constants.BOARD_ROWS, Constants.TILE_SIZE)).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        colors = [Constants.LIGHT_COLOR, Constants.DARK_COLOR]
        colors_index = 0
        for row in range(2 + Constants.BOARD_ROWS):
            for col in range(2 + Constants.BOARD_COLS):
                if row == 0 or row == 1 + Constants.BOARD_ROWS:
                    if 0 < col < 1 + Constants.BOARD_COLS:
                        pass  # LETTER TILES
                elif col == 0 or col == 1 + Constants.BOARD_COLS:
                    if 0 < row < 1 + Constants.BOARD_ROWS:
                        pass  # NUMBER TILES
                else:
                    pass  # GENERAL TILE

                colors_index = MathHelp.toggle(colors_index)
