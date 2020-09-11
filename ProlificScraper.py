from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.common import exceptions
from requests import get
from requests.exceptions import RequestException
from contextlib import closing

# source: https://realpython.com/python-web-scraping-practical-introduction/


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


def loginSite(url, email, psswrd):
    """
    open website, ideally in non-incognito mode for easy logins
    """
    opts = Options()
    browser = Firefox(options=opts)
    browser.get(url)
    username = browser.find_element_by_id("id_username")
    password = browser.find_element_by_name("password")
    username.send_keys(email)
    password.send_keys(psswrd)
    browser.find_element_by_id("login").click()


if __name__ == '__main__':
    # open Prolific website with selenium in normal windows (not incognito)
    url = r"https://app.prolific.co/studies"
    loginSite(url)

    # while True loop
    # refresh page
    # beautiful soup parse the page

    # parse page for "Select This Study" button

    # if button does not exists, refresh after some time

    # if there exists button, parse all information of the study

    # interact with a database
    # open database and connect to it
    # check if study already in database
    # add new entry containing parsed information
    # save, disconnect from database

    # next level: if there exists button then click it, reserve, notify me (telegram?)
