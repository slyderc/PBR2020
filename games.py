class ArcadeGame:
    global fadecandy

    def __init__(self, player, cups, debug=False):
        self.player = player
        self.cups = cups
        self.game_timer = 60
        self.debug = debug

    def start(self):
        print(self.game_timer)
        print(self.player.player_initials)
        print(self.cups[9].color)
