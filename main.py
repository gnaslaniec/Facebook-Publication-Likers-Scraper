from selenium_driver import driver_config
from scraper import scraper_likers
from login import login


def main():
    driver = driver_config()
    login(driver)
    scraper_likers(driver)
    print('\nFim!')
    driver.quit()


if __name__ == '__main__':
    main()
