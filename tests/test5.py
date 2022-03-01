from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
from decouple import config


def test5():
    driver = webdriver.Chrome(config('CHROMEDRIVER_PATH'))

    # Case 5.1: Change language to English from Turkish
    driver.get("http://dijkstra.ug.bcc.bilkent.edu.tr/~alp.eren/cs458-p1/index.html")

    select = Select(driver.find_element(By.ID, 'language-selector'))
    select.select_by_value('en')
    driver.find_element(By.ID, "inputPassword").click()
    driver.find_element(By.ID, "inputEmail").click()

    assert driver.find_element(
        By.ID, "warningPassword").text == "Your password must contain between 4 and 60 characters."
    assert driver.find_element(
        By.ID, "remember-me-label").text == "Remember me"
    assert driver.find_element(
        By.ID, "sign-in-text").text == "Sign In"
    assert driver.find_element(
        By.ID, "inputEmail").get_attribute('placeholder') == "Email or phone number"

    # Case 5.2: Change language to Turkish from English
    select = Select(driver.find_element(By.ID, 'language-selector'))
    select.select_by_value('tr')
    driver.find_element(By.ID, "inputPassword").click()
    driver.find_element(By.ID, "inputEmail").click()

    assert driver.find_element(
        By.ID, "warningPassword").text == "Parolanız 4 ila 60 karakter olmalıdır."
    assert driver.find_element(
        By.ID, "remember-me-label").text == "Beni hatırla"
    assert driver.find_element(
        By.ID, "sign-in-text").text == "Oturum Aç"
    assert driver.find_element(
        By.ID, "inputEmail").get_attribute('placeholder') == "E-posta veya telefon numarası"

    driver.close()


test5()
