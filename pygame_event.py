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
