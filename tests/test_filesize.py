# This test should only test filesizes when the file exists
# TODO: check setup to make sure to verify that all the files shavar should
# have delivered to the cache are actually there.

# 1. get list of files from /safebrowsing
# 2. get filesizes of ^^
# 3. add filename/size key pairs to dict
# 4. get prefs header [ex: whitelist], compare to files in dict and verify size is under maximum


import ConfigParser
import os


parser = ConfigParser.SafeConfigParser()
parser.read('prefs.ini')

dir = ('safebrowsing')
sections = ['whitelist', 'blacklist', 'content', 'DNT', 'plugin']

p = []
f = []

def prefs_group(section):
    # Go through each of the non-default prefs sections and list the files
    prefs = parser.get(section, 'file_list')
    p.extend(prefs.split(','))
    print(p)
    return p
for section in sections:
    prefs_group(section)

def test_safebrowsing():
    """Hardcoded location of safebrowsing directory will need to be updated
    to reflect new FF profile file directory"""
    # Get list of files
    for name in os.listdir('safebrowsing'):
        filename = os.path.join('safebrowsing', name)
        if os.path.isfile(filename):
            f.append(filename)
    # Create list with filename, size tuples
    for i in xrange(len(f)):
        f[i] = (os.path.splitext(f[i])[0], os.path.getsize(f[i]))
    return f
