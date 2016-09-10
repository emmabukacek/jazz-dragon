from constants import menu_options
from menus.medium_setup import display, get_option_callbacks_map
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
