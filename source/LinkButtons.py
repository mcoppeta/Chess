import pygame


class LinkButton:
    def __init__(self, text: str, text_color: tuple, font: pygame.font.Font, width: int, height: int,
                 xpos: int, ypos: int, bg_color: tuple, hover_color: tuple, press_color: tuple):
        self.img_standard = pygame.Surface((width, height)).convert()
        self.img_standard.fill(bg_color)
        self.img_hover = pygame.Surface((width, height)).convert()
        self.img_hover.fill(hover_color)
        self.img_press = pygame.Surface((width, height)).convert()
        self.img_press.fill(press_color)

        self.image = self.img_standard
        self.image_pos = (xpos, ypos)

        self.text = text

        self.rect = self.image.get_rect()
        self.rect.topleft = self.image_pos

        self.label = font.render(text, True, text_color)
        self.label_w, self.label_h = font.size(text)
        self.label_pos = (xpos + int((width - self.label_w) / 2),
                          ypos + int((height - self.label_h) / 2))

        self.selected = False

    def blit(self, screen: pygame.Surface):
        screen.blit(self.image, self.image_pos)
        screen.blit(self.label, self.label_pos)

    def test(self) -> str:
        mouse_state = pygame.mouse.get_pressed(3)
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.selected:
                if mouse_state[0] == 0:
                    self.selected = False
                    self.image = self.img_hover
                    return self.action()
            else:
                if mouse_state[0] == 1:
                    self.selected = True
                    self.image = self.img_press
                else:
                    self.image = self.img_hover
        else:
            self.image = self.img_standard
            self.selected = False
        return "NO_ACTION"

    def action(self) -> str:
        return self.text.upper()


class LinkButtonGroup:
    def __init__(self, *args: LinkButton):
        self.group = []

        self.add(*args)

    def add(self, *args: LinkButton):
        for btn in args:
            self.group.append(btn)

    def remove(self, btn: LinkButton) -> LinkButton:
        x = 0
        while x < len(self.group):
            if self.group[x] is btn:
                return self.group.pop(x)
            x += 1

    def blit(self, screen: pygame.display):
        for btn in self.group:
            btn.blit(screen)

    def test(self) -> str:
        command = "NO_ACTION"
        for btn in self.group:
            command = btn.test()
            if command != "NO_ACTION":
                return command
        return command
