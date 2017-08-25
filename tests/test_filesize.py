# This test should only test filesizes when the file exists
# TODO: check setup to make sure to verify that all the files shavar should
# have delivered to the cache are actually there.

# 1. get list of files from /safebrowsing
# 2. get filesizes of ^^
# 3. add filename/size key pairs to dict
# 4. get prefs header [ex: whitelist], compare to files in dict
# 5. verify size is under maximum
import os

from helper_prefs import max_file_size_file_list
from helper_prefs import pref_sets_combined_file_lists

f = []
s = []


def test_safebrowsing_contains_expected_files(conf):
    """Hardcoded location of safebrowsing directory will need to be updated
    to reflect new FF profile file directory. Also, hardcoded profile type
    'moztestpub' needs to be updated to reflect test profile type."""
    # Get list of local files
    for name in os.listdir('safebrowsing'):
        file = os.path.splitext(name)[0]
        if file not in (f):
            f.append(file)

    expected = pref_sets_combined_file_lists(conf, 'moztestpub')
    assert set(expected).issubset(set(f))


def test_safebrowsing_filesize_under_maximum(conf):
    """Hardcoded location of safebrowsing folder, and filesize grouping
    named whitelist will need to be updated."""
    # List of expected files
    expected = max_file_size_file_list(conf, 'whitelist')

    # Collect local files that match expected list
    max_list_set = set(expected).intersection(f)

    # Get file sizes
    for file in max_list_set:
        size = os.path.getsize(os.path.join('safebrowsing', file))
        s.append(size)
        print('s loop entry', s)
