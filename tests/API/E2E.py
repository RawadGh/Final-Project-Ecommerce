from webbrowser import get

from django.test import LiveServerTestCase
import time
import warnings
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException, ElementNotVisibleException, \
    InvalidElementStateException, StaleElementReferenceException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    firefox_driver_binary = "geckodriver.exe"
    ser_firefox = FirefoxService(firefox_driver_binary)
    driver = webdriver.Firefox(service=ser_firefox)
    yield driver
    driver.close()


# def test_login(driver):
#     driver.get("http://127.0.0.1:8000/#/")
#     driver.maximize_window()
#     driver.find_element(By.CSS_SELECTOR, "a.nav-link:nth-child(2)").click()
#     time.sleep(5)
#     driver.find_element(By.CSS_SELECTOR, "#email").send_keys("rawad@test.com")
#     time.sleep(5)
#     driver.find_element(By.CSS_SELECTOR, "#password").send_keys("Rawadgh592")
#     time.sleep(5)
#     driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
#     time.sleep(5)
#     assert driver.find_element(By.CSS_SELECTOR,"#username").text == "RAWAD"


def test_testBuyProduct(driver):
    driver.get("http://127.0.0.1:8000/#/")
    driver.maximize_window()
    driver.execute_script("window.scrollTo(0,600)")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "div.col-xl-3:nth-child(1) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "select.form-control").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "select.form-control > option:nth-child(2)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".w-100").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".w-100").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys("rawad@test.com")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("Rawadgh592")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#address").send_keys("4040/1")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#city").send_keys("Nazareth")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#postalCode").send_keys("160000")
    driver.execute_script("window.scrollTo(0,250)")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#country").send_keys("israel")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".my-3").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".my-3").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".w-100").click()
    time.sleep(2)
    assert driver.find_element(By.CSS_SELECTOR,"div.list-group-item:nth-child(5) > div:nth-child(1) > div:nth-child(2)").text == "$121.18"




















