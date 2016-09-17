from constants import configs
from mock import patch, mock_open
import utils.settings


@patch('json.dump')
@patch('utils.settings.get_config_path')
def test_create(get_config_path,
                json_dump):
    config_path = 'Sailor Pants are supah cute.'
    get_config_path.return_value = config_path

    with patch('utils.settings.open', mock_open()) as open_mock:
        utils.settings.create()

    # It should open the file and create it if it doesn't exist.
    open_mock.assert_called_once_with(config_path, 'w+')

    # It should dump default json inside.
    json_dump.assert_called_once_with(configs.DEFAULT_SETTINGS,
                                      open_mock(),
                                      indent=2)


@patch('click.edit')
@patch('utils.settings.create')
@patch('utils.settings.get_config_path')
@patch('utils.settings.config_exists', return_value=True)
def test_edit_with_existing_config(config_exists,
                                   get_config_path,
                                   create,
                                   click_edit):
    config_path = 'Seriously. Adorbs.'
    get_config_path.return_value = config_path

    utils.settings.edit()

    # It should not create settings.
    create.assert_not_called()

    # It should open the editor with the config_path
    click_edit.assert_called_once_with(filename=config_path)


@patch('click.edit')
@patch('utils.settings.create')
@patch('utils.settings.get_config_path')
@patch('utils.settings.config_exists', return_value=False)
def test_edit_without_existing_config(config_exists,
                                      get_config_path,
                                      create,
                                      click_edit):
    config_path = 'Okay. Enough about Sailor Pants.'
    get_config_path.return_value = config_path

    utils.settings.edit()

    # It should create new settings.
    create.assert_called()

    # It should open those settings in the editor.
    click_edit.assert_called_once_with(filename=config_path)


@patch('os.path.expanduser')
@patch('os.path.normpath')
def test_get_config_path(normpath, expanduser):
    root = 'What/about/sailor/moon?'
    expected_path = root + '/' + configs.SETTINGS_FILE_NAME
    expanduser.return_value = root

    utils.settings.get_config_path()

    # It should resolve the path based on the user's operating system.
    normpath.assert_called_once_with(expected_path)


@patch('os.path.isfile', return_value=True)
def test_config_exists_with_existing_file(is_file):
    result = utils.settings.config_exists()

    # It should return true.
    assert result is True


@patch('os.path.isfile', return_value=False)
def test_config_exists_without_existing_file(is_file):
    is_file.return_value = False
    result = utils.settings.config_exists()

    # It should return false.
    assert result is False


@patch('json.load')
@patch('utils.settings.get_config_path')
def test_load_settings(get_config_path,
                       json_load):
    config_path = 'Actually haven\'t watched that show...'
    new_settings = 'Oh well. New Settings Yo!'

    get_config_path.return_value = config_path
    json_load.return_value = new_settings

    print(utils.settings._settings)

    with patch('utils.settings.open', mock_open()) as open_mock:
        return_value = utils.settings.load_settings()

    # It should open the file.
    open_mock.assert_called_once_with(config_path, 'r+')

    # It should load the file.
    json_load.assert_called_once_with(open_mock())

    # It should set the settings.
    assert utils.settings._settings is new_settings

    # It should return loaded settings
    assert return_value is new_settings
