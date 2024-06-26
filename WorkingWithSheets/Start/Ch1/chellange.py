# LinkedIn Learning Course
# Example file for Python: Working with Excel and Spreadsheet Data by Joe Marini
# Reading CSV file into an dictionary

import csv
from pathlib import Path
from decimal import Decimal


def read_csv_to_dict(filename):
    data = []
    file_path = Path(__file__).with_name(filename)
    with file_path.open("r") as csv_file:
        reader = csv.DictReader(csv_file)
        row = next(reader)
        for row in reader:
            row["Difference"] = round(
                Decimal(row["Consumer Price"]) - Decimal(row["Wholesale Price"]), 2
            )
            data.append(row)
    return data


def write_dict_to_csv(data, file_name):
    first_entry = data[0]
    keys = first_entry.keys()
    file_path = Path(__file__).with_name(file_name)
    with file_path.open("w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


inventory_data = read_csv_to_dict("Inventory.csv")

write_dict_to_csv(inventory_data, "chellange.csv")
