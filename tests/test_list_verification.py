import requests


def test_list_verification():
    url = "https://shavar.stage.mozaws.net/list?client=foo&appver=1&pver=2.2"
    r = requests.get(url)
    print(r.text)

def test_list_mozstd():
    url = 'https://shavar.stage.mozaws.net/downloads?client=foo&appver=1&pver=2.2'
    data = "mozstd-track-digest256;"
    r = requests.post(url, data)
    print(r.text)
