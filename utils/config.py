# DONT FUCKIN TOUCH OR IT WILL BREAK!!!!
import os
import json

CONFIG_FILE = 'config.json'
DEFAULT_CONFIG = {'prefix': '.', 'help_emoji': '▫️', 'trlang': 'en', 'mainemoji': '🌧'}

if not os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(DEFAULT_CONFIG, f, indent=4)

def add_to_config(key, value):
    """
    Adds or updates a key-value pair in the config file.

    :param key: The key to add or update in the config
    :param value: The value to assign to the key
    """
    with open(CONFIG_FILE, 'r') as f:
        config = json.load(f)

    config[key] = value

    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

def read_from_config(key):
    """
    Reads a value from the config file.

    :param key: The key to read from the config
    :return: The value associated with the key, or None if the key doesn't exist
    """
    with open(CONFIG_FILE, 'r') as f:
        config = json.load(f)

    return config.get(key, None)

def read_all_keys():
    """
    Reads all keys and their corresponding values from the config file.

    :return: A dictionary containing all key-value pairs from the config
    """
    with open(CONFIG_FILE, 'r') as f:
        config = json.load(f)

    return config


def remove_from_config(key):
    """
    Removes a key from the config file.

    :param key: The key to remove from the config
    :return: True if the key was removed, False if the key didn't exist
    """
    with open(CONFIG_FILE, 'r') as f:
        config = json.load(f)

    if key in config:
        del config[key]
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=4)
        return True
    else:
        return False
