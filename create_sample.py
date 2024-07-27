"""Create a small real Excel file from sample data."""
from openpyxl import Workbook

# Real input: a few rows (product, qty, price)
SAMPLE_ROWS = [
    ["Product", "Qty", "Price"],
    ["Coffee", 2, 3.50],
    ["Tea", 1, 2.00],
    ["Milk", 3, 1.20],
]


def main():
    wb = Workbook()
    ws = wb.active
    ws.title = "Sales"
    for row in SAMPLE_ROWS:
        ws.append(row)
    wb.save("sample.xlsx")
    print("Created sample.xlsx")


if __name__ == "__main__":
    main()
