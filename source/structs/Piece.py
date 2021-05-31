import pygame

from source.assist import Colors, Constants, MathHelp

from source.enums.GamePiece import *
from source.enums.PlayerEnum import *
from source.enums.Orientation import *


class Piece:
    def __init__(self, piece_type: GamePiece, player: PlayerEnum,
                 color: pygame.Color, row: int, col: int, board_pos: tuple):

        self.row = row
        self.col = col
        self.type = piece_type
        self.direction = Orientation.UP if player == PlayerEnum.ONE else Orientation.DOWN

        self.player = player
        self.color = color

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

        self.pressed = False

    def toString(self) -> str:
        return str(self.type.name) + ", " + str(self.row) + chr(self.col + 96)

    def test(self, turn: PlayerEnum):
        mouse_state = pygame.mouse.get_pressed(3)
        if turn == self.player and self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.pressed:
                if mouse_state[0] == 0:
                    self.pressed = False
                    self.image = self.image_default
                    return self.toString()
            else:
                if mouse_state[0] == 1:
                    self.pressed = True
                    self.image = self.image_selected
        else:
            self.image = self.image_default
            self.pressed = False
        return "NO_ACTION"


class PieceGroup:
    def __init__(self, *args: Piece):
        self.group = []

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

    def test(self, turn: PlayerEnum) -> str:
        command = "NO_ACTION"
        for p in self.group:
            command = p.test(turn)
            if command != "NO_ACTION":
                return command
        return command

