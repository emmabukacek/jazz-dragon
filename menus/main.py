import click
import menus
import utils.settings
from constants.display import medium_setup


def display():
    """
    Displays main menu for Jazz Dragon.
    """
    if not utils.settings.config_exists():
        click.echo(medium_setup.INTRO)
        return menus.display_medium_setup(display)

    pass
