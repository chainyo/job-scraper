from selenium import webdriver

from src.modules.scraper import Scraper

try:
    grid_url = "http://127.0.0.1:4444/wd/hub"
    driver = webdriver.Remote(command_executor=grid_url)

    scraper = Scraper(url="http://fr.indeed.com", driver=driver, job="intelligence artificielle", location="Lyon")
    scraper.scrap()

    # save screenshot
    driver.save_screenshot("indeed.png")
finally:
    driver.quit()  
