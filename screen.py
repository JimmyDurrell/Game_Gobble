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
    screen_game = pygame.display.set_mode(size)  # 定义窗口大小

    # 设置颜色
    background_color = (80, 80, 100)
    line_color = (0, 0, 0)  # 游戏点之间的线
    button_color = (200, 200, 200)
    text_color = (255, 255, 255)
    text_over_color = (213, 0, 0)
    text_background_color = (100, 100, 100)
    shadow_color = (50, 50, 50)

    shadow_offset = 3
    button_rect_start = pygame.Rect(width / 2 - 100, 175, 200, 50)
    button_rect_exit = pygame.Rect(width / 2 - 100, 250, 200, 50)

    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        # 制作窗口
        pygame.display.set_caption("贪吃蛇")  # 定义标题

        # 设置字体
        self.font_start_menu = pygame.font.Font(None, 48)
        self.font_score = pygame.font.SysFont('SimHei', 20)  # 得分的字体
        self.font_over = pygame.font.Font(None, 72)  # GAME OVER 的字体
        self.font_esc = pygame.font.Font(None, 36)

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

    def display_score(self, score):
        imgText = self.font_score.render(f"得分: {score}", True, self.text_color)
        self.screen_game.blit(imgText, (self.width - 110, 10))

    def start_menu(self):
        # 标题
        text_welcome = self.font_start_menu.render("Welcome to Gobble!", True, self.text_color)
        text_rect = text_welcome.get_rect(center=(self.width / 2, 100))
        # 绘制标题文本
        self.screen_game.blit(text_welcome, text_rect)

        # 开始按钮
        button_text_start = self.font_start_menu.render("Start", True, self.text_color)
        button_text_start_rect = button_text_start.get_rect(center=self.button_rect_start.center)
        # 绘制开始按钮阴影
        shadow_rect = pygame.Rect(self.button_rect_start.left + self.shadow_offset,
                                  self.button_rect_start.top + self.shadow_offset,
                                  self.button_rect_start.width, self.button_rect_start.height)
        pygame.draw.rect(self.screen_game, self.shadow_color, shadow_rect)
        # 绘制开始按钮
        pygame.draw.rect(self.screen_game, self.button_color, self.button_rect_start)
        self.screen_game.blit(button_text_start, button_text_start_rect)

        # 退出按钮
        button_text_exit = self.font_start_menu.render("Exit", True, self.text_color)
        button_text_exit_rect = button_text_exit.get_rect(center=self.button_rect_exit.center)
        # 绘制退出按钮阴影
        shadow_rect = pygame.Rect(self.button_rect_exit.left + self.shadow_offset,
                                  self.button_rect_exit.top + self.shadow_offset,
                                  self.button_rect_exit.width, self.button_rect_exit.height)
        pygame.draw.rect(self.screen_game, self.shadow_color, shadow_rect)
        # 绘制退出按钮
        pygame.draw.rect(self.screen_game, self.button_color, self.button_rect_exit)
        self.screen_game.blit(button_text_exit, button_text_exit_rect)
        
    def esc_menu(self):
        # 如果处于暂停状态，显示一个简单的弹出界面
        text1 = self.font_esc.render("Paused. Press ESC to continue.", True, self.text_color)
        text2 = self.font_esc.render("Or press Enter to return", True, self.text_color)
        text_rect1 = text1.get_rect(center=(self.width / 2, self.height / 2 - 20))
        text_rect2 = text2.get_rect(center=(self.width / 2, self.height / 2 + 20))
        pygame.draw.rect(self.screen_game, self.text_background_color, text_rect1.inflate(20, 20))  # 绘制背景
        pygame.draw.rect(self.screen_game, self.text_background_color, text_rect2.inflate(20, 20))  # 绘制背景
        self.screen_game.blit(text1, text_rect1)  # 绘制文本
        self.screen_game.blit(text2, text_rect2)  # 绘制文本

        # 更新屏幕
        pygame.display.update()

    def end_menu(self, score, max_score):
        # 标题
        text_welcome = self.font_over.render("Game Over", True, self.text_over_color)
        text_rect = text_welcome.get_rect(center=(self.width / 2, 100))
        # 绘制标题文本
        self.screen_game.blit(text_welcome, text_rect)

        # Press Enter to Restart. Or press Esc to return
        text1 = self.font_esc.render("Press Enter to Restart.", True, self.text_color)
        text2 = self.font_esc.render("Or press Esc to return", True, self.text_color)
        text_rect1 = text1.get_rect(center=(self.width / 2, self.height / 2 - 20))
        text_rect2 = text2.get_rect(center=(self.width / 2, self.height / 2 + 20))
        pygame.draw.rect(self.screen_game, self.text_background_color, text_rect1.inflate(20, 20))  # 绘制背景
        pygame.draw.rect(self.screen_game, self.text_background_color, text_rect2.inflate(20, 20))  # 绘制背景
        self.screen_game.blit(text1, text_rect1)  # 绘制文本
        self.screen_game.blit(text2, text_rect2)  # 绘制文本

        # score and max_score
        text3 = self.font_esc.render(f"Your Score: {score}", True, self.text_color)
        text4 = self.font_esc.render(f"Max Score: {max_score}", True, self.text_color)
        text_rect3 = text3.get_rect(center=(self.width / 2, self.height / 2 + 80))
        text_rect4 = text4.get_rect(center=(self.width / 2, self.height / 2 + 110))
        pygame.draw.rect(self.screen_game, self.text_background_color, text_rect3.inflate(20, 20))  # 绘制背景
        pygame.draw.rect(self.screen_game, self.text_background_color, text_rect4.inflate(20, 20))  # 绘制背景
        self.screen_game.blit(text3, text_rect3)  # 绘制文本
        self.screen_game.blit(text4, text_rect4)  # 绘制文本

        # 更新屏幕
        pygame.display.update()


if __name__ == "__main__":
    pass
