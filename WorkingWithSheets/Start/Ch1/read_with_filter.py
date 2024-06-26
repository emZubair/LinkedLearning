# LinkedIn Learning Course
# Example file for Python: Working with Excel and Spreadsheet Data by Joe Marini
# Reading CSV file into an array with a filter function

import csv
import pprint
from pathlib import Path


def filter_by_category(row, category):
    return row[1] == category


def read_csv_filter_rows(filename, filter_to_apply):
    p = Path(__file__).with_name(filename)
    data = []
    with p.open("r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if filter_to_apply(row):
                data.append(row)
        return data


# Filter function (replace with your specific filtering criteria)


def apply_filter_for(category_name):
    filtered_rows = read_csv_filter_rows(
        "Inventory.csv", lambda row: filter_by_category(row, category_name)
    )
    print(f"\n\nResults filtered by: {category_name}\n")
    pprint.pprint(filtered_rows)


apply_filter_for("Fruits")
apply_filter_for("Vegetables")
