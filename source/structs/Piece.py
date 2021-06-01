import pygame

from source.assist import Colors, Constants, MathHelp

from source.enums.GamePiece import *
from source.enums.PlayerEnum import *
from source.enums.Orientation import *
from source.enums.SelectionState import *

import source.structs.ChessBoard as ChessBoard


class Piece:
    def __init__(self, piece_type: GamePiece, player: PlayerEnum, row: int, col: int, board_pos: tuple):

        self.row = row
        self.col = col
        self.type = piece_type
        self.direction = Orientation.UP if player == PlayerEnum.ONE else Orientation.DOWN

        self.player = player
        self.color = Colors.WHITE if self.player == PlayerEnum.ONE else Colors.BLACK
        if self.player == PlayerEnum.NULL:
            self.color = Colors.GRAY

        self.font = pygame.font.SysFont("/fonts/LemonMilk.otf", 30)

        self.image_default = self.font.render(self.type.name[0], True, self.color)
        self.image_selected = self.font.render(self.type.name[0], True, Colors.RED)
        self.image = self.image_default

        board_x, board_y = board_pos
        self.x, self.y = MathHelp.snap_topleft(Constants.TILE_SIZE, (board_x + self.col * Constants.TILE_LENGTH,
                                                                     board_y + (9 - self.row) * Constants.TILE_LENGTH),
                                               self.image.get_size())

        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

        self.unmoved = True  # True if the piece hasn't been moved yet (needed for pawns, and castling)

        self.pressed = False

    def toString(self) -> str:
        return str(self.type.name) + ", " + str(self.row) + chr(self.col + 96) + ", Player " + str(self.player.value)

    def test(self, turn: PlayerEnum):
        mouse_state = pygame.mouse.get_pressed(3)
        if turn == self.player and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.pressed = True
            self.image = self.image_selected
            return SelectionState.PIECE_SELECTED, self
        return SelectionState.NO_SELECTION, None

    def select_confirm(self, turn: PlayerEnum):
        self.pressed = True
        self.image = self.image_selected
        return SelectionState.PIECE_CONFIRMED, self


class PieceGroup:
    def __init__(self, *args: Piece):
        self.group = []
        self.selected = None

        self.add(*args)

    def add(self, *args: Piece):
        for p in args:
            self.group.append(p)

    def remove(self, p: Piece) -> Piece:
        x = 0
        while x < len(self.group):
            if self.group[x] is p:
                return self.group.pop(x)
            x += 1

    def blit(self, screen: pygame.display):
        for p in self.group:
            p.blit(screen)

    def test(self, turn: PlayerEnum, event: pygame.event.Event, select_state: SelectionState,
             board) -> str:

        command = None
        print("PRE: " + select_state.name)
        if select_state == SelectionState.NO_SELECTION and event.type == pygame.MOUSEBUTTONDOWN:
            print("should select")
            for p in self.group:
                command, piece = p.test(turn)
                if command != SelectionState.NO_SELECTION:
                    print("selects?: " + command.name)
                    self.selected = piece
                    break
        elif select_state == SelectionState.PIECE_SELECTED:
            if event.type == pygame.MOUSEBUTTONUP:
                print("should confirm")
                command, self.selected = self.selected.select_confirm(turn)
            else:
                print("ERROR: piece selected, not confirmed, then test without button up")
        elif select_state == SelectionState.PIECE_CONFIRMED:
            # Display available moves
            pass
        #elif select_state == SelectionState.MOVE_SELECTED:
            # handle btn up
        print("POST: " + command.name)
        return command

