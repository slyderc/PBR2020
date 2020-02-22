#!/usr/bin/env python3

import random
import string


class Player:
    def __init__(self, player_initials=''.join(random.choice(string.ascii_uppercase) for x in range(3))):
        self.player_initials = player_initials
        self.game_time = 0  # total seconds played before limit or score=10
        self.score = 0  # total number of cups hit


class Cup:
    global fadecandy

    def __init__(self, color=None):
        if color is None:
            color = [(255, 255, 255)]
        self.color = color
        self.hit = False

    def cup_light(self, color, on=True):
        pass

    def is_hit(self):
        pass
