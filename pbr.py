#!/usr/bin/env python3
"""
 ______   ______   ______
| |  | \ | |  | \ | |  | \
| |__|_/ | |--| < | |__| |
|_|      |_|__|_/ |_|   \_\
   ong,         eer,      ad
"""

from classes import *
from games import *
from av import init_sound


def main():
    pygame.init()
    init_sound()
    player = Player()
    cups = Cups(verbose=True)
    game = ArcadeGame(player, cups)
    # TODO: Player can select different game modes which will ea. have their own class

    print(player)
    print(game)
    cups.shutdown()


if __name__ == '__main__':
    main()
