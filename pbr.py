#!/usr/bin/env python3
"""
 ______   ______   ______
| |  | \ | |  | \ | |  | \
| |__|_/ | |--| < | |__| |
|_|      |_|__|_/ |_|   \_\
   ong,         eer,      ad
"""

from classes import Player, Cups
from games import *
from av import init_sound


def main():
    pygame.init()
    init_sound()
    player = Player()
    cups = Cups()
    game = ArcadeGame(player, cups)
    # TODO: Player can select different game modes which will ea. have their own class
    print(game)
    cups.shutdown()     # close Fadecandy connection, reset term. settings and clean-up


if __name__ == '__main__':
    exit(main())
