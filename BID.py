class BID:
    def __init__(self,name,year_started,year_completed,floor,LEED):
        self.name=name
        self.year_started=year_started
        self.year_completed=year_completed
        self.floor=floor
        self.LEED=LEED
    def LEED_rating(self):
        if self.LEED>80:
            return True
        else: 
            return False
   

        
        