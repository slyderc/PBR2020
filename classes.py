import random
import string
import pygame
import opc
import sys
import select
import termios
import tty
from utils import debug
from av import push_pixels


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
        """ Connect to Fadecandy server, then turn off all cup lights and set cups "hit" status to False """
        self.verbose = verbose
        self.address = "localhost: 7890"
        self.cup_light = [(0, 0, 0)] * 10
        self.cup_hit = [False] * 10
        self.key_name = ''
        self.fadecandy = opc.Client(self.address, verbose=self.verbose)
        self._initialize()

    def _initialize(self):
        tty.setcbreak(sys.stdin.fileno())   # setup keyboard I/O for cup switches
        if self.fadecandy.can_connect():
            debug('connected to %s' % self.address)
        else:
            debug("ERROR: Fadecandy server not answering at %s!" % self.address)
            # TODO: some sort of external message/light/sound to indicate problem, ie::
            # update_matrix("MSG,FC_7890")
            # play_sound("alert.wav", True)
            return False

    def shutdown(self):
        self.fadecandy.disconnect()

    def push_pixels(self):
        """ Push our pixels out to the Fadecandy """
        self.fadecandy.put_pixels(self.cup_light)

    @staticmethod
    def cup_is_hit():
        """ Check to see if there's keyboard input waiting and return it if so """
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

    @staticmethod
    def get_key_press():
        """ Read then convert the keypress to a string character and return """
        return str(sys.stdin.read(1)).upper()

    def light_cup(self, cup_num, color):
        """ Update a cup's color and then push the whole pixel list to the Fadecandy """
        if color is None:
            color = (0, 0, 0)
        self.cup_light[cup_num] = color
        push_pixels(self.fadecandy, self.cup_light)

    def apply_cup_hits(self):
        if self.cup_is_hit():
            self.key_name = self.get_key_press()
            if self.key_name.isdigit():
                self.cup_hit[int(self.key_name)] = True
                self.light_cup(int(self.key_name), (0, 0, 255))
                debug(f"CUP: {self.key_name} hit")
            elif self.key_name == 'Q':
                return True

    def count_cups(self):
        """ Count how many cups have balls """
        total = 0

        for x in self.cup_hit:
            if x:
                total += 1
        return total
