# LinkedIn Learning Course
# Example file for Python: Working with Excel and Spreadsheet Data by Joe Marini
# Writing CSV file from an array

import csv
from pathlib import Path

# define the column names that will be the header row


# declare the sample data
data = [
    {
        "Item Name": "Apple",
        "Category": "Fruits",
        "Quantity": 100,
        "Wholesale Price": 0.50,
        "Consumer Price": 0.75,
    },
    {
        "Item Name": "Banana",
        "Category": "Fruits",
        "Quantity": 150,
        "Wholesale Price": 0.35,
        "Consumer Price": 0.50,
    },
    {
        "Item Name": "Orange",
        "Category": "Fruits",
        "Quantity": 120,
        "Wholesale Price": 0.45,
        "Consumer Price": 0.65,
    },
    {
        "Item Name": "Grapes",
        "Category": "Fruits",
        "Quantity": 80,
        "Wholesale Price": 0.60,
        "Consumer Price": 0.85,
    },
    {
        "Item Name": "Strawberries",
        "Category": "Fruits",
        "Quantity": 90,
        "Wholesale Price": 1.20,
        "Consumer Price": 1.50,
    },
]


# function to write the data
def write_dict_to_csv(data, file_name):
    first_entry = data[0]
    keys = first_entry.keys()
    file_path = Path(__file__).with_name(file_name)
    with file_path.open("w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


# write the data to the file
write_dict_to_csv(data, "dict.csv")
