from selenium import webdriver

from modules.scraper import Indeed

try:
    grid_url = "http://127.0.0.1:4444/wd/hub"
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox') 
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')    
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    
    driver = webdriver.Remote(command_executor=grid_url, options=chrome_options)

    scraper = Indeed(driver=driver, job="data engineer", location="Lyon")
    scraper.scrap()
finally:
    driver.quit()  
