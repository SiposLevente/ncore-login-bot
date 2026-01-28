import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def initDriver(headLess):
    driver = None

    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    if headLess:
        chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    return driver


def login(username, password, driver: webdriver.Chrome):
    driver.get('https://ncore.pro/login.php')
    element = driver.find_element(by=By.XPATH, value="//*[@id=\"nev\"]")
    element.send_keys(username)
    element = driver.find_element(
        by=By.XPATH, value="//*[@id=\"loginform\"]/table/tbody/tr[2]/td[2]/input")
    element.send_keys(password)
    element.send_keys(Keys.RETURN)


driver = initDriver(headLess=True)
sleep(5)
login("username", "password", driver)
sleep(5)
print("Done...!")
