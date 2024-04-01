import pygame
from screen import Screen
from snake import Snake
from food import Food
import time
from pygame_event import pygame_process_event, esc_event


def Update_All():
    game_screen.background()
    snake.draw(game_screen)
    food.draw(game_screen)


def Init_All():
    snake.init()
    food.create_food(snake)
    Update_All()
    game_screen.start_menu()


def Reset_All():
    Init_All()


if __name__ == "__main__":
    game_screen = Screen()
    snake = Snake()
    food = Food()
    eat_flag = False

    event_dict = {"enter": False, "esc": False, "space": False,
                  "left": False, "right": False, "up": False, "down": False,
                  "mouse": False, "start": False,
                  "default": False}
    last_time = time.time()

    Init_All()
    pygame.display.update()
    while True:
        word = pygame_process_event(game_screen)
        event_dict[word] = not event_dict[word]
        if event_dict["start"]:
            if event_dict["esc"]:
                esc_event(game_screen)
                if event_dict["enter"]:
                    Reset_All()
                    pygame.display.flip()
                    event_dict["enter"] = event_dict["esc"] = event_dict["start"] = False
            else:
                Update_All()
                pygame.display.update()

                if event_dict["up"]:
                    event_dict["up"] = False
                    if snake.is_direction_horizontal():
                        snake.move_up(eat_flag := snake.is_food_up(food, snake.direction))
                        last_time = time.time()
                elif event_dict["down"]:
                    event_dict["down"] = False
                    if snake.is_direction_horizontal():
                        snake.move_down(eat_flag := snake.is_food_down(food, snake.direction))
                        last_time = time.time()
                elif event_dict["left"]:
                    event_dict["left"] = False
                    if snake.is_direction_vertical():
                        snake.move_left(eat_flag := snake.is_food_left(food, snake.direction))
                        last_time = time.time()
                elif event_dict["right"]:
                    event_dict["right"] = False
                    if snake.is_direction_vertical():
                        snake.move_right(eat_flag := snake.is_food_right(food, snake.direction))
                        last_time = time.time()
                else:  # 没有按键按下
                    now_time = time.time()
                    if now_time - last_time > snake.speed:
                        snake.move(eat_flag := snake.is_food_ahead(food, snake.direction))
                        last_time = now_time

                if eat_flag:
                    eat_flag = False
                    snake.faster()
                    food.create_food(snake)

        elif event_dict["mouse"]:
            time.sleep(0.15)
            Update_All()
            pygame.display.flip()
            event_dict["start"] = True
            event_dict["mouse"] = False
        else:
            pass
