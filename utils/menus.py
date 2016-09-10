import click
from collections import OrderedDict
from constants.display import menus


def display_invalid_choice(display_options_callback):
    """
    Inform user of invalid option choice and re-prompt user.

    :param display_options_callback: Callback that runs at the end.
    """
    click.echo(menus.INVALID_OPTION)
    display_options_callback()


def get_display_text_from_options(options):
    """
    Format provided options as a string of options for the user.

    :param option: Dictionary of options.
    """
    ordered_options = OrderedDict(sorted(options.items(), key=lambda t: t[0]))
    return reduce(
        lambda displayText, key:
            '{0}[{1}] - {2}\n'.format(displayText,
                                      key,
                                      ordered_options[key]),
        ordered_options,
        ''
    )


def generate_menu(options, options_map, invalid_choice_callback):
    """
    Generates an interactive menu that runs methods based on user
    interaction.

    :param options: Dictionary of options, with keys representing user
        input and values representing display text for each input.
    :pardisplayam options_map: Dictionary of callbacks, corresponding
        to options param keys.
    :param invalid_choice_callback: Function called when an
        invalid choice is selected.
    """
    options_text = get_display_text_from_options(options)

    click.secho(options_text, fg='blue')
    selected_option = click.prompt(menus.SELECT_OPTION)

    def default_option():
        display_invalid_choice(invalid_choice_callback)

    options_map.get(selected_option, default_option)()
