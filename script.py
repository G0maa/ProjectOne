# A small script to file that takes the registered subjects
# and puts them in the .xlsx spreasheet template.
# P.S: YOU NEED TO INSTALL openpyxl module for it to work!
# enter this in your terminal: pip install openpyxl
import csv
from openpyxl import Workbook
from openpyxl import load_workbook

with open("output.csv") as output:
    wb = load_workbook(filename = 'table.xlsx')
    ws = wb.active
    ws.title = "table"

    output = csv.reader(output, delimiter=',')
    for row in output:
        days = int(row[4])
        period_start = int(row[5][0])
        period_end = int(row[5][2])
        for i in range(period_start, period_end + 1):
            ws[f"{chr(i + 65)}{days + 2}"] = row[0] + row[1] + row[2] + row[3]

    wb.save('test.xlsx')
