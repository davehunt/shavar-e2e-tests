import ConfigParser
import pytest

from foxpuppet import FoxPuppet
# from helper_prefs import set_prefs
from selenium import webdriver

@pytest.fixture
def browser(foxpuppet):
    """Initial Firefox browser window."""
    return foxpuppet.browser


@pytest.fixture()
def conf():
    config = ConfigParser.ConfigParser()
    config.read('prefs.ini')
    return config


# @pytest.fixture
# def driver(selenium):
#     driver = webdriver.Firefox(firefox_profile=fp)
#     driver.maximize_window()


@pytest.fixture
def foxpuppet(selenium):
    return FoxPuppet(selenium)
