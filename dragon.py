import click
import menus.main
import utils.display


@click.command()
def cli():
    """
    Jazz Dragon is a command line utility used to communicate
    with the Medium API.
    """
    utils.display.display_logo()
    menus.main.display()
