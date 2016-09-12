from constants.display import menus
from mock import Mock, patch
from utils.menus import (display_invalid_choice,
                         get_display_text_from_options,
                         generate_menu)


@patch('click.echo')
def test_display_invalid_choice(click_echo):
    """
    display_invalid_choice
    """

    callback = Mock()
    display_invalid_choice(callback)

    # It should inform the user of an invalid choice.
    click_echo.assert_called_once_with(menus.INVALID_OPTION)

    # It should run the provided callback.
    callback.assert_called_once()


def test_get_display_text_from_options():
    """
    get_display_text_from_options
    """

    options = {
        'w': 'Wipe',
        'f': 'Flush',
        1: 'Lift seat'
    }

    result = get_display_text_from_options(options)

    # It should return display text generated from the provided map,
    # ordered by keys.
    assert result == '[1] - Lift seat\n[f] - Flush\n[w] - Wipe\n'


@patch('click.prompt')
@patch('click.secho')
@patch('utils.menus.display_invalid_choice')
@patch('utils.menus.get_display_text_from_options')
def test_generate_menu_with_invalid_input(get_display_text_from_options,
                                          display_invalid_choice,
                                          click_secho,
                                          click_prompt):
    options = 'Tearing up the bathroom is a party foul.'
    invalid_choice_callback = 'Seriously'
    option_one_method = Mock()

    option_map = {1: option_one_method}

    click_prompt.return_value = 'Not taking it seriously'
    get_display_text_from_options.side_effect = lambda x: x

    generate_menu(options, option_map, invalid_choice_callback)

    # It should display options provided from the options param.
    click_secho.assert_called_once_with(options, fg='blue')

    # It should prompt the user for the selected option.
    click_prompt.assert_called_once_with(menus.SELECT_OPTION)

    # It should not display an invalid choice warning.
    display_invalid_choice.assert_called_once_with(invalid_choice_callback)


@patch('click.prompt')
@patch('click.secho')
@patch('utils.menus.display_invalid_choice')
@patch('utils.menus.get_display_text_from_options')
def test_generate_menu_with_valid_input(get_display_text_from_options,
                                        display_invalid_choice,
                                        click_secho,
                                        click_prompt):
    options = 'Tearing up the bathroom is a party foul.'
    invalid_choice_callback = 'Seriously'
    option_one_method = Mock()

    option_map = {1: option_one_method}

    click_prompt.return_value = 1
    get_display_text_from_options.side_effect = lambda x: x

    generate_menu(options, option_map, invalid_choice_callback)

    # It should display options provided from the options param.
    click_secho.assert_called_once_with(options, fg='blue')

    # It should prompt the user for the selected option.
    click_prompt.assert_called_once_with(menus.SELECT_OPTION)

    # It should not display an invalid choice warning.
    display_invalid_choice.assert_not_called

    # It should run the method corresponding to the user input.
    option_one_method.assert_called_once
