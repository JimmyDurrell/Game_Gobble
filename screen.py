import pygame


class Screen:

    origin_width = 400
    origin_height = 400
    pixel_size = 20  # 一个游戏点的大小
    bar_height = pixel_size * 2  # 显示栏的高度
    line_width = 1  # # 游戏点之间的线的宽度
    width = int(origin_width / pixel_size) - 1 + origin_width
    height = int((origin_height - bar_height) / pixel_size) + origin_height
    size = (width, height)

    background_color = (80, 80, 100)
    line_color = (0, 0, 0)  # 游戏点之间的线
    button_color = (200, 200, 200)
    font_color = (255, 255, 255)
    shadow_color = (50, 50, 50)

    shadow_offset = 3
    button_rect_start = pygame.Rect(width / 2 - 100, 175, 200, 50)
    button_rect_exit = pygame.Rect(width / 2 - 100, 250, 200, 50)
    screen_game = pygame.display.set_mode(size)  # 定义窗口大小

    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        # 制作窗口
        pygame.display.set_caption("贪吃蛇")  # 定义标题

    def background(self):
        self.screen_game.fill(self.background_color)  # 填充背景色
        self.draw_lines()

    def draw_lines(self):
        # 画网格竖线
        for x in range(self.pixel_size, self.width, self.pixel_size + 1):
            pygame.draw.line(self.screen_game, self.line_color, (x, self.bar_height), (x, self.height),
                             self.line_width)
        # 画网格横线
        for y in range(self.bar_height, self.height, self.pixel_size + 1):
            pygame.draw.line(self.screen_game, self.line_color, (0, y), (self.width, y), self.line_width)

    def start_menu(self):
        # 设置字体
        font = pygame.font.Font(None, 48)

        # 标题
        text_welcome = font.render("Welcome to Gobble!", True, self.font_color)
        text_rect = text_welcome.get_rect(center=(self.width / 2, 100))
        # 绘制标题文本
        self.screen_game.blit(text_welcome, text_rect)

        # 开始按钮
        button_text_start = font.render("Start", True, self.font_color)
        button_text_start_rect = button_text_start.get_rect(center=self.button_rect_start.center)
        # 绘制开始按钮阴影
        shadow_rect = pygame.Rect(self.button_rect_start.left + self.shadow_offset, self.button_rect_start.top + self.shadow_offset,
                                  self.button_rect_start.width, self.button_rect_start.height)
        pygame.draw.rect(self.screen_game, self.shadow_color, shadow_rect)
        # 绘制开始按钮
        pygame.draw.rect(self.screen_game, self.button_color, self.button_rect_start)
        self.screen_game.blit(button_text_start, button_text_start_rect)

        # 退出按钮
        button_text_exit = font.render("Exit", True, self.font_color)
        button_text_exit_rect = button_text_exit.get_rect(center=self.button_rect_exit.center)
        # 绘制退出按钮阴影
        shadow_rect = pygame.Rect(self.button_rect_exit.left + self.shadow_offset,
                                  self.button_rect_exit.top + self.shadow_offset,
                                  self.button_rect_exit.width, self.button_rect_exit.height)
        pygame.draw.rect(self.screen_game, self.shadow_color, shadow_rect)
        # 绘制退出按钮
        pygame.draw.rect(self.screen_game, self.button_color, self.button_rect_exit)
        self.screen_game.blit(button_text_exit, button_text_exit_rect)


if __name__ == "__main__":
    pass
