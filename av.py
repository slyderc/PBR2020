import time
import pygame
from utils import debug

SOUND_PATH = '/home/cdimick/PBR2020/sounds'
MUSIC_PATH = '/home/cdimick/PBR2020/music'


def init_sound():
    """Setup the PyGame audio mixer and initialize"""
    pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.mixer.init()


def play_sound(sound_file, wait=False):
    sfx = pygame.mixer.Sound(f'{SOUND_PATH}/{sound_file}')
    sfx.set_volume(1.0)
    sfx.play()
    if wait:
        time.sleep(1)


def play_music(music_file):
    pygame.mixer.music.load(f'{MUSIC_PATH}/{music_file}')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()


def push_pixels(fadecandy, cups):
    """ Push our pixels out to the Fadecandy """
    fadecandy.put_pixels(cups)


def update_matrix(command_string):
    debug(f"MATRIX: {command_string}")
