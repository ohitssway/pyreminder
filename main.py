from constants import DAYS
from reminders_io import open_json
from pyreminder import create_reminders
import datetime
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--file", help="Choose reminders json file", required=True)
args = parser.parse_args()

create_reminders(open_json(args.file)['tasks'])
