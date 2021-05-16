import pygame
from Chess.source.assist.Constants import *
from Chess.source.assist.Colors import *
from source.structs import LinkButtons


def start(screen, clock):
    background = pygame.Surface(screen.get_size()).convert()
    background.fill(BLACK)

    font = pygame.font.SysFont("fonts/LemonMilk.otf", 100)
    title = font.render("Chess", True, WHITE)

    font_button = pygame.font.SysFont("fonts/LemonMilk.otf", 30)
    sp_button = LinkButtons.LinkButton("1 Player", WHITE, font_button, 150, 50, 125, 300, DARK_COLOR, LIGHT_COLOR,
                                       BROWN)
    mp_button = LinkButtons.LinkButton("2 Players", WHITE, font_button, 150, 50, 325, 300, DARK_COLOR, LIGHT_COLOR,
                                       BROWN)
    quit_button = LinkButtons.LinkButton("Quit", WHITE, font_button, 150, 50, 525, 300, DARK_COLOR, LIGHT_COLOR, RED)
    buttons = LinkButtons.LinkButtonGroup(sp_button, mp_button, quit_button)

    screen.blit(background, ORIGIN)
    screen.blit(title, ((screen.get_width() / 2) - (font.size("Chess")[0] / 2), 100))

    run = True
    ret = ""
    command = "NO_ACTION"
    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                ret = "QUIT"
            if event.type == pygame.MOUSEMOTION:
                command = buttons.test()
            if event.type == pygame.MOUSEBUTTONDOWN:
                command = buttons.test()
            if event.type == pygame.MOUSEBUTTONUP:
                command = buttons.test()

            if command != "NO_ACTION":
                run = False
                ret = command

        buttons.blit(screen)

        pygame.display.flip()

    # free up a little memory
    del background
    del font
    del title
    del sp_button
    del mp_button
    del quit_button
    del buttons

    return ret
