#!/usr/bin/env python3

import time
import tty
import termios
import sys
import opc
import pygame
from classes import *

def main():
    player = Player()
    game = Arcade_Game(player)
    game.start()

if __name__ == '__main__':
    main()
