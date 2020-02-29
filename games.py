import pygame
from av import play_sound, play_music, update_matrix
from utils import config, debug, game_log

GAME_OVER = {"LOST":0, "WON":1, "TIE":2, "TIMEOUT":3, "QUIT":4}
GAME_MODE = {"PRACTICE":0, "TIMED":1}


def time_check(game_length, elapsed_seconds, last_time_value):
    """ Clock handler routine """

    seconds_left = int(game_length - elapsed_seconds)
    if seconds_left:

        """ Has one sec. of time elapsed?  If so, update display & run checks """
        if seconds_left != last_time_value:
            if seconds_left == 10:
                debug("*** HURRY UP ***")
                play_music(config['music']['hurry_up'])

            if seconds_left < 6:
                if seconds_left != 0:
                    play_sound(config['sounds']['countdown'] + str(seconds_left) + ".wav")
                else:
                    play_sound(config['sounds']['times_up'])

            update_matrix(command="TIME", value=seconds_left)
            debug(f"** {str(seconds_left)} **")

    return seconds_left


class ArcadeGame:
    """ ArcadeGame mode: 1 player; 60 sec. to hit all 10 cups """
    def __init__(self, player, cups):
        self.player = player
        self.cups = cups
        self.game_length = 14   # TODO: change this to 60 when debugging is done
        self.time_left = self.game_length
        self.game_name = "Arcade"
        self._last_time_check = 0
        game_log(f"{player.player_initials} starting new {self.game_name} game of {self.game_length} seconds")
        self._game_loop()

    def __str__(self):
        """ Return the player's initials string """
        return self.game_name

    @staticmethod
    def _game_over():
        pygame.mixer.music.fadeout(1500)
        pygame.quit()

    def _game_loop(self):
        self._start_ticks = pygame.time.get_ticks()

        while True:
            self.elapsed_seconds = (pygame.time.get_ticks() - self._start_ticks) / 1000
            self._last_time_check = time_check(self.game_length, self.elapsed_seconds, self._last_time_check)

            """ TIME'S UP - GAME OVER """
            if self._last_time_check == 0:
                debug("OUT OF TIME")
                play_sound(config['sounds']['you_lose'])
                self._game_over()
                break

            """ Check for & record cup switch hits, or if (Q) pressed, which returns a True """
            if self.cups.apply_cup_hits():
                debug("QUIT")
                self._game_over()
                break

            """ See if all 10 cups have been hit == WINNER """
            if self.cups.count_cups() == 10:
                debug("WINNER")
                play_music(config['music']['you_win'])
                play_sound(config['sounds']['win_cheering'])
                pygame.mixer.music.fadeout(8000)
                self._game_over()
                break

        log_entry = (f"{self.player.player_initials} threw {self.cups.balls_thrown} balls and hit {self.cups.count_cups()} cups in {int(self.elapsed_seconds)} seconds")
        debug(log_entry)
        game_log(log_entry)

    def top10(self):
        pass


class TicTacToeGame:
    """ TicTacToe mode: 2 players; ea. taking turns to win a 3-in-a-row line """
    def __init__(self, player_1, cups, player_2=None, game_mode=GAME_MODE['TIMED']):
        self.player_1 = player_1
        self.player_2 = player_2
        self.cups = cups
        self.game_name = "TicTacToe"
        self.game_mode = game_mode
        game_log(f"{player_1.player_initials} and {player_2.player_initials} starting new {self.game_name} game")
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
    def __init__(self, player_1, cups, player_2=None, game_mode=GAME_MODE['TIMED']):
        self.player_1 = player_1
        self.player_2 = player_2
        self.cups = cups
        self.game_name = "TargetPractice"
        self.game_mode = game_mode
        self._game_loop()

    def __str__(self):
        """ Return the game's name string """
        return self.game_name

    def _game_loop(self):
        pass

    def top10(self):
        pass
