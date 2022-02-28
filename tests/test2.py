from selenium import webdriver
from selenium.webdriver.common.by import By

from decouple import config
import time


def test2():
    driver = webdriver.Chrome(config('CHROMEDRIVER_PATH'))

    # Test 2.1 After login go back and forward pages

    driver.get(
        "http://dijkstra.ug.bcc.bilkent.edu.tr/~alp.eren/cs458-p1/index.html")
    driver.find_element(By.ID, "inputEmail").send_keys("05362284637")
    driver.find_element(By.ID, "inputPassword").send_keys("Ali3457y")
    time.sleep(1)
    driver.find_element(By.ID, "signin-button").click()
    url1 = driver.current_url
    time.sleep(1)

    driver.get(
        "http://dijkstra.ug.bcc.bilkent.edu.tr/~alp.eren/cs458-p1/index.html")
    url2 = driver.current_url
    time.sleep(1)

    assert url1 == url2

    # Test 2.2 After logout go back page

    logout = driver.find_element(By.XPATH, "//*[@id='emptyPage']/button")
    logout.click()
    time.sleep(1)
    url1 = driver.current_url
    driver.back()
    time.sleep(1)
    url2 = driver.current_url
    assert url1 == url2


test2()
