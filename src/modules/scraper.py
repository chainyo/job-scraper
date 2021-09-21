import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from modules.offer import Offer


class Indeed:

    def __init__(self, job:str, location:str, driver:webdriver):
        """
        """
        self.location = location
        self.job = job
        self.driver = driver
        self.offers = []

    def get_page(self, url:str):
        """
        """
        self.driver.get(url)

    def save_offers(self):
        """
        """
        offers = self.driver.find_elements_by_class_name('resultWithShelf')
        print(offers)
        for e in offers:
            offer = Offer(e.get_attribute('href'))
            print(offer.link)
            if offer not in self.offers:
                self.offers.append(offer)
                return True
            else: return False
    
    def scrap(self):
        """
        """
        i = 0
        while True:
            self.driver.save_screenshot("indeed1.png")
            self.url = f'https://fr.indeed.com/emplois?q={self.job}&l={self.location}&start={i}'
            time.sleep(5)
            self.driver.save_screenshot("indeed2.png")
            print(self.url)
            self.save_offers()
            i += 10
            print(len(self.offers))
            