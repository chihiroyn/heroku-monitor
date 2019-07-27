from selenium import webdriver
import chromedriver_binary
from time import sleep

import os
from os.path import join, dirname
from dotenv import load_dotenv

from shoppingSite import ShoppingSite

import pyautogui

browser = webdriver.Chrome()
DEFAULT_WAIT = 3

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# get information about certification from environment variable
ACCOUNT = os.environ['ACCOUNT']
PASSWORD = os.environ['PASSWORD']

class HerokuAdmin(ShoppingSite):
    def login(self):
        # jump to login page
        url = 'https://id.heroku.com/login'

        # URLで指定したHTML文書を取得
        browser.get(url)
        sleep(DEFAULT_WAIT)

        # enter account
        browser.find_element_by_name('email').send_keys(ACCOUNT)
        # enter password
        browser.find_element_by_name('password').send_keys(PASSWORD)
        # click login button
        browser.find_element_by_xpath('//*[@id="login"]/form/button').click()

        super().login()

def main():
    herokuAdmin = HerokuAdmin()

    sleep(5)
    print(pyautogui.locateCenterOnScreen('success_icon.png'))

if (__name__ == "__main__"):
    main()