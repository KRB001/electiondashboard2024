import requests
from exceptions import NetworkError, StatusError
from bs4 import BeautifulSoup as bs

def do_request(url):
    headers_get = {
        'User-Agent': 'Mozilla/5.0'
    }
    url = "https://" + url
    res = None
    try:
        res = requests.get(url, headers=headers_get)
    except requests.exceptions.ConnectionError as err:
        raise NetworkError(f'Failed due to connection error {err}')
    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise StatusError(f'Failed with status {res.status_code}: {err}')

    return bs(res.text, 'html.parser')