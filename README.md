# Game_Gobble

## Welcome

This is a classic game. To play it, run the script below or double-click the `gobble.exe` file in build directory.

> python gobble.py

Enjoy it.

## Game Instruction

Click the Start Button to play or the Exit Button to exit.

When you are playing, press Esc to stop the game.

- Press Esc again to resume.
- Press Enter to return to the Start Menu.

When you eat yourself or hit the barrier, the game is over. To remind you, a file name "score.txt" is automatically generated to record your score.

- Then press Enter to restart the game.
- Or press Esc to return to the Start Menu.

## File Instruction

main.py: just ignore it.

gobble.py: the main file.

snake.py: define a Snake class, containing some motions.

food.py: define a Food class.

pygame_event.py: some functions monitoring the event.

screen.py: define a Screen class, to control the interface of the game.

barrier.py: define Barrier class, to create barriers for snake.

build & dist & gobble.spec: pyinstaller help me generate that.