import click
import utils.menus
import sys
from constants import medium_paths, menu_options


def display(previous_menu_callback):
    """
    Prompt user to initialize Medium settings.

    :param previous_menu_callback: Function that displays prior menu.
    """

    option_map = get_option_callbacks_map(previous_menu_callback)

    utils.menus.generate_menu(menu_options.SETUP_MEDIUM, option_map, display)


def get_option_callbacks_map(previous_menu_callback):
    """
    Gets medium setup option callbacks.
    """
    return {
        '1': lambda: click.launch(medium_paths.APPLICATION_PATH, wait=True),
        '2': lambda: utils.settings.edit_settings(use_defaults=True),
        '3': previous_menu_callback,
        '4': sys.exit
    }
