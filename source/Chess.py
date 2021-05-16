import pygame

import source.assist.Constants as Constants

from source.screens import GameScreen, MultiplayerSelectionScreen, TitleScreen


def main():
    pygame.init()
    pygame.display.set_caption("Chess")

    screen = pygame.display.set_mode(Constants.SCREEN_SIZE)

    run = True
    clock = pygame.time.Clock()
    while run:
        title = TitleScreen.start(screen, clock)
        if title == "QUIT":
            run = False

        else:
            if title == "1 PLAYER":
                game = GameScreen.start(screen, clock)
                break  # TODO: Change this ?
            elif title == "2 PLAYERS":  # TODO: Multi player
                game = MultiplayerSelectionScreen.start()
                break  # TODO: Change this ?
            else:
                print("error:", title)
                run = False
                break


if __name__ == "__main__":
    main()
