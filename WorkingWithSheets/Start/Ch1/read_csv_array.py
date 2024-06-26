# LinkedIn Learning Course
# Example file for Python: Working with Excel and Spreadsheet Data by Joe Marini.
# Reading CSV file into an array

# import the csv module from the standard library
import csv
from pathlib import Path


def read_csv_to_array(filename):
    p = Path(__file__).with_name(filename)
    data = []
    with p.open("r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            data.append(row)
        return data


# Read the data into an array of arrays
inventory_data = read_csv_to_array("Inventory.csv")

# Each row in the array is itself an array of values
print(f"Read rows: {len(inventory_data)}")
print(inventory_data[0])
print(inventory_data[1])
print(f"Break down of \n{inventory_data[3]}")
print(f"Name:{inventory_data[3][0]}, Quantity:{inventory_data[3][2]}")
