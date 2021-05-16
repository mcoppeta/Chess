import pygame

from source.assist import MathHelp, Colors, Constants

from source.structs import ChessBoard


def start(screen: pygame.Surface, clock: pygame.time.Clock):
    background = pygame.Surface(screen.get_size()).convert()
    background.fill(Colors.BLACK)

    board = ChessBoard.ChessBoard("standard", *(MathHelp.snap_topleft(screen.get_size(), Constants.ORIGIN,
                                                                      Constants.BOARD_SIZE)))

    run = True
    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.blit(background, (0, 0))

        board.blit(screen)
        board.blit_pieces(screen)

        pygame.display.flip()
