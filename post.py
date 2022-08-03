from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


def post(driver, product):
    post_new_ad = WebDriverWait(driver, timeout=10).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="root"]/header/div/div/button')))
    post_new_ad.click()

    ad_title = WebDriverWait(driver, timeout=10).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="posting-form"]/main/div[1]/div[1]/div[1]/div/div/div/div/textarea')))
    ad_title.send_keys(product.title)

    categories_btn = WebDriverWait(driver, timeout=10).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="posting-form"]/main/div[1]/div[1]/div[2]/div')))
    categories_btn.click()

    suggested_category_btn = WebDriverWait(driver, timeout=10).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="posting-form"]/main/div[1]/div[1]/div[2]/div/div[2]/div/div/button')))
    suggested_category_btn.click()

    photo_input = WebDriverWait(driver, timeout=10).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="photo-attachment-files"]')))
    photo_input.send_keys(product.photo)

    description_input = WebDriverWait(driver, timeout=10).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="posting-form"]/main/div[1]/div[3]/div/div[1]/div/div/div/textarea')))
    description_input.send_keys(product.description)

    price_input = WebDriverWait(driver, timeout=10).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="parameters.price.price"]')))
    price_input.send_keys(product.price)

    set_private = WebDriverWait(driver, timeout=10).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/ul/li[1]/div/div/div[1]/button')))
    set_private.click()

    set_used = WebDriverWait(driver, timeout=10).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/ul/li[2]/div/div/div[1]/button')))
    set_used.click()

    size_s = WebDriverWait(driver, timeout=10).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="Band-S__toggle"]/span/div/p[2]')))
    size_s.click()

    select_inpost = WebDriverWait(driver, timeout=10).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="Band-S__collapse"]/ul/li[2]/label/input')))
    select_inpost.click()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    submit = WebDriverWait(driver, timeout=10).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="posting-form"]/main/div[1]/div[8]/div/button[2]')))
    if submit:
        print("Znaleziono")
    # submit.click()
