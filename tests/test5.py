from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
from decouple import config


def test5():
    driver = webdriver.Chrome(config('CHROMEDRIVER_PATH'))
    driver.get("http://dijkstra.ug.bcc.bilkent.edu.tr/~alp.eren/cs458-p1/")

    # Case 1.1: Check if the facebook login page opens
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[5]').click()
    time.sleep(1)

    main_window = driver.current_window_handle
    for fb_login in driver.window_handles:
        if fb_login != main_window:  # Facebook login page
            driver.switch_to.window(fb_login)
            break

    current_url = driver.current_url
    expected_url = 'http://dijkstra.ug.bcc.bilkent.edu.tr/~alp.eren/cs458-p1/fblogin.html'

    assert current_url == expected_url

    # Case 1.2: Login with empty username and password
    driver.find_element(By.ID, "u_0_0_Q6").click()
    time.sleep(1)
    no_account = driver.find_element(By.XPATH, '//*[@id="error_box1"]')

    assert no_account.is_displayed()

    # Case 1.3: Login with invalid email/phone value
    driver.find_element(By.ID, "emailfb").send_keys("mayathecat")
    time.sleep(1)
    driver.find_element(By.ID, "passfb").send_keys("12345678")
    time.sleep(1)
    driver.find_element(By.ID, "u_0_0_Q6").click()
    time.sleep(1)

    # TODO: BUNUN ÇIKMASI LAZIM
    no_account = driver.find_element(By.XPATH, '//*[@id="error_box1"]')

    # assert no_account.is_displayed()

    # Case 1.4: Login with invalid email
    driver.find_element(By.ID, "emailfb").clear()
    driver.find_element(By.ID, "passfb").clear()
    time.sleep(1)
    driver.find_element(By.ID, "emailfb").send_keys("mayathecat@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "passfb").send_keys("12345678")
    time.sleep(1)
    driver.find_element(By.ID, "u_0_0_Q6").click()
    time.sleep(1)

    # TODO: BUNUN ÇIKMASI LAZIM
    no_account = driver.find_element(By.XPATH, '//*[@id="error_box1"]')

    # assert no_account.is_displayed()

    # Case 1.5: Login with valid email and invalid password
    driver.find_element(By.ID, "emailfb").clear()
    driver.find_element(By.ID, "passfb").clear()
    time.sleep(1)
    driver.find_element(By.ID, "emailfb").send_keys("ismet@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "passfb").send_keys("12345678")
    time.sleep(1)
    driver.find_element(By.ID, "u_0_0_Q6").click()
    time.sleep(1)

    wrong_pass = driver.find_element(By.ID, 'error_box0')
    no_account = driver.find_element(By.XPATH, '//*[@id="error_box1"]')

    assert wrong_pass.is_displayed()
    assert not no_account.is_displayed()

    # Case 1.6: Login with valid email and valid password
    driver.find_element(By.ID, "emailfb").clear()
    driver.find_element(By.ID, "passfb").clear()
    time.sleep(1)
    driver.find_element(By.ID, "emailfb").send_keys("ismet@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "passfb").send_keys("asd123er")
    time.sleep(1)
    driver.find_element(By.ID, "u_0_0_Q6").click()
    time.sleep(1)

    driver.switch_to.window(main_window)
    current_url = driver.current_url
    expected_url = "http://dijkstra.ug.bcc.bilkent.edu.tr/~alp.eren/cs458-p1/emptyPage.html?logged-in"

    assert current_url == expected_url

    # Logout from the previous account and enter facebook login page again
    driver.find_element(By.XPATH, "//*[@id='emptyPage']/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[5]').click()
    main_window = driver.current_window_handle
    for fb_login in driver.window_handles:
        if fb_login != main_window:  # Facebook login page
            driver.switch_to.window(fb_login)
            break
    time.sleep(1)

    # Case 1.7: Login with invalid phone
    driver.find_element(By.ID, "emailfb").send_keys("05436786564")
    time.sleep(1)
    driver.find_element(By.ID, "passfb").send_keys("12345678")
    time.sleep(1)
    driver.find_element(By.ID, "u_0_0_Q6").click()
    time.sleep(1)

    # TODO: BUNUN ÇIKMASI LAZIM
    no_account = driver.find_element(By.XPATH, '//*[@id="error_box1"]')

    # assert no_account.is_displayed()

    # Case 1.8: Login with valid phone and invalid password
    driver.find_element(By.ID, "emailfb").clear()
    driver.find_element(By.ID, "passfb").clear()
    time.sleep(1)
    driver.find_element(By.ID, "emailfb").send_keys("05362284637")
    time.sleep(1)
    driver.find_element(By.ID, "passfb").send_keys("12345678")
    time.sleep(1)
    driver.find_element(By.ID, "u_0_0_Q6").click()
    time.sleep(1)

    wrong_pass = driver.find_element(By.ID, 'error_box0')
    no_account = driver.find_element(By.XPATH, '//*[@id="error_box1"]')

    assert wrong_pass.is_displayed()
    assert not no_account.is_displayed()

    # Case 1.8: Login with valid phone and valid password
    driver.find_element(By.ID, "emailfb").clear()
    driver.find_element(By.ID, "passfb").clear()
    time.sleep(1)
    driver.find_element(By.ID, "emailfb").send_keys("05362284637")
    time.sleep(1)
    driver.find_element(By.ID, "passfb").send_keys("Ali3457y")
    time.sleep(1)
    driver.find_element(By.ID, "u_0_0_Q6").click()
    time.sleep(1)

    assert len(driver.window_handles) == 1
    driver.switch_to.window(main_window)
    current_url = driver.current_url
    expected_url = "http://dijkstra.ug.bcc.bilkent.edu.tr/~alp.eren/cs458-p1/emptyPage.html?logged-in"

    assert current_url == expected_url


test5()
