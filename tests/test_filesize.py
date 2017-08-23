# This test should only test filesizes when the file exists
# TODO: check setup to make sure to verify that all the files shavar should
# have delivered to the cache are actually there.

# 1. get list of files from /safebrowsing
# 2. get filesizes of ^^
# 3. add filename/size key pairs to dict
# 4. get prefs header [ex: whitelist], compare to files in dict
# 5. verify size is under maximum
import os

from helper_prefs import get_profile_expected_files

f = []
s = []


def test_safebrowsing_contains_files(conf):
    """Hardcoded location of safebrowsing directory will need to be updated
    to reflect new FF profile file directory"""
    # Get list of local files
    for name in os.listdir('safebrowsing'):
        file = os.path.splitext(name)[0]
        if file not in (f):
            f.append(file)

    expected = get_profile_expected_files(conf, ('moztestpub'))
    assert set(expected).issubset(set(f))


def test_filesize(conf):
    # collect local file sizes
    for file in os.listdir('safebrowsing'):
        # print(f)
        if file in (f):
            size = os.path.getsize(os.path.join('safebrowsing', file))
            s.append(size)
    # print (s)
    wh_size = conf.get("whitelist", "size_threshold")
    for item in s:
        assert item < wh_size
