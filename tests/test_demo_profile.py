"""Test to download a version of Firefox Nightly and then
be able to edit the profile preferences to match Tracking
Protection lists.
1. download - either Nightly and release
[2. install Linux only] - skip for today
3. set installdir in PATH for Selenium
4. run Selenium
"""
import pytest
import time
from selenium import webdriver
from helper_prefs import set_prefs


@pytest.mark.nondestructive
def test_moztestpub(conf, driver):
    fp = set_prefs(conf, ['stage', 'moztestpub'])

    driver = webdriver.Firefox(firefox_profile=fp)
    driver.maximize_window()
    driver.get("about:config")
    time.sleep(2)

@pytest.mark.nondestructive
def test_mozstd(conf, driver):
    fp = set_prefs(conf, ['stage', 'mozstd'])

    driver = webdriver.Firefox(firefox_profile=fp)
    driver.maximize_window()
    driver.get("about:config")
    time.sleep(2)
