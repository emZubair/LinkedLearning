# LinkedIn Learning Course
# Example file for Python: Working with Excel and Spreadsheet Data by Joe Marini
# Reading CSV file into an dictionary

import csv
from pathlib import Path
from pprint import pprint


def read_csv_to_dict(filename):
    file_path = Path(__file__).with_name(filename)
    data = {}
    with file_path.open("r") as csv_file:
        reader = csv.DictReader(csv_file)
        row = next(reader)
        for row in reader:
            data[row[reader.fieldnames[0]]] = row
    return data


inventory_data = read_csv_to_dict("Inventory.csv")

pprint(inventory_data)
pprint(inventory_data["Pineapple"])
pprint(inventory_data["Pineapple"]["Consumer Price"])
