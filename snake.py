from collections import deque
import pygame
from screen import Screen


class Snake(deque):
    body_color = (200, 200, 200)
    head_color = (200, 100, 100)
    direction = 'right'
    speed = 0.8

    def init(self):
        self.clear()
        self.direction = 'right'
        self.appendleft((int(Screen.origin_width / Screen.pixel_size / 2), int((Screen.origin_height - Screen.bar_height) / Screen.pixel_size / 2)))
        self.appendleft((int(Screen.origin_width / Screen.pixel_size / 2) - 1, int((Screen.origin_height - Screen.bar_height) / Screen.pixel_size / 2)))
        self.appendleft((int(Screen.origin_width / Screen.pixel_size / 2) - 2, int((Screen.origin_height - Screen.bar_height) / Screen.pixel_size / 2)))

    def reset(self):
        self.init()

    """还需要修改"""
    # def eat_food(self, eaten_food, keyboard: str):
    #     # return self[-1] == (eaten_food.x, eaten_food.y)
    #     match self.direction:
    #         case "up":
    #             return (keyboard != "left" and keyboard != "right" and self[-1] == (eaten_food.x, eaten_food.y + 1)) \
    #                 or (keyboard == "left" and self[-1] == (eaten_food.x + 1, eaten_food.y))
    #         case "down":
    #             return self[-1] == (eaten_food.x, eaten_food.y - 1)
    #         case "left":
    #             return self[-1] == (eaten_food.x + 1, eaten_food.y)
    #         case "right":
    #             return self[-1] == (eaten_food.x - 1, eaten_food.y)
    #         case _:
    #             pass

    def is_food_ahead(self, food, direct) -> bool:
        match direct:
            case "up":
                return (self[-1] == (food.x, food.y + 1) or
                        self[-1] == (food.x, food.y - (int((Screen.origin_height - Screen.bar_height) / Screen.pixel_size) - 1)))
            case "down":
                return (self[-1] == (food.x, food.y - 1) or
                        self[-1] == (food.x, food.y + (int((Screen.origin_height - Screen.bar_height) / Screen.pixel_size) - 1)))
            case "left":
                return (self[-1] == (food.x + 1, food.y) or
                        self[-1] == (food.x - (int(Screen.origin_width / Screen.pixel_size) - 1), food.y))
            case "right":
                return (self[-1] == (food.x - 1, food.y) or
                        self[-1] == (food.x + (int(Screen.origin_width / Screen.pixel_size) - 1), food.y))
            case _:
                return False

    def is_food_up(self, food, direct) -> bool:
        if direct == "left" or direct == "right":
            return self.is_food_ahead(food, "up")
        else:
            return False

    def is_food_down(self, food, direct) -> bool:
        if direct == "left" or direct == "right":
            return self.is_food_ahead(food, "down")
        else:
            return False

    def is_food_right(self, food, direct) -> bool:
        if direct == "up" or direct == "down":
            return self.is_food_ahead(food, "right")
        else:
            return False

    def is_food_left(self, food, direct) -> bool:
        if direct == "up" or direct == "down":
            return self.is_food_ahead(food, "left")
        else:
            return False

    def faster(self):
        if self.speed > 0.7:
            self.speed -= 0.02
        elif self.speed > 0.5:
            self.speed -= 0.015
        elif self.speed > 0.3:
            self.speed -= 0.012
        elif self.speed > 0.2:
            self.speed -= 0.01
        else:
            pass

    # def longer(self, loc: tuple):
    #     self.append(loc)

    def is_direction_horizontal(self):
        return self.direction == "left" or self.direction == "right"

    def is_direction_vertical(self):
        return self.direction == "up" or self.direction == "down"

    def move_up(self, eat_flag: bool):
        self.direction = "up"
        if not eat_flag:
            self.popleft()
        if self[-1][1] == 0:
            self.append((self[-1][0], int((Screen.origin_height - Screen.bar_height) / Screen.pixel_size) - 1))
        else:
            self.append((self[-1][0], self[-1][1] - 1))

    def move_down(self, eat_flag: bool):
        self.direction = "down"
        if not eat_flag:
            self.popleft()
        if self[-1][1] == int((Screen.origin_height - Screen.bar_height) / Screen.pixel_size) - 1:
            self.append((self[-1][0], 0))
        else:
            self.append((self[-1][0], self[-1][1] + 1))

    def move_left(self, eat_flag: bool):
        self.direction = "left"
        if not eat_flag:
            self.popleft()
        if self[-1][0] == 0:
            self.append((int(Screen.origin_width / Screen.pixel_size) - 1, self[-1][1]))
        else:
            self.append((self[-1][0] - 1, self[-1][1]))

    def move_right(self, eat_flag: bool):
        self.direction = "right"
        if not eat_flag:
            self.popleft()
        if self[-1][0] == int(Screen.origin_width / Screen.pixel_size) - 1:
            self.append((0, self[-1][1]))
        else:
            self.append((self[-1][0] + 1, self[-1][1]))

    def move(self, eat_flag: bool):
        match self.direction:
            case "up":
                self.move_up(eat_flag)
            case "down":
                self.move_down(eat_flag)
            case "left":
                self.move_left(eat_flag)
            case "right":
                self.move_right(eat_flag)
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
