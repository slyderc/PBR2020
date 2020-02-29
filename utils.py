import os
import sys
import time
import configparser
import argparse


def get_args():
    """ Get arguments """

    parser = argparse.ArgumentParser(
        description='PBR Arcade Beer Pong Game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-c',
                        '--config',
                        type=str,
                        default='config.ini',
                        help='Config. file to use')
    game_args = parser.parse_args()
    return game_args


def debug(msg, urgent=False):
    if config['defaults'].getboolean('verbose') and not urgent:
        print('>> %s' % str(msg))


def game_log(log_entry):
    if config['defaults'].getboolean('game_log'):
        log_time = time.asctime(time.localtime(time.time()))
        log_string = (f'{log_time}: {log_entry}{nl}')
        log_file = (f"{config['defaults']['game_path']}/game.log")

        if os.path.isfile(log_file):
            fh = open(f"{log_file}", "a")
        else:
            fh = open(f"{log_file}", "w")

        fh.write(log_string)
        fh.close()


nl = '\n'
args = get_args()
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
if not os.path.isfile(args.config):
    debug(f'Cannot open config file: {args.config}', urgent=True)
    sys.exit()
config = configparser.ConfigParser()
config.read(args.config)
