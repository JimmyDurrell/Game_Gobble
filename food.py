import random
import pygame
from snake import Snake
from screen import Screen


class Food:
    x = -100  # 一开始不显示食物
    y = -100
    color = (0, 200, 0)

    def create_food(self, snake: Snake):
        self.x = random.randint(0, int(Screen.origin_width / Screen.pixel_size) - 1)
        self.y = random.randint(0, int((Screen.origin_height - Screen.bar_height) / Screen.pixel_size) - 1)
        while (self.x, self.y) in snake:
            self.x = random.randint(0, int(Screen.origin_width / Screen.pixel_size) - 1)
            self.y = random.randint(0, int((Screen.origin_height - Screen.bar_height) / Screen.pixel_size) - 1)

    def draw(self, screen: Screen):
        pygame.draw.rect(screen.screen_game, self.color,
                         (self.x * (screen.pixel_size + screen.line_width),
                          self.y * screen.pixel_size + (self.y + 1) * screen.line_width + screen.bar_height,
                          screen.pixel_size, screen.pixel_size), 0)
