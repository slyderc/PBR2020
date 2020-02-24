import random
import string
import opc
import sys
import select
import termios
import tty
from utils import config, debug
from av import push_pixels, update_matrix, play_sound


class Player:
    def __init__(self, player_initials=''.join(random.choice(string.ascii_uppercase) for x in range(3))):
        self.player_initials = player_initials
        self.game_time = 0  # total seconds played before limit or score=10
        self.score = 0  # total number of cups hit

    def __str__(self):
        """ Return the player's initials string """
        return self.player_initials


class Cups:
    def __init__(self):
        """ Connect to Fadecandy server, then turn off all cup lights and set cups "hit" status to False """
        self.address = "localhost:7890"     # Fadecandy server address & port
        self.cup_light = [(0, 0, 0)] * 10   # blackout all cup LEDs
        self.cup_hit = [False] * 10         # reset all cups "hit" status to False
        self.balls_thrown = 0
        self.key_name = ''
        self.fadecandy = opc.Client(self.address, verbose=config['defaults'].getboolean('verbose'))
        self._initialize()

    def _initialize(self):
        self._term_settings = termios.tcgetattr(sys.stdin)  # record term. settings to restore upon exit
        tty.setcbreak(sys.stdin.fileno())   # setup keyboard I/O for cup switches
        if self.fadecandy.can_connect():
            debug('connected to %s' % self.address)
        else:
            debug("ERROR: Fadecandy server not answering at %s!" % self.address)
            update_matrix("MSG,FC_7890")
            play_sound("alert.wav", True)
            return False

    def shutdown(self):
        """ Clean-up connections, terminal settings, etc. before exiting PBR script """
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self._term_settings)    # restore orig. term. settings
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
        """ If needed, update a cup's color and then push the whole pixel list to the Fadecandy """
        if self.cup_light[cup_num] != color:
            self.cup_light[cup_num] = color
            push_pixels(self.fadecandy, self.cup_light)

    def apply_cup_hits(self):
        """ Check for a switch/keyboard hit and change associated cup list item to True """
        if self.cup_is_hit():
            self.key_name = self.get_key_press()
            if self.key_name.isdigit() and not self.cup_hit[int(self.key_name)]:
                self.cup_hit[int(self.key_name)] = True
                self.light_cup(int(self.key_name), (0, 0, 255))
                play_sound(f"{config['sounds']['cup_cheers']}{self.key_name}.wav")
                self.balls_thrown += 1
                debug(f"CUP: {self.key_name} hit")
            elif self.key_name == 'Q':  # can be used during console runs to safely abort the Python script
                return True
            else:
                self.balls_thrown += 1

    def count_cups(self):
        """ Iterate cups list for True values to determine how many cups have been hit """
        total = 0

        for x in self.cup_hit:
            if x:
                total += 1
        return total
