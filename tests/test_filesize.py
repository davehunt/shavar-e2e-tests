# This test should only test filesizes when the file exists
# TODO: check setup to make sure to verify that all the files shavar should
# have delivered to the cache are actually there.

# 1. get list of files from /safebrowsing
# 2. get filesizes of ^^
# 3. add filename/size key pairs to dict
# 4. get prefs header [ex: whitelist], compare to files in dict
# 5. verify size is under maximum

import ConfigParser
import os

conf = ConfigParser.ConfigParser()
conf.read('prefs.ini')
dir = ('safebrowsing')
sections = ['flashblock', 'whitelist', 'blacklist', 'content', 'DNT', 'plugin']

p = []
f = []
s = []


def prefs_group(conf, section):
    # Go through each of the non-default prefs sections and list the files
    prefs = conf.get(section, 'file_list')
    p.extend(prefs.split(','))
    return p

    for section in sections:
        prefs_group(section)


def test_safebrowsing(conf):
    """Hardcoded location of safebrowsing directory will need to be updated
    to reflect new FF profile file directory"""
    # Get list of files
    for name in os.listdir('safebrowsing'):
        file = os.path.splitext(name)[0]
        if file not in (f):
            f.append(file)

    # compare local files with expected file_list
    flashblock = conf.get("flashblock", "file_list")
    assert flashblock == (f)


def test_filesize(conf):
    # collect local file sizes
    for file in os.listdir('safebrowsing'):
        size = os.path.getsize
        s.append(size)

    wh_size = conf.getint("whitelist", "size_threshold")
    wh_th = conf.getint("whitelist", "threshold_operation")
    wh_max = eval(conf.getint("whitelist", "max"))
    assert 900000000, wh_max
