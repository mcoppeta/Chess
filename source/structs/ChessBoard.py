import pygame

from source.assist import MathHelp, Colors, Constants

from source.structs import Tile, Piece

from source.enums import GamePiece


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
                        current = Tile.LetterTile(colors[colors_index], chr(97 - 1 + col), Colors.BLACK,
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
                                                  Colors.BLACK, self.font, Constants.TILE_LENGTH * col,
                                                  Constants.TILE_LENGTH * row)
                        current.blit(self.image)
                else:
                    current = Tile.Tile(colors[colors_index], Constants.TILE_LENGTH * col, Constants.TILE_LENGTH * row)
                    current.blit(self.image)

                colors_index = MathHelp.toggle(colors_index)
            colors_index = MathHelp.toggle(colors_index)

        self.grid, self.pieces = self.create_grid_standard()

    def blit(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect.topleft)

    def blit_pieces(self, screen: pygame.Surface):
        for row in self.grid:
            for piece in row:
                screen.blit(piece.image, piece.rect)

    def create_grid_standard(self):
        grid = [[0 for j in range(8)] for i in range(8)]
        pieces = Piece.PieceGroup()
        for r in range(1, 9):
            for c in range(1, 9):
                if r == 2 or r == 7:
                    p = Piece.Piece(GamePiece.GamePiece.PAWN, 1, Colors.WHITE, r, c, self.rect.topleft)
                    grid[8 - r][c - 1] = p
                    pieces.add(p)
                else:
                    p = Piece.Piece(GamePiece.GamePiece.NULL, 0, Colors.BLACK, r, c, self.rect.topleft)
                    grid[8 - r][c - 1] = p
                    pieces.add(p)
        
        return grid, pieces
