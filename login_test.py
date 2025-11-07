from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture(scope="module")
def driver():
    # Cria o navegador uma vez por módulo
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_valid_login(driver):
    # Limpa cookies e garante estado inicial
    driver.delete_all_cookies()
    driver.get("https://app.telpark.com")

    assert 'elpark' in driver.title

    username = "oazaptxfcirvrkjgmq@ytnhy.com"
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys("oazaptxfcirvrkjgmq")

    driver.find_element(By.ID, 'kc-login').click()

    # Espera até que o elemento com o nome do utilizador apareça no header
    msg_elm = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#mainHeader > div.navbar-inner > div > span > a > span")
        )
    )

    assert msg_elm.text == username


def test_invalid_login(driver):
    # Limpa cookies e volta ao login
    driver.delete_all_cookies()
    driver.get("https://app.telpark.com")

    assert 'Telpark' in driver.title

    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_input.send_keys("xpto@hotmail.com")

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys("mypassword")

    driver.find_element(By.ID, 'kc-login').click()

    # Espera até que a mensagem de erro apareça
    msg_elm = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#kc-content-wrapper > div.alert.alert-error > span.kc-feedback-text")
        )
    )

    assert msg_elm.text == "Invalid username or password."
