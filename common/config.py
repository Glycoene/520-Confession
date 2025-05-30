import configparser
from pathlib import Path

CONFIG = configparser.ConfigParser()

def init_config():
    config_path = Path(__file__).parent.parent / 'config.ini'
    CONFIG.read(f'{config_path}', encoding='utf-8')