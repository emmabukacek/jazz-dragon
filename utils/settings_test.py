from constants import configs
from mock import patch, mock_open
from utils.settings import (create,
                            edit,
                            get_config_path,
                            config_exists)


@patch('json.dump')
@patch('utils.settings.get_config_path')
def test_create(get_config_path,
                json_dump):
    """
    create

    It should create the default Jazz Dragon config object.
    """
    settings_path = 'Sailor Pants are supah cute.'
    get_config_path.return_value = settings_path

    with patch('utils.settings.open', mock_open()) as open_mock:
        create()

    open_mock.assert_called_once_with(settings_path, 'w+')
    json_dump.assert_called_once_with(configs.DEFAULT_SETTINGS,
                                      open_mock())


@patch('click.edit')
@patch('utils.settings.create')
@patch('utils.settings.get_config_path')
@patch('utils.settings.config_exists', return_value=True)
def test_edit_with_existing_settings(config_exists,
                                     get_config_path,
                                     create,
                                     click_edit):
    """
    edit and config_exists() returns True.

    It should not create setetinsg and open the existing settings
    in the default editor.
    """
    settings_path = 'Seriously. Adorbs.'
    get_config_path.return_value = settings_path

    edit()

    create.assert_not_called()
    click_edit.assert_called_once_with(settings_path)


@patch('click.edit')
@patch('utils.settings.create')
@patch('utils.settings.get_config_path')
@patch('utils.settings.config_exists', return_value=False)
def test_edit_without_existing_settings(config_exists,
                                        get_config_path,
                                        create,
                                        click_edit):
    """
    edit and config_exists() returns False.

    It should create settings and open the settings in the
    default editor.
    """
    settings_path = 'Okay. Enough about Sailor Pants.'
    get_config_path.return_value = settings_path

    edit()

    create.assert_called()
    click_edit.assert_called_once_with(settings_path)


@patch('os.path.expanduser')
@patch('os.path.normpath')
def test_get_config_path(normpath, expanduser):
    """
    test_get_config_path

    It should return the path to the settings, normalized
    per operating system.
    """
    root = 'What/about/sailor/moon?'
    expected_path = root + '/' + configs.SETTINGS_FILE_NAME
    expanduser.return_value = root

    get_config_path()

    normpath.assert_called_once_with(expected_path)


@patch('os.path.isfile', return_value=True)
def test_config_exists_with_file(is_file):
    """
    config_exists and the file exists

    It should return true.
    """
    result = config_exists()

    assert result is True


@patch('os.path.isfile', return_value=False)
def test_config_exists_without_file(is_file):
    """
    config_exists and the file doesn't exists

    It should return false.
    """
    is_file.return_value = False
    result = config_exists()

    assert result is False
