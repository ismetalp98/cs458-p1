from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time


def test1():
    driver = webdriver.Chrome(
        "D:\chromedriver_win32\chromedriver.exe")
    driver.get("http://dijkstra.ug.bcc.bilkent.edu.tr/~alp.eren/cs458/")

    # Case 1.1: Login with empty username and password
    driver.find_element(By.ID, "signin-button").click()
    time.sleep(2)

    warn_mail_phone = driver.find_element(By.ID, "warningEmailEmp")
    warn_pass = driver.find_element(By.ID, "warningPassword")

    assert warn_mail_phone.is_displayed()
    assert warn_pass.is_displayed()

    # Case 1.2: Login with invalid email/phone value
    driver.find_element(By.ID, "inputEmail").send_keys("mayathecat")
    time.sleep(1)
    driver.find_element(By.ID, "inputPassword").send_keys("12345678")
    time.sleep(1)
    driver.find_element(By.ID, "signin-button").click()
    time.sleep(2)

    warn_invalid_email = driver.find_element(By.ID, "warningEmailEmail")
    warn_invalid_pass = driver.find_element(By.ID, "warningPassword")

    assert warn_invalid_email.is_displayed()
    assert not warn_invalid_pass.is_displayed()

    # Case 1.3: Login with invalid email
    driver.find_element(By.ID, "inputEmail").clear()
    driver.find_element(By.ID, "inputPassword").clear()
    time.sleep(1)
    driver.find_element(By.ID, "inputEmail").send_keys("mayathecat@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "inputPassword").send_keys("12345678")
    driver.find_element(By.ID, "signin-button").click()
    time.sleep(2)

    no_account = driver.find_element(
        By.XPATH, "//*[@id='userNot']/div[2]")
    warn_invalid_email = driver.find_element(By.ID, "warningEmailEmail")
    warn_invalid_pass = driver.find_element(By.ID, "warningPassword")

    assert no_account.is_displayed()
    assert not warn_invalid_email.is_displayed()
    assert not warn_invalid_pass.is_displayed()

    # Case 1.4: Login with valid email and invalid password
    driver.find_element(By.ID, "inputEmail").clear()
    driver.find_element(By.ID, "inputPassword").clear()
    time.sleep(1)
    driver.find_element(By.ID, "inputEmail").send_keys("ismet@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "inputPassword").send_keys("12345678")
    time.sleep(1)
    driver.find_element(By.ID, "signin-button").click()
    time.sleep(2)

    wrong_pass = driver.find_element(
        By.XPATH, "//*[@id='passNot']/div[2]")
    warn_invalid_email = driver.find_element(By.ID, "warningEmailEmail")
    warn_invalid_pass = driver.find_element(By.ID, "warningPassword")

    assert wrong_pass.is_displayed()
    assert not warn_invalid_email.is_displayed()
    assert not warn_invalid_pass.is_displayed()

    # Case 1.5: Login with valid email and valid password
    driver.find_element(By.ID, "inputEmail").clear()
    driver.find_element(By.ID, "inputPassword").clear()
    time.sleep(1)
    driver.find_element(By.ID, "inputEmail").send_keys("ismet@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "inputPassword").send_keys("asd123er")
    time.sleep(1)
    driver.find_element(By.ID, "signin-button").click()
    time.sleep(2)

    current_url = driver.current_url
    expected_url = "http://dijkstra.ug.bcc.bilkent.edu.tr/~alp.eren/cs458/emptyPage.html?logged-in"

    assert current_url == expected_url

    # Case 1.6: Login with invalid phone
    # Logout from the previous account
    driver.find_element(By.XPATH, "//*[@id='emptyPage']/button").click()

    driver.find_element(By.ID, "inputEmail").send_keys("505")
    time.sleep(1)
    driver.find_element(By.ID, "inputPassword").send_keys("12345678")
    time.sleep(1)
    driver.find_element(By.ID, "signin-button").click()
    time.sleep(2)

    warn_invalid_phone = driver.find_element(By.ID, "warningEmailPhone")
    warn_invalid_pass = driver.find_element(By.ID, "warningPassword")

    assert warn_invalid_phone.is_displayed()
    assert not warn_invalid_pass.is_displayed()

    # Case 1.7: Login with valid phone and invalid password
    driver.find_element(By.ID, "inputEmail").clear()
    driver.find_element(By.ID, "inputPassword").clear()
    time.sleep(1)
    driver.find_element(By.ID, "inputEmail").send_keys("05362284637")
    time.sleep(1)
    driver.find_element(By.ID, "inputPassword").send_keys("12345678")
    time.sleep(1)
    driver.find_element(By.ID, "signin-button").click()
    time.sleep(2)

    wrong_pass = driver.find_element(
        By.XPATH, "//*[@id='passNot']/div[2]")
    warn_invalid_phone = driver.find_element(By.ID, "warningEmailPhone")
    warn_invalid_pass = driver.find_element(By.ID, "warningPassword")

    assert wrong_pass.is_displayed()
    assert not warn_invalid_phone.is_displayed()
    assert not warn_invalid_pass.is_displayed()

    # Case 1.8: Login with valid phone and valid password
    driver.find_element(By.ID, "inputEmail").clear()
    driver.find_element(By.ID, "inputPassword").clear()
    time.sleep(1)
    driver.find_element(By.ID, "inputEmail").send_keys("05362284637")
    time.sleep(1)
    driver.find_element(By.ID, "inputPassword").send_keys("Ali3457y")
    time.sleep(1)
    driver.find_element(By.ID, "signin-button").click()
    time.sleep(2)

    current_url = driver.current_url
    expected_url = "http://dijkstra.ug.bcc.bilkent.edu.tr/~alp.eren/cs458/emptyPage.html?logged-in"

    assert current_url == expected_url


test1()
