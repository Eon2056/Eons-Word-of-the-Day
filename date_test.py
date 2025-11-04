
# from datetime import dat
from src.wotdDate import wotdDate as date
from time import time
from math import ceil
import json

filename = "testdate.json"


dayUnix = 86400 
# lastdate = 1759427400
# lastdate = 1761277520
lastdate = 1761281120
lastDay = "24"
# today = time()
today = date()
# print(f"today.day = {today.day}")
# print(f"lastDay = {lastDay}")
# print(type(today.day))
# print(f"today.day == lastDay : {today.day == lastDay}")
if today.day != lastDay:
    daydiff = ceil((today.unix-lastdate)/dayUnix)
else:
    daydiff = 0
print(f"{daydiff} days since last")
# print(today)
# print(type(today))

# with open(filename, 'w') as file:
#     json.dump({"date":str(today)}, file)

# class date:
#         def __init__(self, datestr):
#             self.year,self.month,self.day = datestr.split("-")

#         def __str__(self):
#             return f"| year: {self.year} | month: {self.month} | day: {self.day} | "

# todayDate = date(str(today))
# print(todayDate)
# print(todayDate.month)

with open(filename, 'r') as file:
    a = json.load(file)
    

print(a['date'])