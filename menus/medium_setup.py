import click
import sys
import utils.menus
import utils.settings
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

    :param previous_menu_callback: Function that displays prior menu.
    """
    return {
        '1': lambda: _launch_medium_applications_page(previous_menu_callback),
        '2': lambda: _edit_settings(previous_menu_callback),
        '3': previous_menu_callback,
        '4': sys.exit
    }


def _edit_settings(previous_menu_callback):
    """
    Edits settings and opens the previous menu.
    """
    utils.settings.edit()
    previous_menu_callback()


def _launch_medium_applications_page(previous_menu_callback):
    """
    Launches the medium application page and opens the previous menu.
    """
    click.launch(medium_paths.APPLICATION_PATH, wait=True)
    previous_menu_callback()
