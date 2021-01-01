from constants import DAYS, DAYS_MAP
import os
import datetime
import random

def get_current_date():
    return datetime.date.strftime(datetime.datetime.now(), "%m/%d/%Y")

def get_current_day():
    _, _, current_day = datetime.date.today().isocalendar()
    return DAYS[current_day - 1]
    

def get_random_time(time_range):
    start, end = time_range
    sh, sm = start.split(":")
    eh, em = end.split(":")
    rh = random.randint(int(sh), int(eh))
    if (rh == sh) and (rh == eh):
        return "{:02d}:{:02d}".format(rh, random.randint(int(sm),int(em)))
    elif rh == sh:
        return "{:02d}:{:02d}".format(rh, random.randint(int(sm),59))
    elif rh == eh:
        return "{:02d}:{:02d}".format(rh, random.randint(0, int(em)))
    else:
        return "{:02d}:{:02d}".format(rh, random.randint(0, 59))

def convert_time(task_time):
    return datetime.datetime.strptime(task_time, "%H:%M").strftime("%I:%M%p")

def create_reminder(task, task_date): 
    task_time = convert_time(get_random_time(task['time']))

    remind_path = os.path.abspath("create_remind") 
    full_remind_path = remind_path + " '{}' {} {}"
    rmd_cmd = full_remind_path.format(task["name"], task_date, task_time)
    os.system(rmd_cmd)

def create_reminders(tasks):
    current_date = get_current_date()
    current_day = get_current_day()
    for task in tasks:
        if "days" in task and current_day in DAYS_MAP[task["days"]]:
            create_reminder(task, current_date)
        if "date" in task:
            create_reminder(task, task["date"])

