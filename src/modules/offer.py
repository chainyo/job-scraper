class Offer:

    def __init__(self, link:str):
        self.link = link

    def __eq__(self, other):
        """
        """
        return self.link == other.link

    def store_infos(
        self, 
        title:str, 
        company:str, 
        location:str, 
        metadata:str, 
        description:str,
        profile:str,
        skills:str):
        """
        Function to store each offer's infos.

        Parameters
        ----------
        title: str
            Job title.
        company: str
            Job company name.
        location: str
            Job location.
        metadata: str
            Job metadata.
        description: str
            Job description.
        profile: str
            Job profile.
        skills: str
            Job skills.
        """
        self.job_title = title # "/html/body/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[1]/h1".text
        self.company = company # "/html/body/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div".text
        self.location = location # "/html/body/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]".text
        self.job_metadata = metadata # "/html/body/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[2]/span".text
        self.job_description = description # "/html/body/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[3]/div/div[1]".text
        self.job_profile = profile # "/html/body/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[3]/div/div[2]/div" multiple li and text
        self.skills = skills # "/html/body/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[3]/div/div[5]/div[1]/div" multiple text in div

    def apply(self):
        """
        """
        pass