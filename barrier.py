from collections import deque
from screen import Screen
import pygame


class Barrier(deque):
    color = (0, 0, 0)

    def draw(self, screen: Screen):
        for tp in self:
            pygame.draw.rect(screen.screen_game, self.color,
                             (tp[0] * (screen.pixel_size + screen.line_width),
                              tp[1] * screen.pixel_size + (tp[1] + 1) * screen.line_width + screen.bar_height,
                              screen.pixel_size, screen.pixel_size), 0)

    @classmethod
    def create_barrier(cls, num):
        match num:
            case 1:
                return cls([(0, 0), (0, 1), (0, 2)])
            case _:
                return cls([(0, 0), (1, 0), (2, 0)])
