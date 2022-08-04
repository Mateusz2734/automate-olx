from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os


def config():
    options = Options()
    options.page_load_strategy = 'normal'
    options.add_argument("--incognito")

    service = Service(executable_path=os.getenv("CHROME_DRIVER_PATH"))
    driver = webdriver.Chrome(service=service)

    driver.get("https://www.olx.pl/")
    driver.set_window_position(3000, 0)
    driver.maximize_window()
    return driver
