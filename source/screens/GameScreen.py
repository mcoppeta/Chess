import pygame

from source.assist import MathHelp, Colors, Constants

from source.structs import ChessBoard

from source.enums.PlayerEnum import PlayerEnum


def start(screen: pygame.Surface, clock: pygame.time.Clock):
    background = pygame.Surface(screen.get_size()).convert()
    background.fill(Colors.BLACK)

    board = ChessBoard.ChessBoard("standard", *(MathHelp.snap_topleft(screen.get_size(), Constants.ORIGIN,
                                                                      Constants.BOARD_SIZE)))

    turn = PlayerEnum.ONE
    played = False

    run = True
    while run:
        clock.tick(Constants.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    played = True
            if event.type == pygame.MOUSEMOTION:
                command = board.pieces.test(turn)
            if event.type == pygame.MOUSEBUTTONDOWN:
                command = board.pieces.test(turn)
            if event.type == pygame.MOUSEBUTTONUP:
                command = board.pieces.test(turn)

            if command != "NO_ACTION":
                print(command)

        screen.blit(background, Constants.ORIGIN)

        board.blit(screen)
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
