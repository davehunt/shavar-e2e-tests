import ConfigParser
import pytest

from foxpuppet import FoxPuppet


@pytest.fixture
def browser(foxpuppet):
    """Initial Firefox browser window."""
    return foxpuppet.browser


@pytest.fixture()
def conf():
    config = ConfigParser.ConfigParser()
    config.read('prefs.ini')
    return config


@pytest.fixture
def foxpuppet(selenium):
    return FoxPuppet(selenium)
