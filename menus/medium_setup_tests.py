from constants import menu_options
from menus.medium_setup import (display,
                                get_option_callbacks_map,
                                _edit_settings,
                                _launch_medium_applications_page)
from mock import Mock, patch


@patch('menus.medium_setup.get_option_callbacks_map')
@patch('utils.menus.generate_menu')
def test_display(generate_menu, get_options):
    """
    display
    """
    options_map = 'Who cares'
    previous_menu_callback = 'No one.'
    get_options.return_value = options_map

    display(previous_menu_callback)

    # It should get callbacks from the get_option_callbacks_map function.
    get_options.assert_called_once_with(previous_menu_callback)

    # It should generate a menu.
    generate_menu.assert_called_once_with(menu_options.SETUP_MEDIUM,
                                          options_map,
                                          display)


def test_get_option_callbacks_map():
    """
    get_option_callbacks_map
    """
    result = get_option_callbacks_map(Mock())

    # It should return an options map.
    for key, value in result.items():
        assert callable(value)


@patch('utils.settings.edit')
def test_edit_settings(edit):
    """
    _edit_settings
    """
    prev_menu = Mock()

    _edit_settings(prev_menu)

    # It should call the edit method on settings.
    edit.assert_called_once()

    # It should open the previous menu.
    prev_menu.assert_called_once()


@patch('click.launch')
def test_launch_medium_applications_page(launch):
    """
    _launch_medium_applications_page
    """
    prev_menu = Mock()

    _launch_medium_applications_page(prev_menu)

    # It should call the edit method on settings.
    launch.assert_called_once()

    # It should open the previous menu.
    prev_menu.assert_called_once()
