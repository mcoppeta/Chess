import pygame

from source.assist import MathHelp, Colors, Constants

from source.structs import Tile, Piece

from source.enums import GamePiece, PlayerEnum


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
                screen.blit(piece.image, piece.rect)  # TODO: Isn't this what PieceGroup is for?

    def create_grid_standard(self):
        grid = [[0 for j in range(Constants.BOARD_COLS)] for i in range(Constants.BOARD_ROWS)]
        pieces = Piece.PieceGroup()
        for r in range(1, 1 + Constants.BOARD_ROWS):
            for c in range(1, 1 + Constants.BOARD_COLS):
                p = None

                if r == 1:  # Player 1 pieces
                    if c == 1 or c == 8:
                        p = Piece.Piece(GamePiece.GamePiece.ROOK, PlayerEnum.PlayerEnum.ONE, r, c, self.rect.topleft)
                    elif c == 2 or c == 7:
                        p = Piece.Piece(GamePiece.GamePiece.KNIGHT, PlayerEnum.PlayerEnum.ONE, r, c, self.rect.topleft)
                    elif c == 3 or c == 6:
                        p = Piece.Piece(GamePiece.GamePiece.BISHOP, PlayerEnum.PlayerEnum.ONE, r, c, self.rect.topleft)
                    elif c == 4:
                        p = Piece.Piece(GamePiece.GamePiece.QUEEN, PlayerEnum.PlayerEnum.ONE, r, c, self.rect. topleft)
                    elif c == 5:
                        p = Piece.Piece(GamePiece.GamePiece.KING, PlayerEnum.PlayerEnum.ONE, r, c, self.rect.topleft)
                    else:
                        print("ERROR: r=" + str(r) + ", c=" + str(c))
                elif r == 2:  # Player 1 pawns
                    p = Piece.Piece(GamePiece.GamePiece.PAWN, PlayerEnum.PlayerEnum.ONE, r, c, self.rect.topleft)
                elif r == 7:  # Player 2 pawns
                    p = Piece.Piece(GamePiece.GamePiece.PAWN, PlayerEnum.PlayerEnum.TWO, r, c, self.rect.topleft)
                elif r == 8:  # Player 2 pieces
                    if c == 1 or c == 8:
                        p = Piece.Piece(GamePiece.GamePiece.ROOK, PlayerEnum.PlayerEnum.TWO, r, c, self.rect.topleft)
                    elif c == 2 or c == 7:
                        p = Piece.Piece(GamePiece.GamePiece.KNIGHT, PlayerEnum.PlayerEnum.TWO, r, c, self.rect.topleft)
                    elif c == 3 or c == 6:
                        p = Piece.Piece(GamePiece.GamePiece.BISHOP, PlayerEnum.PlayerEnum.TWO, r, c, self.rect.topleft)
                    elif c == 4:
                        p = Piece.Piece(GamePiece.GamePiece.QUEEN, PlayerEnum.PlayerEnum.TWO, r, c, self.rect. topleft)
                    elif c == 5:
                        p = Piece.Piece(GamePiece.GamePiece.KING, PlayerEnum.PlayerEnum.TWO, r, c, self.rect.topleft)
                    else:
                        print("ERROR: r=" + str(r) + ", c=" + str(c))
                else:
                    p = Piece.Piece(GamePiece.GamePiece.NULL, PlayerEnum.PlayerEnum.NULL, r, c, self.rect.topleft)

                grid[Constants.BOARD_ROWS - r][c - 1] = p
                pieces.add(p)

        return grid, pieces
