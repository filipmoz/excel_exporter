"""Create a small real Excel file from sample data."""
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

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

    # Small bar chart: products vs Qty
    chart = BarChart()
    chart.title = "Qty by Product"
    chart.width = 10
    chart.height = 8
    data = Reference(ws, min_col=2, min_row=1, max_row=4, max_col=2)
    cats = Reference(ws, min_col=1, min_row=2, max_row=4)
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(cats)
    ws.add_chart(chart, "E2")

    wb.save("sample.xlsx")
    print("Created sample.xlsx")


if __name__ == "__main__":
    main()
