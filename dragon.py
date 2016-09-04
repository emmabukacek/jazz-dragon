import click
import pkg_resources
from utils import settings


@click.command()
def cli():
    """
    Jazz Dragon is a command line utility used to communicate
    with the Medium API.
    """
    version = pkg_resources.require('JazzDragon')[0].version

    click.echo(click.style('Dragon', fg='green'))
    click.echo(click.style('Version: {0}\n'.format(version), fg='green'))

    if not settings.settings_exist():
        return settings.prompt_create_settings()

    show_options()


def show_options():
    pass
