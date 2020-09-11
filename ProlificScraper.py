from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.common import exceptions
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import getpass
import time

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


def getCreds():
    """
    Ask user for username, then password, then returns both values
    """
    email = getpass.getpass(prompt="Email: ")
    pwd = getpass.getpass(prompt="Password: ")
    return (email, pwd)


def loginSite(url, email, psswrd):
    """
    open website, ideally in non-incognito mode for easy logins
    """
    opts = Options()
    browser = Firefox(options=opts)
    browser.get(url)
    username = browser.find_element_by_name("username")
    password = browser.find_element_by_name("password")
    username.send_keys(email)
    password.send_keys(psswrd)
    browser.find_element_by_id("login").click()


opts = Options()
browser = Firefox(options=opts)
browser.get(r"https://app.prolific.co/studies")
username = browser.find_element_by_name("username")
username.send_keys("derekho4.20@gmail.com")
password = browser.find_element_by_name("password")
password.send_keys("Welcome2Prolific")
browser.find_element_by_id("login").click()

# loginSite(r"https://app.prolific.co/studies", "derekho4.20@gmail.com", "Welcome2Prolific")
# when study appears:
# source code for button:


# "reserve place" button leds to this event:
# source code for button is:
# <button class="el-button button el-button--primar el-button--xl"
# data-v-bf6a7d82="" type="submit" data-tid="reserve>"
# has an event: https://app.prolific.co/js/chunk-vendors.5f8c32b8.js:7:51647
# try using:
# bowser.find_element_by_partial_link_text(r"https://app.prolific.co/js/chunk-vendors.")
# browser.find_element_by_class_name("el-button button el-button--primar el-button--xl")


def main():
    # open Prolific website with selenium in normal windows (not incognito)
    url = r"https://app.prolific.co/studies"
    creds = getCreds()
    loginSite(url, creds[0], creds[1])


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


if __name__ == '__main__':
    main()
