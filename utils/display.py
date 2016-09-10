import click
import pkg_resources
from constants.display import ascii_art


def display_logo():
    """
    Display the Jazz Dragon logo.
    """
    version = pkg_resources.require('JazzDragon')[0].version

    click.secho(ascii_art.JAZZ_DRAGON_LOGO, fg='red', bold=True)
    click.secho('Version: {0}\n'.format(version), fg='yellow', bold=True)
