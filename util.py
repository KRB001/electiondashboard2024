import requests
from exceptions import NetworkError, StatusError, DriverAccessError
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.common import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

BOLD = "\033[1m"
RESET = "\033[0m"
DEM = "\033[1;34m"
REP = "\033[1;31m"

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

def do_driver(url, class_names):

    url = "https://" + url

    options = webdriver.FirefoxOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")
    with webdriver.Firefox(options=options) as driver:
        try:
            driver.get(url)
        except WebDriverException as err:
            raise DriverAccessError(f"Couldn't access {url}")

        results = []

        for class_name in class_names:
            results.append(driver.find_element(By.CLASS_NAME, class_name).text)

        return results


def generate_leader_string(scrape, curr, prev, dem, rep):
    if rep == scrape[0]:
        curr = curr * -1.0

    diff = curr - prev

    leader_string = ""

    if dem == scrape[0]:
        leader_string = leader_string + DEM
    else:
        leader_string = leader_string + REP

    leader_string = leader_string + scrape[0] + str(scrape[1])

    if diff > 0.0:
        if dem == scrape[0]:
            leader_string = leader_string + RESET + DEM + " (" + "+"
        else:
            leader_string = leader_string + RESET + DEM + " (" + "-"
    elif diff < 0.0:
        if dem  == scrape[0]:
            leader_string = leader_string + RESET + REP + " (" + "-"
        else:
            leader_string = leader_string + RESET + REP + " (" + "+"
    else:
        leader_string = leader_string + RESET + "(~"

    leader_string = leader_string + str(abs(diff))[0:3] + ")"

    return leader_string