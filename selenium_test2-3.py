# cases 2-3
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test3():
    PATH = "C:\driver\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("http://dijkstra.ug.bcc.bilkent.edu.tr/~alp.eren/cs458/")

    # test 3.1 copy from email paste to password

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

    # test 3.2 copy from password pass to email when it is hidden

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

    # test 3.3 copy from password pass to email when it is not hidden

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


def test2():
    PATH = "C:\driver\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    # test 2.1 after login go back and forward pages

    driver.get("http://dijkstra.ug.bcc.bilkent.edu.tr/~alp.eren/cs458/")
    driver.find_element(By.ID, "inputEmail").send_keys("05362284637")
    driver.find_element(By.ID, "inputPassword").send_keys("Ali3457y")
    time.sleep(1)
    driver.find_element(By.ID, "signin-button").click()
    url1 = driver.current_url
    time.sleep(1)

    driver.get("http://dijkstra.ug.bcc.bilkent.edu.tr/~alp.eren/cs458/")
    url2 = driver.current_url
    time.sleep(1)

    assert url1 == url2

    # test 2.2 after logout go back page

    logout = driver.find_element(By.XPATH, "//*[@id='emptyPage']/button")
    logout.click()
    time.sleep(1)
    url1 = driver.current_url
    driver.back()
    time.sleep(1)
    url2 = driver.current_url
    assert url1 == url2


test2()
test3()
