import pygame

import Colors

import ChessBoard


def start(screen: pygame.Surface, clock: pygame.time.Clock):
    background = pygame.Surface(screen.get_size()).convert()
    background.fill(Colors.BLACK)

    board = ChessBoard.ChessBoard(10, 10)

    run = True
    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.blit(background, (0, 0))
        screen.blit(board.image, board.rect.topleft)
        pygame.display.flip()
