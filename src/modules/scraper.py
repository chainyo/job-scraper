import time

from selenium import webdriver

from src.modules.offer import Offer


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
        Function to access the page.
        
        Parameters
        ----------
        url: str
            Url of the page to access.
        """
        self.driver.get(url)

    def save_offers(self):
        """
        Function to save offers and append them to the list of all offers.
        """
        offers = self.driver.find_elements_by_xpath('//*[@id="mosaic-provider-jobcards"]/a')
        for ele in offers:
            job_id = ele.get_attribute('id').split('_')[-1]
            offer = Offer(job_id)
            if offer not in self.offers:
                self.offers.append(offer)
    
    def get_offers_infos(self):
        for offer in self.offers:
            infos = {}
            time.sleep(0.2)
            while True:
                try:
                    self.access_page(offer.link)
                    if self.driver.title == 'hCaptcha solve page': continue
                    
                    try: infos['title'] = self.driver.find_element_by_class_name('jobsearch-JobInfoHeader-title').text
                    except: infos['title'] = None
                    try: infos['company'] = self.driver.find_element_by_class_name('jobsearch-InlineCompanyRating').text.split('\n')[0]
                    except: infos['company'] = None
                    
                    print(offer.link)
                    print(infos['title'])
                    print(infos['company'])
                    time.sleep(0.2)
                    break
                except: pass
                
            
    def export_to_txt(self):
        """
        Function to export the offers links to a txt file.
        """
        with open('indeed.txt', 'w') as file:
            for offer in self.offers:
                file.write(offer.link + '\n')


    def scrap(self, iterator:int=0):
        """
        Function to scrap the offers.

        Parameters
        ----------
        iterator: int
            Iterator used to access the page before scraping.
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
            
        self.get_offers_infos()
        self.export_to_txt()
