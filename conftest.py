import os
import ConfigParser
import pytest

from foxpuppet import FoxPuppet
from helper_prefs import set_prefs


PREF_SET = os.environ['PREF_SET']


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
def firefox_options(firefox_options):
    c = conf()
    # firefox_options.set_preference('browser.startup.homepage', "google.com")
    # 1. Set default conf values (loop through them)
    # 2. Set test env (stage or prod)
    # This will come from an environment variable
    # 3. Set "pref_set" values, this will come from an env. variable
    return firefox_options


@pytest.fixture
def foxpuppet(selenium):
    return FoxPuppet(selenium)
