import click
import json
import os.path
from constants import configs


def create():
    """
    Creates initial Jazz Dragon settings.
    """
    with open(get_config_path(), 'w+') as file:
        json.dump(configs.DEFAULT_SETTINGS, file, indent=2)


def edit():
    """
    Edit Jazz Dragon settings.
    """
    if not config_exists():
        create()

    return click.edit(filename=get_config_path())


def get_config_path():
    """
    Return the settings path.
    """
    path = '{0}/{1}'.format(os.path.expanduser('~'),
                            configs.SETTINGS_FILE_NAME)
    return os.path.normpath(path)


def config_exists():
    """
    Check to see if settings exist.
    """
    return os.path.isfile(get_config_path())
