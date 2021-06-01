import pygame

from source.assist import MathHelp, Colors, Constants

from source.structs import ChessBoard

from source.enums.PlayerEnum import PlayerEnum
from source.enums.SelectionState import SelectionState


def start(screen: pygame.Surface, clock: pygame.time.Clock):
    background = pygame.Surface(screen.get_size()).convert()
    background.fill(Colors.BLACK)

    board = ChessBoard.ChessBoard("standard", *(MathHelp.snap_topleft(screen.get_size(), Constants.ORIGIN,
                                                                      Constants.BOARD_SIZE)))

    turn = PlayerEnum.ONE
    played = False
    selection_state = SelectionState.NO_SELECTION
    command = SelectionState.NO_SELECTION
    last_command = SelectionState.NO_SELECTION

    run = True
    while run:
        clock.tick(Constants.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    played = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                command = board.pieces.test(turn, event, selection_state)
            if event.type == pygame.MOUSEBUTTONUP:
                command = board.pieces.test(turn, event, selection_state)

            if command != last_command:
                print("loop: " + str(command.name))
                last_command = command
                selection_state = command

        screen.blit(background, Constants.ORIGIN)

        board.blit(screen)
        if selection_state == SelectionState.MOVE_CONFIRMED:
            board.blit_moves(screen, board.pieces.selected)
        board.blit_pieces(screen)

        pygame.display.flip()

        if played:
            if turn == PlayerEnum.ONE:
                turn = PlayerEnum.TWO
            elif turn == PlayerEnum.TWO:
                turn = PlayerEnum.ONE
            else:
                turn = PlayerEnum.NULL
            print("It is now Player " + turn.name + "'s turn!")
            played = not played
