# 1. get list of files from local /safebrowsing
# 2. get filesizes of ^^
# 4. get filesize group [ex: whitelist], compare to local matching files
# 5. verify size is under maximum
import os

import json

from helper_prefs import (
  filesize_index,
  max_file_size_file_list,
  pref_sets_combined_file_lists,
  safebrowsing_files_unique,
  safebrowsing_files_local,
  safebrowsing_files_local_expected,
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
    sections_filesizes = filesize_index(conf)
    for section in sections_filesizes:
        print('----------------')
        print(section)
        print('----------------')
        size_threshold = conf.get(section, 'size_threshold')
        threshold_operation = conf.get(section, 'threshold_operation')
        found_expected = safebrowsing_files_local_expected(conf, section)

        for f in found_expected:
            conditional = '{0} {1} {2}'.format(f[1], threshold_operation, size_threshold)
            print(f)
            assert eval(conditional), 'Filesize unexpected'
