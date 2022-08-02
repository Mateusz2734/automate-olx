from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

class Product:
    description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras faucibus lectus in orci volutpat varius. Proin iaculis ex elit, id aliquet lacus rhoncus eu. In id ligula a felis mattis fringilla. Suspendisse ut accumsan elit, sit amet mattis ipsum. Mauris porta tortor quis purus sodales, quis aliquam ipsum molestie. Aliquam dignissim egestas dolor, id volutpat turpis efficitur quis. Aliquam pharetra justo leo, porttitor euismod dui vulputate imperdiet. Duis rutrum est ac odio suscipit elementum. Integer maximus tincidunt augue quis volutpat. Nam in mattis augue, non hendrerit justo. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum bibendum metus a mauris mollis, eu dapibus risus bibendum."
    title = "Book of every "
    photo = "C:/path/to/photo.jpg"
    price = 15

sample_product = Product()

def post(driver):
    post_new_ad = WebDriverWait(driver, timeout=5).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="root"]/header/div/div/button')))
    post_new_ad.click()

    ad_title = WebDriverWait(driver, timeout=5).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="posting-form"]/main/div[1]/div[1]/div[1]/div/div/div/div/textarea')))
    ad_title.send_keys(sample_product.title)

    categories_btn = WebDriverWait(driver, timeout=5).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="posting-form"]/main/div[1]/div[1]/div[2]/div')))
    categories_btn.click()

    suggested_category_btn = WebDriverWait(driver, timeout=5).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="posting-form"]/main/div[1]/div[1]/div[2]/div/div[2]/div/div/button')))
    suggested_category_btn.click()

    photo_input = WebDriverWait(driver, timeout=5).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="photo-attachment-files"]')))
    photo_input.send_keys(sample_product.photo)

    description_input = WebDriverWait(driver, timeout=5).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="posting-form"]/main/div[1]/div[3]/div/div[1]/div/div/div/textarea')))
    description_input.send_keys(sample_product.description)

    price_input = WebDriverWait(driver, timeout=5).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="posting-form"]/main/div[1]/div[3]/div/div[1]/div/div/div/textarea')))
    price_input.send_keys(sample_product.price)

    set_private = WebDriverWait(driver, timeout=5).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/ul/li[1]/div/div/div[1]/button')))
    set_private.click()

    set_used = WebDriverWait(driver, timeout=5).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="posting-form"]/main/div[1]/div[4]/div/div[2]/ul/li[3]/div/div/div[1]/button')))
    set_used.click()

    submit = WebDriverWait(driver, timeout=5).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="posting-form"]/main/div[1]/div[7]/div/button[2]')))
    submit.click()