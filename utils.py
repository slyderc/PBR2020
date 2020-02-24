import os
import sys
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

    args = parser.parse_args()

    return args


def debug(msg, urgent=False):
    if config['defaults'].getboolean('verbose') and not urgent:
        print('>> %s' % str(msg))


args = get_args()
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
if not os.path.isfile(args.config):
    debug(f'Cannot open config file: {args.config}', urgent=True)
    sys.exit()
config = configparser.ConfigParser()
config.read(args.config)
