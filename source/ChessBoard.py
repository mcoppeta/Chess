import pygame

import Constants
import Colors
import MathHelp

import Tile


class ChessBoard:
    def __init__(self, game_type: str, x: int, y: int):
        self.image = pygame.Surface(MathHelp.scale_tuple(2 + Constants.BOARD_ROWS, Constants.TILE_SIZE)).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.font = pygame.font.SysFont("/fonts/LemonMilk.otf", 30)

        colors = [Constants.LIGHT_COLOR, Constants.DARK_COLOR]
        colors_index = 0

        for row in range(2 + Constants.BOARD_ROWS):
            for col in range(2 + Constants.BOARD_COLS):
                if row == 0 or row == 1 + Constants.BOARD_ROWS:
                    if 0 < col < 1 + Constants.BOARD_COLS:
                        current = Tile.LetterTile(colors[colors_index], chr(97 - 1 + col), Colors.WHITE,
                                                  self.font, Constants.TILE_LENGTH * col,
                                                  Constants.TILE_LENGTH * row)
                        current.blit(self.image)
                    else:
                        current = Tile.Tile(colors[colors_index], Constants.TILE_LENGTH * col,
                                            Constants.TILE_LENGTH * row)
                        current.blit(self.image)

                elif col == 0 or col == 1 + Constants.BOARD_COLS:
                    if 0 < row < 1 + Constants.BOARD_ROWS:
                        current = Tile.LetterTile(colors[colors_index], "" + str(Constants.BOARD_ROWS - row + 1),
                                                  Colors.WHITE, self.font, Constants.TILE_LENGTH * col,
                                                  Constants.TILE_LENGTH * row)
                        current.blit(self.image)
                else:
                    current = Tile.Tile(colors[colors_index], Constants.TILE_LENGTH * col, Constants.TILE_LENGTH * row)
                    current.blit(self.image)

                colors_index = MathHelp.toggle(colors_index)
            colors_index = MathHelp.toggle(colors_index)

            self.grid = [[] for i in range(8)]
            if game_type == "standard":
                print("standard")
            else:
                print("error")
