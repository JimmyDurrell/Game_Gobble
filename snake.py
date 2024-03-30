from collections import deque
import pygame
from screen import Screen


class Snake(deque):
    body_color = (200, 200, 200)
    head_color = (200, 100, 100)
    direction = 'right'
    speed = 1

    def init(self):
        self.clear()
        self.direction = 'right'
        self.appendleft((int(Screen.origin_width / Screen.pixel_size / 2), int((Screen.origin_height - Screen.bar_height) / Screen.pixel_size / 2)))
        self.appendleft((int(Screen.origin_width / Screen.pixel_size / 2) - 1, int((Screen.origin_height - Screen.bar_height) / Screen.pixel_size / 2)))
        self.appendleft((int(Screen.origin_width / Screen.pixel_size / 2) - 2, int((Screen.origin_height - Screen.bar_height) / Screen.pixel_size / 2)))

    def reset(self):
        self.init()

    def is_direction_horizontal(self):
        return self.direction == "left" or self.direction == "right"

    def is_direction_vertical(self):
        return self.direction == "up" or self.direction == "down"

    def move_up(self):
        self.direction = "up"
        self.popleft()
        if self[-1][1] == 0:
            self.append((self[-1][0], int((Screen.origin_height - Screen.bar_height) / Screen.pixel_size) - 1))
        else:
            self.append((self[-1][0], self[-1][1] - 1))

    def move_down(self):
        self.direction = "down"
        self.popleft()
        if self[-1][1] == int((Screen.origin_height - Screen.bar_height) / Screen.pixel_size) - 1:
            self.append((self[-1][0], 0))
        else:
            self.append((self[-1][0], self[-1][1] + 1))

    def move_left(self):
        self.direction = "left"
        self.popleft()
        if self[-1][0] == 0:
            self.append((int(Screen.origin_width / Screen.pixel_size) - 1, self[-1][1]))
        else:
            self.append((self[-1][0] - 1, self[-1][1]))

    def move_right(self):
        self.direction = "right"
        self.popleft()
        if self[-1][0] == int(Screen.origin_width / Screen.pixel_size) - 1:
            self.append((0, self[-1][1]))
        else:
            self.append((self[-1][0] + 1, self[-1][1]))

    def move(self, direct):
        match direct:
            case "up":
                self.move_up()
            case "down":
                self.move_down()
            case "left":
                self.move_left()
            case "right":
                self.move_right()
            case _:
                pass

    def draw(self, screen: Screen):
        for i in range(len(self)):
            if i == len(self) - 1:
                pygame.draw.rect(screen.screen_game, self.head_color,
                                 (self[i][0] * (screen.pixel_size + screen.line_width),
                                  self[i][1] * screen.pixel_size + (self[i][1] + 1) * screen.line_width + screen.bar_height,
                                  screen.pixel_size, screen.pixel_size), 0)
            else:
                pygame.draw.rect(screen.screen_game, self.body_color,
                                 (self[i][0] * (screen.pixel_size + screen.line_width),
                                  self[i][1] * screen.pixel_size + (self[i][1] + 1) * screen.line_width + screen.bar_height,
                                  screen.pixel_size, screen.pixel_size), 0)
