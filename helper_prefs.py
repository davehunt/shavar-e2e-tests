from selenium import webdriver

dir = ('safebrowsing')
sections = ['whitelist', 'blacklist', 'content', 'DNT', 'plugin']

p = []
pf = []


def pref_sets_list_all(conf):
    pass

def pref_set(name_pref_set):
    pass

def pref_set_files_in_safebrowsing_dir(conf, section):
    # get list of expected files in a profile
    for item in section:
        items = conf.items(section)
        for val in items:
            # subval = val.split()
            # pf.extend(subval)
            # pf.extend(val.split(','))
            pf.extend(val)
            print ('val goes here', val)
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
