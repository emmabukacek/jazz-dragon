import click
import pkg_resources
from utils import settings
from constants import display


@click.command()
def cli():
    """
    Jazz Dragon is a command line utility used to communicate
    with the Medium API.
    """
    version = pkg_resources.require('JazzDragon')[0].version

    click.echo(click.style(display.JAZZ_DRAGON_LOGO, fg='red'))
    click.echo(click.style('Version: {0}\n'.format(version), fg='green'))

    if not settings.settings_exist():
        return settings.prompt_create_settings(cli, True)

    show_options()


def show_options():
    pass
