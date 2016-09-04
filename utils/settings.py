from os.path import expanduser, isfile
SETTINGS_FILE_NAME = '.jazz_dragon_settings'


def settings_exist():
    """
    Check to see if settings exist.
    """
    home = expanduser('~')
    return isfile(home + SETTINGS_FILE_NAME)


def prompt_create_settings():
    """
    Prompt user to create settings.
    """
    pass
