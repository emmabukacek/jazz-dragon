from constants.display import medium_setup
from menus.main import display
from mock import patch


@patch('click.echo')
@patch('menus.medium_setup.display')
@patch('utils.settings.config_exists', return_value=True)
def test_display_with_existing_config(config_exists,
                                      display_medium_menu,
                                      click_echo):
    display()

    # It should not display the medium setup intro.
    click_echo.assert_not_called()

    # It should not show the medium setup menu.
    display_medium_menu.assert_not_called()


@patch('click.echo')
@patch('menus.medium_setup.display')
@patch('utils.settings.config_exists', return_value=False)
def test_display_without_existing_config(config_exists,
                                         display_medium_menu,
                                         click_echo):
    display()

    # It should display the medium setup intro.
    click_echo.assert_called_once_with(medium_setup.INTRO)

    # It should not show the medium setup menu.
    display_medium_menu.assert_called_once_with(display)
