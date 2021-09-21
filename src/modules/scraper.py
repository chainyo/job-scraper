from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

from src.modules.offer import Offer

class Scraper:

    def __init__(self, url:str, job:str, location:str, driver:webdriver):
        """
        """
        self.url = url
        self.location = location
        self.job = job
        self.driver = driver
        self.offers = []

    def get_page(self):
        """
        """
        self.driver.get(self.url)

    def launch_search(self):
        """
        """
        self.driver.find_element_by_id("text-input-what").send_keys("intelligence artificielle")
        where_input = self.driver.find_element_by_id("text-input-where")
        where_input.send_keys(Keys.CONTROL + "a")
        where_input.send_keys(Keys.DELETE)
        where_input.send_keys("Lyon")

        self.driver.find_element_by_id("text-input-what").submit()

    def save_offers(self):
        """
        """
        offers = self.driver.find_elements_by_xpath('//*[@id="mosaic-provider-jobcards"]/a')
        for e in offers:
            offer = Offer(e.get_attribute('href'))
            if offer not in self.offers:
                self.offers.append(offer)
            else: return False
    
    def scrap(self):
        """
        """
        self.get_page()
        self.launch_search()
        i = 0
        while True:
            self.save_offers()
            i += 10
            url = self.driver.current_url.split('start=')[0] + str(i)
            self.driver.get(url)
            print(len(self.offers))