from click.testing import CliRunner
from dragon import cli
from mock import patch


@patch('utils.display.display_logo')
@patch('menus.main.display')
def test_cli(display_logo, display_main_menu):
    """
    cli
    """
    runner = CliRunner()
    runner.invoke(cli)

    # It should display the logo.
    display_logo.assert_called_once()

    # It should display the main menu.
    display_main_menu.assert_called_once()
