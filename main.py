from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv
from config import config
from login import login_email
from post import post
from excel import read_from_excel
import os


if __name__ == '__main__':

    load_dotenv()

    list_of_products = read_from_excel("./OLX.xlsx")

    driver = config()

    login_email(driver)

    for product in list_of_products:
        post(driver, product)

    
