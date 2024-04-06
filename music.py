import pygame


class Music:
    def __init__(self):
        pass

    @staticmethod
    def play_music(music_file: str, is_loop: bool = True):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1 if is_loop else 0)  # 开始播放音乐，-1表示无限循环

    @staticmethod
    def add_music(music_file: str, is_loop: bool = True):
        sound_effect = pygame.mixer.Sound(music_file)
        sound_effect.play(-1 if is_loop else 0)

    @staticmethod
    def pause_music():
        pygame.mixer.music.pause()

    @staticmethod
    def unpause_music():
        pygame.mixer.music.unpause()
