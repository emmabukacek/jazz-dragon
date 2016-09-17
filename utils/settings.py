import click
import json
import os.path
from constants import configs

_settings = {}


def config_exists():
    """
    Check if settings exist.
    """
    return os.path.isfile(get_config_path())


def create():
    """
    Create initial Jazz Dragon settings.
    """
    with open(get_config_path(), 'w+') as file:
        json.dump(configs.DEFAULT_SETTINGS, file, indent=2)


def edit():
    """
    Edit Jazz Dragon settings.
    """
    if not config_exists():
        create()

    click.edit(filename=get_config_path())


def get_config_path():
    """
    Return settings path.
    """
    path = '{0}/{1}'.format(os.path.expanduser('~'),
                            configs.SETTINGS_FILE_NAME)
    return os.path.normpath(path)


def load_settings():
    """
    Load current settings.
    """
    global _settings

    with open(get_config_path(), 'r+') as file:
        _settings = json.load(file)

    return _settings
