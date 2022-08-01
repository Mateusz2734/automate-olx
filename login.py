from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import os


def login(driver):
    accept_button = WebDriverWait(driver, timeout=5).until(
        ec.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
    accept_button.click()

    your_account = WebDriverWait(driver, timeout=5).until(
        ec.element_to_be_clickable((By.ID, 'topLoginLink')))
    your_account.click()

    email = WebDriverWait(driver, timeout=5).until(
        ec.presence_of_element_located((By.ID, 'userEmail')))
    email.send_keys(os.getenv("OLX_EMAIL"))

    password = WebDriverWait(driver, timeout=5).until(
        ec.presence_of_element_located((By.ID, 'userPass')))
    password.send_keys(os.getenv("OLX_PASSWORD"))

    login_me = WebDriverWait(driver, timeout=5).until(
        ec.presence_of_element_located((By.ID, 'se_userLogin')))
    login_me.click()

    try:
        dont_show = WebDriverWait(driver, timeout=5).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div[2]/button[2]')))
        dont_show.click()
    except:
        pass
