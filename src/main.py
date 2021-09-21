from selenium import webdriver

from modules.scraper import Indeed

try:
    grid_url = "http://127.0.0.1:4444/wd/hub"
    driver = webdriver.Remote(command_executor=grid_url)

    scraper = Indeed(driver=driver, job="data engineer", location="Lyon")
    scraper.scrap()

    # save screenshot
    driver.save_screenshot("indeed.png")
finally:
    driver.quit()  
