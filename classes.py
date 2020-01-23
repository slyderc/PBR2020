#!/usr/bin/env python3

import string
import random

class Player:
    def __init__(self, player_initials=''.join(random.choice(string.ascii_uppercase) for x in range(3))):
        self.player_initials = player_initials
        self.game_time = 0	# total seconds played before limit or score=10
        self.score = 0		# total number of cups hit

class Cup:
    def __init__(self, color=[(255, 255, 255)]):
        self.color = color
        self.hit = False

class Arcade_Game:
    def __init__(self, player, debug=False):
        self.cups = [Cup(count) for count in range(10)]
        self.game_timer = 60
        self.player = player
        self.debug = debug

    def start(self):
        print(self.game_timer)
        print(self.player.player_initials)
        print(self.cups[0].hit)

def main():
    player = Player()
    game = Arcade_Game(player)
    game.start()

if __name__ == '__main__':
    main()
