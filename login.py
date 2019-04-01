from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


def login(driver):
    driver.get("https://m.facebook.com/")
    try:
        elem = driver.find_element_by_xpath('//*[@id="m_login_email"]')
        usr = input('Insira o email: ')
        elem.send_keys(usr)
        elem = driver.find_element_by_xpath('//*[@id="m_login_password"]')
        pwd = input('Insira a senha: ')
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
    except NoSuchElementException:
        pass