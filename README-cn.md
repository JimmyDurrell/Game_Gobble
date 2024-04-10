# Game_Gobble（中文版）

## 欢迎

这是一个经典的游戏。

双击`build`文件夹下的`gobble.exe`文件或者运行下面这个脚本来启动。

`python gobble.py`

玩得开心。

## 游戏指导

点击`Start`按钮开始游戏或者点击`Exit`按钮退出游戏。

当游戏开始后，按上下左右四个方向键操控小蛇来吃食物以及避免碰撞，这样才能生存继续游戏。如果有事需要离开，按下`Esc`键来暂停游戏。接下来有两种选择：

- 再按下`Esc`键继续游戏。
- 按下`Enter`键返回开始菜单。

当时吃到自己或者撞到黑色障碍物，游戏结束。需要注意的时，游戏会自动生成一个名为`score.txt`的文件来记录分数。接下来又有两种选择：

- 再按下`Enter`键重玩游戏。
- 按下`Esc`键返回开始菜单。

## 文件介绍

`main.py`: 没啥用

`gobble.py`: 游戏主文件

`snake.py`: 定义了蛇的类，包含一些动作的方法。

`food.py`: 定义了食物的类。

`pygame_event.py`: 一些监听时间的函数。

`screen.py`: 定义了屏幕的类，管理游戏的界面。

`barrier.py`: 定义了障碍物的类，生成障碍物。

`music.py`: 管理背景音乐的播放。

`music`: 包含四个音频文件。

`build` & `dist` & `gobble.spec`: pyinstaller生成的。

`gobble.ico` & `gobble2.ico`: gobble.exe文件的图标。

- 运行`pyinstaller -F -w -i [.ico file] [.py file]` 可生成.exe文件。