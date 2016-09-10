from click.testing import CliRunner
from dragon import cli
from mock import patch


@patch('utils.settings.settings_exist', return_value=False)
@patch('utils.settings.prompt_create_settings')
@patch('dragon.show_options')
def test_cli_without_config(mockSettingsExist,
                            mockPromptCreateSettings,
                            mockShowOptions):
    """
    'dragon' command without API configuration

    It should prompt the user to set up their
    configuration.
    """
    runner = CliRunner()
    result = runner.invoke(cli)

    assert result.exit_code == 0
    assert mockShowOptions.not_called
    mockPromptCreateSettings.assert_called_with(cli, True)


@patch('utils.settings.settings_exist', return_value=True)
@patch('utils.settings.prompt_create_settings')
@patch('dragon.show_options')
def test_cli_with_config(mockSettingsExist,
                         mockPromptCreateSettings,
                         mockShowOptions):
    """
    'dragon' command with API configuration

    It should show the user available application
    options.
    """
    runner = CliRunner()
    result = runner.invoke(cli)

    assert result.exit_code == 0
    assert mockPromptCreateSettings.not_called
    assert mockShowOptions.called
