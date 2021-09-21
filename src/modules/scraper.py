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
        offers = self.driver.find_elements_by_xpath('//*[@id="mosaic-provider-jobcards"]/a')
        for e in offers:
            job_id = e.get_attribute('id').split('_')[-1]
            offer = Offer(f'https://fr.indeed.com/voir-emploi?jk={job_id}')
            if offer not in self.offers:
                self.offers.append(offer)
    
    def export_to_txt(self):
        """
        """
        with open('indeed.txt', 'w') as file:
            for offer in self.offers:
                file.write(offer.link + '\n')


    def scrap(self, iterator:int = 0):
        """
        """

        while True:
            self.access_page(f'https://fr.indeed.com/emplois?q={self.job}&l={self.location}&start={iterator}')
            try: 
                self.driver.find_element_by_xpath('//*[@id="mosaic-provider-jobcards"]/a')
                length = len(self.offers)
                self.save_offers()
                if length == len(self.offers):
                    break
                iterator += 10
            except: pass
        self.export_to_txt()
