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
  safebrowsing_files_local_NEW,
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
    filenames_expected = subset_safebrowsing_prefs(conf, 'whitelist')
    import json
    fe = json.dumps(filenames_expected, indent=4)
    print(fe)

    # # Get file sizes
    # s = []
    # for file in (f):
    #     size = os.path.getsize(os.path.join('safebrowsing', file))
    #     s.append(size)
    #     print('s loop entry', s)
    #
    # for items in (s):
    #     assert items threshold_operation size_threshold

    section = 'DNT'
    size_threshold = conf.get(section, 'size_threshold')
    threshold_operation = conf.get(section, 'threshold_operation')
    #size_threshold = 100
    #threshold_op = '>'
    found = safebrowsing_files_local_NEW()

    for f in found:
	conditional = '{0} {1} {2}'.format(f[1], threshold_operation, size_threshold)
	if eval(conditional):
	    print('{0}: {1}'.format(f[0], f[1]))
	    #assert


