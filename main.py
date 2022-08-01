from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv
import os

load_dotenv()

options = Options()
options.page_load_strategy = 'normal'

service = Service(executable_path=os.getenv("AUTOMATION_PATH"))
driver = webdriver.Chrome(service=service)

driver.get("https://www.olx.pl/")
driver.set_window_position(3000, 0)
driver.maximize_window()
