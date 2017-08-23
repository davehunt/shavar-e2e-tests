from selenium import webdriver


dir = ('safebrowsing')
sections = ['whitelist', 'blacklist', 'content', 'DNT', 'plugin']

p = []
pf = []

def sections_list_all(conf):
    return conf.sections()

def section_list_all(conf, name_section):
    return conf.items(name_section)

# returns expected "prefs-list" list from prefs.ini
def pref_set_file_list(conf, name_section):
    return conf.get(name_section, 'file_list').split(',')

def pref_sets_list_all(conf):
    return conf.get('index', 'pref_sets_index').split(',')

def max_file_size_list_all(conf):
    return conf.get('index', 'max_file_size').split(',')

def pref_set(conf, name_pref_set):
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


if __name__ == '__main__':
    import ConfigParser
 
    def conf():
	config = ConfigParser.ConfigParser()
	config.read('./prefs.ini')
	return config
    conf = conf()

    #val = sections_list_all(conf)
    #val = section_list_all(conf, 'DNT')
    #val = pref_set_file_list(conf, 'DNT')
    #val = pref_sets_list_all(conf)
    val = max_file_size_list_all(conf)
    print(val)
