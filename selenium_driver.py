from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def driver_config():
    chrome_options = Options()
    # chrome_options.add_argument(r"user-data-dir=C:\Users\USER\AppData\Local\Google\Chrome\User Data\Profile 1")
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('disable-infobars')

    driver = webdriver.Chrome(options=chrome_options)

    return driver
