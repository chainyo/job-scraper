class Offer:

    def __init__(self, link:str):
        self.link = link

    def __eq__(self, other):
        """
        """
        return self.link == other.link

    def store_infos(
        self, 
        job_title:str, 
        company:str, 
        location:str, 
        job_metadata:str, 
        job_description:str,
        job_profile:str,
        skills:str):
        """
        """
        self.job_title = job_title # "/html/body/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[1]/h1".text
        self.company = company # "/html/body/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div".text
        self.location = location # "/html/body/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]".text
        self.job_metadata = job_metadata # "/html/body/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[2]/span".text
        self.job_description = job_description # "/html/body/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[3]/div/div[1]".text
        self.job_profile = job_profile # "/html/body/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[3]/div/div[2]/div" multiple li and text
        self.skills = skills # "/html/body/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[3]/div/div[5]/div[1]/div" multiple text in div

    def apply(self):
        """
        """
        pass