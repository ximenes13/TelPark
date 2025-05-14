from time import sleep
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_valid_login(driver):
    driver.get("https://app.telpark.com")
    assert 'Log in to Telpark' in driver.title

    username = "oazaptxfcirvrkjgmq@ytnhy.com"
    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys("oazaptxfcirvrkjgmq")

    driver.find_element(By.ID, 'kc-login').click()

    sleep(2)

    msg_elm = driver.find_element(By.CSS_SELECTOR, "#mainHeader > div.navbar-inner > div > span > a > span")

    assert msg_elm is not None

    assert msg_elm.text == username

def test_invalid_login(driver):
    driver.get("https://app.telpark.com")
    assert 'Log in to Telpark' in driver.title

    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys("xpto@hotmail.com")

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys("mypassword")

    sleep(2)

    driver.find_element(By.ID, 'kc-login').click()

    msg_elm = driver.find_element(By.CSS_SELECTOR,
                                  "#kc-content-wrapper > div.alert.alert-error > span.kc-feedback-text")
    assert msg_elm is not None

    assert msg_elm.text == "Invalid username or password."


