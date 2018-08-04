# settings.py
import pathlib
import json

BASE_DIR = pathlib.Path(__file__)
config_path = BASE_DIR / 'config' / 'conf.json'

def get_config(path):
    with open(path) as f:
        config = json.load(f)
    return config

config = get_config(config_path)