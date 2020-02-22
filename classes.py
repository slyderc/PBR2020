#!/usr/bin/env python3

"""
 ______   ______   ______
| |  | \ | |  | \ | |  | \
| |__|_/ | |--| < | |__| |
|_|      |_|__|_/ |_|   \_\
   ong,         eer,      ad
"""

import random
import string
import opc


class Player:
    def __init__(self, player_initials=''.join(random.choice(string.ascii_uppercase) for x in range(3))):
        self.player_initials = player_initials
        self.game_time = 0  # total seconds played before limit or score=10
        self.score = 0  # total number of cups hit

    def __str__(self):
        """ Return the player's initials string """
        return self.player_initials


class Cups:
    def __init__(self, verbose=False):
        """ Connect to Fadecandy server, then turn off all cup lights and set "hit" status to False """
        self.verbose = verbose
        self.address = "localhost: 7890"
        self.cup_light = [(0, 0, 0)] * 10
        self.cup_hit = [False] * 10
        self.fadecandy = opc.Client(self.address, verbose=self.verbose)
        self._initialize()

    def _debug(self, msg):
        if self.verbose:
            print('>> %s' % str(msg))

    def _initialize(self):
        if self.fadecandy.can_connect():
            self._debug('connected to %s' % self.address)
        else:
            self._debug("ERROR: Fadecandy server not answering at %s!" % self.address)
            # TODO: some sort of external message/light/sound to indicate problem, ie::
            # update_matrix("MSG,FC_7890")
            # play_sound("alert.wav", True)
            return False

    def shutdown(self):
        self.fadecandy.disconnect()

    def turn_on(self, cup_num, color):
        if color is None:
            color = (0, 0, 0)
        self.cup_light[cup_num] = color
        self.fadecandy.put_pixels(self.cup_light)

    def check_hits(self):
        pass
    