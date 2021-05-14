import pygame

import Colors
import Constants

import TitleScreen
import MultiplayerSelectionScreen
import GameScreen


def main():
    pygame.init()
    pygame.display.set_caption("Chess")

    screen = pygame.display.set_mode((800, 550))

    run = True
    clock = pygame.time.Clock()
    while run:
        title = TitleScreen.start(screen, clock)
        if title == "QUIT":
            run = False

        else:
            if title == "1 PLAYER":
                game = GameScreen.start()
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
