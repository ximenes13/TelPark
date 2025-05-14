from time import sleep, time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest


from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()

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

    yield driver
    driver.quit()


def test_add_vehicle(driver):
    driver.get("https://app.telpark.com/es/vehicles")

    sleep(1)

    try:
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
    except:
        pass

    sleep(1)

    vehicles = driver.find_elements(By.ID, "vehicles")
    initial_vehicles_count = len(vehicles)

    new_vehicle_elm = driver.find_element(By.ID, "aNewVehicle")

    assert new_vehicle_elm is not None
    new_vehicle_elm.click()

    sleep(1)

    vehicle_name ="xpto"
    name_vehicle_elm = driver.find_element(By.XPATH, "//*[contains(@id, 'id')]/div[2]/div[2]/input[1]")
    assert name_vehicle_elm is not None
    name_vehicle_elm.send_keys(vehicle_name)

    vehicle_nameplate = "xpto"
    name_plate_elm = driver.find_element(By.XPATH, "//*[contains(@id, 'id')]/div[2]/div[2]/input[2]")
    assert name_plate_elm is not None
    name_plate_elm.send_keys(vehicle_nameplate)

    select_box_elm = driver.find_element(By.XPATH, "//*[contains(@id, 'id')]/div[2]/div[2]/select")
    select_box = Select(select_box_elm)
    select_box.select_by_value("0")

    save_btn_elm = driver.find_element(By.XPATH, "//*[contains(@id, 'id') and @type='submit']")
    assert save_btn_elm is not None
    save_btn_elm.click()

    sleep(1)

    vehicles = driver.find_elements(By.CSS_SELECTOR, 'span[id="vehicles"]')
    actual_vehicles_count = len(vehicles)
    assert (initial_vehicles_count + 1) == actual_vehicles_count

    vehicle_found = False

    for vehicle in vehicles:
        try:
            name = vehicle.find_element(By.XPATH, ".//div/div/div[2]/span").text
            nameplate = vehicle.find_element(By.XPATH, ".//div/div/div[4]/span").text
            if name == vehicle_name and nameplate == vehicle_nameplate.upper():
                vehicle_found = True
                break
        except:
            continue

    assert vehicle_found


def test_remove_vehicle(driver):
    driver.get("https://app.telpark.com/es/vehicles")

    sleep(1)

    try:
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
    except:
        pass

    sleep(1)

    edit_elm = driver.find_element(By.XPATH, "//*[@class='btn btn-small btn-info vehiclebtnbig']")
    assert edit_elm is not None
    edit_elm.click()

    sleep(1)

    delete_vehicle_elm = driver.find_element(By.XPATH, "//*[@class='close']")
    assert delete_vehicle_elm is not None
    delete_vehicle_elm.click()

    delete_button_elm = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Delete")))
    assert delete_button_elm is not None
    delete_button_elm.click()

    sleep(1)
