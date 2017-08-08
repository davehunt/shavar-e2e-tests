from selenium import webdriver


def set_prefs(conf, sections):
    fp = webdriver.FirefoxProfile()
    for section in sections:
        items = conf.items(section)
        for (key, val) in items:
            print (key, val)
            fp.set_preference(key, val)
    return fp
