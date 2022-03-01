from selenium import webdriver
from selenium.webdriver.common.by import By

from decouple import config
import time


def test2():
    driver = webdriver.Chrome(config('CHROMEDRIVER_PATH'))

    # Test 2.1 After login go back and forward pages

    driver.get(
        "https://ismetalp98.github.io/cs458-p1/")
    driver.find_element(By.ID, "inputEmail").send_keys("05362284637")
    driver.find_element(By.ID, "inputPassword").send_keys("Ali3457y")
    time.sleep(1)
    driver.find_element(By.ID, "signin-button").click()
    url1 = driver.current_url
    time.sleep(1)

    driver.get("https://ismetalp98.github.io/cs458-p1/")
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

    # Test 2.3 After login with mail go back and forward pages

    driver.get("https://ismetalp98.github.io/cs458-p1/")
    driver.find_element(By.ID, "inputEmail").send_keys("ismet@gmail.com")
    driver.find_element(By.ID, "inputPassword").send_keys("asd123er")
    time.sleep(1)
    driver.find_element(By.ID, "signin-button").click()
    url1 = driver.current_url
    time.sleep(1)

    driver.get("https://ismetalp98.github.io/cs458-p1/")
    url2 = driver.current_url
    time.sleep(1)

    assert url1 == url2

    # Test 2.4 After logout go back page

    logout = driver.find_element(By.XPATH, "//*[@id='emptyPage']/button")
    logout.click()
    time.sleep(1)
    url1 = driver.current_url
    driver.back()
    time.sleep(1)
    url2 = driver.current_url
    assert url1 == url2

    # Test 2.5 After login with facebook go back and forward pages

    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[5]').click()
    time.sleep(3)

    main_window = driver.current_window_handle
    for fb_login in driver.window_handles:
        if fb_login != main_window:  # Facebook login page
            driver.switch_to.window(fb_login)
            break

    driver.find_element(By.ID, "email").send_keys("alp@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "pass").send_keys("fds135bo")
    time.sleep(1)
    driver.find_element(By.ID, "loginbutton").click()
    time.sleep(1)

    driver.switch_to.window(main_window)
    current_url = driver.current_url
    expected_url = "https://ismetalp98.github.io/cs458-p1/emptyPage.html?logged-in"

    assert current_url == expected_url

    url1 = current_url
    driver.get("https://ismetalp98.github.io/cs458-p1/")
    time.sleep(1)
    url2 = driver.current_url
    assert url1 == url2


test2()
