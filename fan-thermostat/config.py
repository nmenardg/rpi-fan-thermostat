import os
from configparser import ConfigParser


config_parser = None
fan_section = None


def init():
    global config_parser, fan_section
    config_parser = ConfigParser()
    config_parser.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'local.ini'))
    fan_section = config_parser['fan']
init()
