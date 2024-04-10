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
    def create_barrier(cls):
        return cls(
            [
                (3, 3), (4, 3), (5, 3), (6, 3), (7, 3),
                (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (5, 12), (5, 13),
                (3, 14), (4, 14), (5, 14), (6, 14), (7, 14),

                (11, 3), (12, 3), (13, 3), (14, 3), (15, 3), (16, 3),
                (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12), (11, 13),
                (11, 14), (12, 14), (13, 14), (14, 14), (15, 14), (16, 14)
            ]
        )
        # match num:
        #     case 1:
        #         return cls([(0, 0), (0, 1), (0, 2)])
        #     case _:
        #         return cls([(0, 0), (1, 0), (2, 0)])
