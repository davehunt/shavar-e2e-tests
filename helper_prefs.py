from selenium import webdriver

dir = ('safebrowsing')
sections = ['whitelist', 'blacklist', 'content', 'DNT', 'plugin']

p = []
pf = []

def get_profile_expected_files(conf, section):
    # get list of expected files in a profile

    # moztest = conf.get('moztestpub', 'urlclassifier.trackingTable')
    # pf.extend(moztest.split(','))
    # moztest_wl = conf.get('moztestpub', 'urlclassifier.trackingWhitelistTable')
    # pf.extend(moztest_wl.split(','))

    for item in section:
        items = conf.items(section)
        for (val) in items:
            pf.extend(prefs.split(','))
    return pf

def prefs_group(conf, section):
    # Go through each of the non-default prefs sections and list the files
    prefs = conf.get(section, 'file_list')
    p.extend(prefs.split(','))
    return p

    for section in sections:
        prefs_group(section)

def set_prefs(conf, sections):
    fp = webdriver.FirefoxProfile()
    for section in sections:
        items = conf.items(section)
        for (key, val) in items:
            print (key, val)
            fp.set_preference(key, val)
    return fp
