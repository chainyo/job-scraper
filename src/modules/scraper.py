from selenium import webdriver

from modules.offer import Offer


class Indeed:

    def __init__(self, job:str, location:str, driver:webdriver):
        """
        """
        self.location = location
        self.job = job
        self.driver = driver
        self.offers = []

    def access_page(self, url:str):
        """
        """
        self.driver.get(url)

    def save_offers(self):
        """
        """
        offers = self.driver.find_elements_by_class_name('resultWithShelf')
        for e in offers:
            offer = Offer(e.get_attribute('href'))
            print(offer.link)
            if offer not in self.offers:
                self.offers.append(offer)
    
    def scrap(self):
        """
        """
        i = 0
        while True:
            self.url = f'https://fr.indeed.com/emplois?q={self.job}&l={self.location}&start={i}'
            self.access_page(self.url)
            self.save_offers()
            i += 10
            print(len(self.offers))
            