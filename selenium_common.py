from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as geckoOptions
from selenium.webdriver.chrome.options import Options as chromeOptions

from time import sleep
import sys


def init_selenium(web_driver,headless=False):
    if web_driver == "firefox":
        browser = gecko_setup(headless=headless)
    elif web_driver == "chrome":
        browser = chrome_setup(headless=headless)
    return browser


def gecko_setup(headless=False):
    options = geckoOptions()
    options.add_argument('--disable-gpu')
    if headless==True:
        options.add_argument('--headless')
    if sys.platform.startswith('linux'):  # any linux 64bit
        browser = webdriver.Firefox(
            executable_path="./drivers/linux/geckodriver", options=options)
    elif sys.platform.startswith('darwin'):  # any macos
        browser = webdriver.Firefox(
            executable_path="./drivers/macos/geckodriver", options=options)
    elif sys.platform.startswith('cygwin'):  # any windows 64bit
        browser = webdriver.Firefox(
            executable_path="./drivers/windows/geckodriver.exe", options=options)
    return browser


def chrome_setup(headless=False):
    options = chromeOptions()
    options.add_argument('--disable-gpu')
    if headless==True:
        options.add_argument('--headless')
    if sys.platform.startswith('linux'):  # any linux 64bit
        browser = webdriver.Chrome(
            executable_path="./drivers/linux/chromedriver", options=options)
    elif sys.platform.startswith('darwin'):  # any macos
        browser = webdriver.Chrome(
            executable_path="./drivers/macos/chromedriver", options=options)
    elif sys.platform.startswith('cygwin'):  # any windows 64bit
        browser = webdriver.Chrome(
            executable_path="./drivers/windows/chromedriver.exe", options=options)
    return browser

if __name__ == "__main__":
	br = init_selenium("firefox")
	br.get("www.google.com")
	sleep(60)
	br.quit()
	

