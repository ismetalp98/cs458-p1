from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
from decouple import config


def test4():
    driver = webdriver.Chrome(config('CHROMEDRIVER_PATH'))

    # Case 4.1: Remember me with email
    driver.get("https://ismetalp98.github.io/cs458-p1/")

    driver.find_element(By.ID, "inputEmail").send_keys("ismet@gmail.com")
    driver.find_element(By.ID, "inputPassword").send_keys("asd123er")
    checkbox = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[1]/input")
    checkbox.click()
    driver.find_element(By.ID, "signin-button").click()
    logout = driver.find_element(By.XPATH, "//*[@id='emptyPage']/button")
    logout.click()

    assert ("ismet@gmail.com" == driver.find_element(
        By.ID, "inputEmail").get_attribute('value')) 
    assert ("asd123er" == driver.find_element(
                By.ID, "inputPassword").get_attribute('value'))


    driver.close()
    driver = webdriver.Chrome(config('CHROMEDRIVER_PATH'))

    # Case 4.2: Remember me with phone number
    driver.get("https://ismetalp98.github.io/cs458-p1/")

    driver.find_element(By.ID, "inputEmail").send_keys("05362284637")
    driver.find_element(By.ID, "inputPassword").send_keys("Ali3457y")
    checkbox = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[1]/input")
    checkbox.click()
    driver.find_element(By.ID, "signin-button").click()
    logout = driver.find_element(By.XPATH, "//*[@id='emptyPage']/button")
    logout.click()

    assert ("05362284637" == driver.find_element(
        By.ID, "inputEmail").get_attribute('value')) 
    assert ("Ali3457y" == driver.find_element(
                By.ID, "inputPassword").get_attribute('value'))

    driver.close()
    driver = webdriver.Chrome(config('CHROMEDRIVER_PATH'))

    # Case 4.3: Not remember
    driver.get("https://ismetalp98.github.io/cs458-p1/")

    driver.find_element(By.ID, "inputEmail").send_keys("05362284637")
    driver.find_element(By.ID, "inputPassword").send_keys("Ali3457y")
    driver.find_element(By.ID, "signin-button").click()
    logout = driver.find_element(By.XPATH, "//*[@id='emptyPage']/button")
    logout.click()
    assert driver.find_element(
        By.ID, "inputEmail").get_attribute('placeholder') == "E-posta veya telefon numarası"
    assert driver.find_element(
        By.ID, "inputPassword").get_attribute('placeholder') == "Şifre"

    driver.close()