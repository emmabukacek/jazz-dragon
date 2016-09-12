from constants.display import ascii_art
from mock import call, patch
from utils.display import display_logo


@patch('click.secho')
@patch('pkg_resources.require')
def test_display_logo(require, click_secho):
    class Package(object):
        version = 'Derp'

    mock_package = Package()
    versionDisplay = 'Version: ' + mock_package.version + '\n'
    require.return_value = [mock_package]

    display_logo()

    click_secho.assert_has_calls([
        # It should display the logo.
        call(ascii_art.JAZZ_DRAGON_LOGO, fg='red', bold=True),
        # It should display the version.
        call(versionDisplay, fg='yellow', bold=True)
    ])
