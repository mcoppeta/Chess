from enum import Enum


class SelectionState(Enum):
    NO_SELECTION = 0
    PIECE_SELECTED = 1
    PIECE_CONFIRMED = 2
    MOVE_SELECTED = 3
    MOVE_CONFIRMED = 4
