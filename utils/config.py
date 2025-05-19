import configparser

CONFIG = configparser.ConfigParser()

def init_config():
    global CONFIG
    CONFIG.read('config.ini')