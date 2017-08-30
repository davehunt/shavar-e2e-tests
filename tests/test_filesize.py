# 1. get list of files from local /safebrowsing
# 2. get filesizes of ^^
# 4. get filesize group [ex: whitelist], compare to local matching files
# 5. verify size is under maximum
import os

from helper_prefs import (
  max_file_size_file_list,
  pref_sets_combined_file_lists,
  safebrowsing_files_unique,
  safebrowsing_files_local,
  subset_safebrowsing_prefs
)


def test_safebrowsing_contains_expected_files(conf):
    """Hardcoded location of safebrowsing directory will need to be updated
    to reflect new FF profile file directory. Also, hardcoded profile type
    'moztestpub' needs to be updated to reflect test profile type."""

    f = safebrowsing_files_unique()
    expected = pref_sets_combined_file_lists(conf, 'moztestpub')
    assert set(expected).issubset(set(f))


def test_safebrowsing_filesize_under_maximum(conf):
    """Hardcoded location of safebrowsing folder, and filesize grouping
    named whitelist will need to be updated."""
    # List of expected files
    expected = set(max_file_size_file_list(conf, 'whitelist'))
    print('----------')
    print('expected list', expected)
    print('----------')
    # Collect local files that match expected list
    found = safebrowsing_files_local()
    print('found list here', found)
    subset_safebrowsing_prefs(conf, 'whitelist')

    # # Get file sizes
    # s = []
    # for file in (f):
    #     size = os.path.getsize(os.path.join('safebrowsing', file))
    #     s.append(size)
    #     print('s loop entry', s)
    #
    # for items in (s):
    #     assert items threshold_operation size_threshold
