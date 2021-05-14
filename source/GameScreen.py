import pygame


def start(screen: pygame.Surface, clock: pygame.time.Clock):
    run = True
    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip()
