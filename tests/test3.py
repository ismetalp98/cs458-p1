from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
from decouple import config


def test3():
    driver = webdriver.Chrome(config('CHROMEDRIVER_PATH'))

    driver.get(
        "http://dijkstra.ug.bcc.bilkent.edu.tr/~alp.eren/cs458-p1/index.html")

    # Test 3.1 copy from email paste to password

    email = driver.find_element(By.ID, 'inputEmail')
    email.send_keys("asd123er")
    time.sleep(1)

    act = ActionChains(driver)
    act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
    password = driver.find_element(By.ID, 'inputPassword')
    password.click()
    act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    time.sleep(1)

    email.click()
    act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    email.send_keys("ismet@gmail.com")
    time.sleep(1)

    driver.find_element(By.ID, "signin-button").click()
    time.sleep(1)

    assert driver.find_element(By.ID, "signin-button")

    # Test 3.2 copy from password pass to email when it is hidden

    password.click()
    act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    password.send_keys("ismet@gmail.com")
    time.sleep(1)

    act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

    email.click()
    act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    time.sleep(1)

    password.click()
    act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    password.send_keys("asd123er")
    time.sleep(1)

    driver.find_element(By.ID, "signin-button").click()
    time.sleep(1)

    assert driver.find_element(By.ID, "signin-button")

    # Test 3.3 copy from password pass to email when it is not hidden

    password.click()
    act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    password.send_keys("ismet@gmail.com")
    time.sleep(1)

    show = driver.find_element(By.XPATH, "//div[@class='showWrap']")
    show.click()
    time.sleep(1)

    password.click()
    act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

    email.click()
    act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    time.sleep(1)

    password.click()
    act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    password.send_keys("asd123er")
    time.sleep(1)

    driver.find_element(By.ID, "signin-button").click()
    time.sleep(1)

    assert driver.find_element(By.XPATH, "//*[@id='emptyPage']/button")


test3()
