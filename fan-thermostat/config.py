import os
from configparser import ConfigParser

from variables import ROOT_DIR


config_parser = None
fan_section = None


def init():
    global config_parser, fan_section
    config_parser = ConfigParser()
    config_parser.read(os.path.join(ROOT_DIR, 'local.ini'))
    fan_section = config_parser['fan']
init()
