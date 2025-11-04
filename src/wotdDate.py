from time import time
from datetime import date

class wotdDate:
        def __init__(self):
            self.unix = time()
            self.year,self.month,self.day = str(date.today()).split("-")

        def __str__(self):
            return f"| year: {self.year} | month: {self.month} | day: {self.day} | unix:{self.unix}"
