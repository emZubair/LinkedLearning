# LinkedIn Learning Course
# Example file for Python: Working with Excel and Spreadsheet Data by Joe Marini
# Writing CSV file from an array

import csv
from pathlib import Path

# Sample data
data = [
    ["Item Name", "Category", "Quantity", "Wholesale Price", "Consumer Price"],
    ["Apple", "Fruits", 100, 0.50, 0.75],
    ["Banana", "Fruits", 150, 0.35, 0.50],
    ["Orange", "Fruits", 120, 0.45, 0.65],
    ["Grapes", "Fruits", 80, 0.60, 0.85],
    ["Strawberries", "Fruits", 90, 1.20, 1.50],
]


def write_data_csv(data, file_name):
    file_path = Path(__file__).with_name(file_name)
    with file_path.open("w", newline="") as csv_file:
        write = csv.writer(csv_file)
        write.writerows(data)


write_data_csv(data, "first_attempt.csv")
write_data_csv(data, "last_attempt.csv")
