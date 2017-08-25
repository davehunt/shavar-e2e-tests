import os
from selenium import webdriver


dir = ('safebrowsing')
sections = ['whitelist', 'blacklist', 'content', 'DNT', 'plugin']


# list all sections (prefs.ini)
def sections_list_all(conf):
    return conf.sections()


# list all items in a given section (prefs.ini)
def section_list_all(conf, name_section):
    return conf.items(name_section)


def max_file_size_index(conf):
    return conf.get('index', 'max_file_size').split(',')


# returns expected "max file size" grouping file_list from prefs.ini
def max_file_size_file_list(conf, name_section):
    return conf.get(name_section, 'file_list').split(',')


def pref_set(conf, name_pref_set):
    pass


def pref_sets_index(conf):
    return conf.get('index', 'pref_sets_index').split(',')


def pref_sets_combined_file_lists(conf, section_name):
    items = conf.items(section_name)
    file_list = []
    for (key, val) in items:
        list_tmp = val.split(',')
        for item in list_tmp:
            file_list.append(item)
    return file_list


def set_prefs(conf, sections):
    fp = webdriver.FirefoxProfile()
    for section in sections:
        items = conf.items(section)
        for (key, val) in items:
            print (key, val)
            fp.set_preference(key, val)
    return fp


def safebrowsing_files_unique():
    # return list of unique safebrowsing files (less file extension)
    f = []
    for name in os.listdir('safebrowsing'):
        file = os.path.splitext(name)[0]
        if file not in (f):
            f.append(file)
    return f


def safebrowsing_files_local():
    # return list of all local safebrowsing files
    f = []
    return [f.append(file) for name in os.listdir('safebrowsing')]


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
    #val = max_file_size_list_all(conf)
    #val = max_file_size_file_list(conf, 'whitelist')
    #val = pref_sets_index(conf)
    #val = max_file_size_index(conf)
    #val = pref_sets_combined_file_lists(conf, 'mozfull')
    print(val)
