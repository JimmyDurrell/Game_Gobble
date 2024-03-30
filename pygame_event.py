import pygame
import sys
from screen import Screen


def pygame_process_event(screen: Screen) -> str:
    # dict1 = {"enter": False, "esc": False, "space": False, "left": False, "right": False, "up": False, "down": False}
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return "enter"  # dict1["enter"] = True
            elif event.key == pygame.K_ESCAPE:
                return "esc"  # dict1["esc"] = True
            elif event.key == pygame.K_SPACE:
                return "space"  # dict1["space"] = True
            elif event.key == pygame.K_LEFT:
                return "left"  # dict1["left"] = True
            elif event.key == pygame.K_RIGHT:
                return "right"  # dict1["right"] = True
            elif event.key == pygame.K_UP:
                return "up"  # dict1["up"] = True
            elif event.key == pygame.K_DOWN:
                return "down"  # dict1["down"] = True
            else:
                pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if screen.button_rect_start.collidepoint(event.pos):
                print("Start Game!")
                return "mouse"
            elif screen.button_rect_exit.collidepoint(event.pos):
                print("Exit Game")
                pygame.quit()
                sys.exit()
            else:
                pass
        else:
            pass

    return "default"


def esc_event(screen: Screen):
    text_color = (255, 255, 255)
    text_background_color = (100, 100, 100)
    # 设置字体
    font = pygame.font.Font(None, 36)
    # 如果处于暂停状态，显示一个简单的弹出界面
    text1 = font.render("Paused. Press ESC to continue.", True, text_color)
    text2 = font.render("Or press Enter to return", True, text_color)
    text_rect1 = text1.get_rect(center=(screen.width / 2, screen.height / 2 - 20))
    text_rect2 = text2.get_rect(center=(screen.width / 2, screen.height / 2 + 20))
    pygame.draw.rect(screen.screen_game, text_background_color, text_rect1.inflate(20, 20))  # 绘制背景
    pygame.draw.rect(screen.screen_game, text_background_color, text_rect2.inflate(20, 20))  # 绘制背景
    screen.screen_game.blit(text1, text_rect1)  # 绘制文本
    screen.screen_game.blit(text2, text_rect2)  # 绘制文本

    # 更新屏幕
    pygame.display.update()
