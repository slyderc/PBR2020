import pygame


class ArcadeGame:
    def __init__(self, player, cups, verbose=False):
        self.player = player
        self.cups = cups
        self.game_timer = 60
        self.verbose = verbose
        self._initialize()

    def _debug(self, msg):
        if self.verbose:
            print('>> %s' % str(msg))

    def _initialize(self):
        self._start_ticks = pygame.time.get_ticks()

    def start(self):
        print(self.game_timer)
        print(self.player.player_initials)
        print(self.cups.cup_light[9])
        self.cups.cup_light[9] = (255, 255, 255)
        print(self.cups.cup_light[9])
