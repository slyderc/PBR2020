import pygame
from av import play_sound, play_music, update_matrix
from utils import debug

GAME_OVER = {"LOST":0, "WON":1, "TIE":2, "TIMEOUT":3, "QUIT":4}
GAME_MODE = {"PRACTICE":0, "TIMED":1}


def time_check(game_length, elapsed_seconds, last_time_value):

    seconds_left = int(game_length - elapsed_seconds)

    if seconds_left:

        """ Has one sec. of time elapsed?  If so, update display & run checks """
        if seconds_left != last_time_value:
            if seconds_left == 10:
                debug("*** HURRY UP ***")
                play_music("BK2K_hurry.mp3")

            if seconds_left < 6:
                if seconds_left != 0:
                    play_sound("countdown_" + str(seconds_left) + ".wav")
                else:
                    play_sound("airhorn.wav")

            update_matrix("TIME,"+str(seconds_left))
            debug("** {} **".format(str(seconds_left)))

    return seconds_left


class ArcadeGame:
    """ ArcadeGame mode: 1 player; 60 sec. to hit all 10 cups """
    def __init__(self, player, cups, verbose=False):
        self.player = player
        self.cups = cups
        self.game_length = 60
        self.time_left = self.game_length
        self.game_name = "Arcade"
        self.game_over = GAME_OVER['LOST']
        self.balls_thrown = 0
        self.verbose = verbose
        self._last_time_check = 0
        self._game_loop()

    def __str__(self):
        """ Return the player's initials string """
        return self.game_name

    def _game_loop(self):
        self._start_ticks = pygame.time.get_ticks()

        while True:
            self.elapsed_seconds = (pygame.time.get_ticks() - self._start_ticks) / 1000
            self._last_time_check = time_check(self.game_length, self.elapsed_seconds, self._last_time_check)

            """ TIME'S UP - GAME OVER """
            if self._last_time_check == 0:
                pygame.mixer.music.fadeout(1500)
                break

        print(self.player.player_initials)
        print(self.cups.cup_light[9])
        self.cups.cup_light[9] = (255, 255, 255)
        self.cups.push_pixels()
        print(self.cups.cup_light[9])

    def top10(self):
        pass


class TicTacToeGame:
    """ TicTacToe mode: 2 players; ea. taking turns to win a 3-in-a-row line """
    def __init__(self, player_1, cups, player_2=None, game_mode=GAME_MODE['TIMED'], verbose=False):
        self.player_1 = player_1
        self.player_2 = player_2
        self.cups = cups
        self.game_name = "TicTacToe"
        self.game_mode = game_mode
        self.verbose = verbose
        self._game_loop()

    def __str__(self):
        """ Return the game's name string """
        return self.game_name

    def _game_loop(self):
        pass

    def top10(self):
        pass


class TargetPracticeGame:
    """ TargetPractice mode: sequential cup hits and random, computer-given cup hits """
    def __init__(self, player_1, cups, player_2=None, game_mode=GAME_MODE['TIMED'], verbose=False):
        self.player_1 = player_1
        self.player_2 = player_2
        self.cups = cups
        self.game_name = "TargetPractice"
        self.game_mode = game_mode
        self.verbose = verbose
        self._game_loop()

    def __str__(self):
        """ Return the game's name string """
        return self.game_name

    def _game_loop(self):
        pass

    def top10(self):
        pass
