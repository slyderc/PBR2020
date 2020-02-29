import time
import pygame
from utils import config, debug
import bibliopixel.colors as colors


def init_sound():
    """Setup the PyGame audio mixer and initialize"""
    pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.mixer.init()


def play_sound(sound_file, wait=False):
    """ Play the given sound file, prefixed with config. game_path/sounds """
    sfx = pygame.mixer.Sound(f"{config['defaults']['game_path']}/sounds/{sound_file}")
    sfx.set_volume(1.0)
    sfx.play()
    if wait:
        time.sleep(1)
    debug(f"Sound: {sound_file}")


def play_music(music_file):
    """ Play the given music file, prefixed with config. game_path/music """
    pygame.mixer.music.load(f"{config['defaults']['game_path']}/music/{music_file}")
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    debug(f"Music: {music_file}")

def push_pixels(fadecandy, cups):
    """ Push our pixel array of RGB values out to the Fadecandy """
    fadecandy.put_pixels(cups)


def update_matrix(**command_string):
    """ Do some LED matrix magic """
    debug(f"MATRIX: {command_string}")
    command = command_string['command']
    value = command_string['value']
