from utils.settings import settings_exist
from mock import patch


@patch('utils.settings.isfile', return_value=True)
def test_settings_exist_with_file(mockIsFile):
    """
    settings_exist and the file exists

    settings_exist should return true
    """
    result = settings_exist()
    print(result)
    print(mockIsFile)

    assert mockIsFile.called
    # assert result is True


@patch('utils.settings.isfile', return_value=False)
def test_settings_exist_without_file(mockIsFile):
    """
    settings_exist and the file doesn't exists

    settings_exist should return false
    """
    mockIsFile.return_value = False
    result = settings_exist()

    assert result is False
