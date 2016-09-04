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

    If I run the 'dragon' command,
    and I haven't set up my configuration yet,
    then I should be prompted to set it up.

    """
    runner = CliRunner()
    result = runner.invoke(cli)

    assert result.exit_code == 0
    assert mockPromptCreateSettings.called
    assert mockShowOptions.not_called


@patch('utils.settings.settings_exist', return_value=True)
@patch('utils.settings.prompt_create_settings')
@patch('dragon.show_options')
def test_cli_with_config(mockSettingsExist,
                         mockPromptCreateSettings,
                         mockShowOptions):
    """
    'dragon' command with API configuration

    If I run the 'dragon' command,
    and I have set up my configuration,
    then it should show all application options.
    """
    runner = CliRunner()
    result = runner.invoke(cli)

    assert result.exit_code == 0
    assert mockPromptCreateSettings.not_called
    assert mockShowOptions.called
