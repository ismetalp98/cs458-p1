from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
from decouple import config


def test1():
    base_path = "https://ismetalp98.github.io/cs458-p1/"
    driver = webdriver.Chrome(config('CHROMEDRIVER_PATH'))
    driver.get(base_path)

    # Case 1.1: Login with invalid username and password
    driver.get(base_path)
    driver.find_element(By.ID, "signin-button").click()
    warn_mail_phone = driver.find_element(By.ID, "warningEmailEmp")
    warn_pass = driver.find_element(By.ID, "warningPassword")
    assert warn_mail_phone.is_displayed()
    assert warn_pass.is_displayed()

    # Case 1.2: Login with invalid email/phone value
    driver.get(base_path)
    driver.find_element(By.ID, "inputEmail").send_keys("mayathecat")
    driver.find_element(By.ID, "inputPassword").send_keys("12345678")
    driver.find_element(By.ID, "signin-button").click()
    warn_invalid_email = driver.find_element(By.ID, "warningEmailEmail")
    warn_invalid_pass = driver.find_element(By.ID, "warningPassword")
    assert warn_invalid_email.is_displayed()
    assert not warn_invalid_pass.is_displayed()

    # Case 1.3: Login with non-exisitng email
    driver.get(base_path)
    driver.find_element(By.ID, "inputEmail").send_keys("mayathecat@gmail.com")
    driver.find_element(By.ID, "inputPassword").send_keys("Agrt67u")
    driver.find_element(By.ID, "signin-button").click()
    no_account = driver.find_element(
        By.XPATH, '//*[@id="userNot"]/div[2]')
    warn_invalid_email = driver.find_element(By.ID, "warningEmailEmail")
    warn_invalid_pass = driver.find_element(By.ID, "warningPassword")
    assert no_account.is_displayed()
    assert not warn_invalid_email.is_displayed()
    assert not warn_invalid_pass.is_displayed()

    # Case 1.4: Login with existing email and wrong password
    driver.get(base_path)
    driver.find_element(By.ID, "inputEmail").send_keys("ismet@gmail.com")
    driver.find_element(By.ID, "inputPassword").send_keys("12345678")
    driver.find_element(By.ID, "signin-button").click()
    wrong_pass = driver.find_element(
        By.XPATH, "//*[@id='passNot']/div[2]")
    warn_invalid_email = driver.find_element(By.ID, "warningEmailEmail")
    warn_invalid_pass = driver.find_element(By.ID, "warningPassword")
    assert wrong_pass.is_displayed()
    assert not warn_invalid_email.is_displayed()
    assert not warn_invalid_pass.is_displayed()

    # Case 1.5: Login with existing email and valid password
    driver.get(base_path)
    driver.find_element(By.ID, "inputEmail").send_keys("ismet@gmail.com")
    driver.find_element(By.ID, "inputPassword").send_keys("asd123er")
    driver.find_element(By.ID, "signin-button").click()
    current_url = driver.current_url
    expected_url = base_path + "emptyPage.html?logged-in"
    assert current_url == expected_url

    # Case 1.6: Login with invalid phone
    # Logout from the previous account
    driver.find_element(By.XPATH, "//*[@id='emptyPage']/button").click()
    driver.find_element(By.ID, "inputEmail").send_keys("505")
    driver.find_element(By.ID, "signin-button").click()
    warn_invalid_phone = driver.find_element(By.ID, "warningEmailPhone")
    warn_invalid_pass = driver.find_element(By.ID, "warningPassword")
    assert warn_invalid_phone.is_displayed()
    assert warn_invalid_pass.is_displayed()

    # Case 1.7: Login with existing phone and wrong password
    driver.get(base_path)
    driver.find_element(By.ID, "inputEmail").send_keys("05362284637")
    driver.find_element(By.ID, "inputPassword").send_keys("12345678")
    driver.find_element(By.ID, "signin-button").click()
    wrong_pass = driver.find_element(
        By.XPATH, "//*[@id='passNot']/div[2]")
    warn_invalid_phone = driver.find_element(By.ID, "warningEmailPhone")
    warn_invalid_pass = driver.find_element(By.ID, "warningPassword")
    assert wrong_pass.is_displayed()
    assert not warn_invalid_phone.is_displayed()
    assert not warn_invalid_pass.is_displayed()

    # Case 1.8: Login with valid phone and correct password
    driver.get(base_path)
    driver.find_element(By.ID, "inputEmail").send_keys("05362284637")
    driver.find_element(By.ID, "inputPassword").send_keys("Ali3457y")
    driver.find_element(By.ID, "signin-button").click()
    current_url = driver.current_url
    expected_url = base_path + "emptyPage.html?logged-in"
    assert current_url == expected_url

    # Logout from the previous account for facebook login
    driver.find_element(By.XPATH, "//*[@id='emptyPage']/button").click()

    # Case 1.9: Check if the facebook login page opens
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[5]').click()
    main_window = driver.current_window_handle
    for fb_login in driver.window_handles:
        if fb_login != main_window:  # Facebook login page
            driver.switch_to.window(fb_login)
            break
    current_url = driver.current_url
    assert 'facebook.com' in current_url

    # Case 1.10: Login with empty username and password
    driver.find_element(By.ID, "loginbutton").click()
    time.sleep(1)
    inc_email_phone = driver.find_element(
        By.ID, 'error_box')
    assert inc_email_phone.is_displayed()

    # Case 1.11: Login with incorrect email
    driver.find_element(By.ID, "email").send_keys("mayathecattolatte")
    driver.find_element(By.ID, "pass").send_keys("sdf456yt")
    driver.find_element(By.ID, "loginbutton").click()
    time.sleep(1)
    inc_email_phone = driver.find_element(By.ID, 'error_box')
    assert inc_email_phone.is_displayed()

    # Case 1.12: Login with incorrect email
    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "pass").clear()
    driver.find_element(By.ID, "email").send_keys("hayirlimayalar@gmail.com")
    driver.find_element(By.ID, "pass").send_keys("sdg456er")
    driver.find_element(By.ID, "loginbutton").click()
    time.sleep(1)
    inc_email_phone = driver.find_element(By.ID, 'error_box')
    assert inc_email_phone.is_displayed()

    # Case 1.13: Login with existing email and wrong password
    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "pass").clear()
    driver.find_element(By.ID, "email").send_keys("mayatheozsoy@gmail.com")
    driver.find_element(By.ID, "pass").send_keys("klmldsgk")
    driver.find_element(By.ID, "loginbutton").click()
    time.sleep(2)
    inc_email_phone = driver.find_element(By.ID, 'error_box')
    assert inc_email_phone.is_displayed()

    # Case 1.14: Login with existing email and correct password
    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "pass").clear()
    driver.find_element(By.ID, "email").send_keys("mayatheozsoy@gmail.com")
    driver.find_element(By.ID, "pass").send_keys("thecatnamedmaya")
    driver.find_element(By.ID, "loginbutton").click()
    time.sleep(2)
    driver.switch_to.window(main_window)
    current_url = driver.current_url
    expected_url = base_path + "emptyPage.html?logged-in"
    assert current_url == expected_url

    # Logout from the previous account and enter facebook login page again
    driver.find_element(By.XPATH, "//*[@id='emptyPage']/button").click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[5]').click()
    main_window = driver.current_window_handle
    for fb_login in driver.window_handles:
        if fb_login != main_window:  # Facebook login page
            driver.switch_to.window(fb_login)
            break

    # Case 1.15: Login with incorrect phone and empty password field
    time.sleep(2)
    driver.find_element(By.ID, "email").send_keys("05436786564")
    driver.find_element(By.ID, "loginbutton").click()
    inc_email_phone = driver.find_element(By.ID, 'error_box')
    assert inc_email_phone.is_displayed()

    # Case 1.16: Login with existing phone and wrong password
    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "pass").clear()
    driver.find_element(By.ID, "email").send_keys("05319215595")
    driver.find_element(By.ID, "pass").send_keys("fgh567may")
    driver.find_element(By.ID, "loginbutton").click()
    time.sleep(1)
    wrong_pass = driver.find_element(By.ID, 'error_box')
    assert wrong_pass.is_displayed()

    # Case 1.17: Login with existing phone and correct password
    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "pass").clear()
    driver.find_element(By.ID, "email").send_keys("05319215595")
    driver.find_element(By.ID, "pass").send_keys("thecatnamedmaya")
    driver.find_element(By.ID, "loginbutton").click()  # login button
    assert len(driver.window_handles) == 1
    driver.switch_to.window(main_window)
    current_url = driver.current_url
    expected_url = base_path + "emptyPage.html?logged-in"
    assert current_url == expected_url


test1()
