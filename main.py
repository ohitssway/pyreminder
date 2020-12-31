from pyreminder import create_reminders
from json import load
from constants import DAYS
import datetime
import os

current_date = datetime.date.strftime(datetime.datetime.now(), "%m/%d/%Y")
_, _, current_day = datetime.date.today().isocalendar()
current_day = DAYS[current_day - 1]

filename = os.path.abspath("reminders.json") 
with open(filename, 'r') as f:
    reminders = load(f)
print(reminders)
create_reminders(reminders['tasks'], current_day)
