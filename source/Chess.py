import pygame

import Colors
import TitleScreen
import Constants


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
            if title == "1 PLAYER":  # TODO: MAKE GAME FUNC -> THIS PREVENTS QUITTING
                bg = pygame.Surface(screen.get_size()).convert()
                bg.fill(Colors.BLACK)
                while 1:
                    screen.blit(bg, Constants.ORIGIN)
                    pygame.display.flip()
            elif title == "2 PLAYERS":  # TODO: MAKE GAME FUNC -> THIS PREVENTS QUITTING
                bg = pygame.Surface(screen.get_size()).convert()
                bg.fill(Colors.BLACK)
                while 1:
                    screen.blit(bg, Constants.ORIGIN)
                    pygame.display.flip()
            else:
                print("error:", title)
                run = False
                break;


if __name__ == "__main__":
    main()
