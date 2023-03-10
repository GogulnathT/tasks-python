# from sqlite3 import Row
# import openpyxl as oxl
# from pyparsing import col

# path = r'C:\Users\7000031725\Desktop\fileio\test-excel.xlsx'

# wb = oxl.load_workbook(path)

# sheet = wb.active
# cell_obj = sheet.cell(row=1, column=2)

# print(cell_obj.value)

# max_row = sheet.max_row
# max_column = sheet.max_column

# print(max_column)
# print(max_row)
# # trying to print multiple rows
# for i in range(1, max_row + 1):
#     for j in range(1, max_column + 1):
#         cell_obj = sheet.cell(row=i, column=j)
#         print(cell_obj.value, end='')
#     print()

from turtle import shape
import pandas as pd

path = r'C:\Users\7000031725\Desktop\fileio\test-excel.xlsx'

df1 = pd.read_excel(path)
df2 = pd.read_excel(path, sheet_name='Sheet2')

print(df1)
print('--------------------------------------')
print(df2)
print('--------------------------------------')

book = pd.concat([df1, df2])

print(book)
print('--------------------------------------')

print(book.head())
print('--------------------------------------')

print(book.tail())
print('--------------------------------------')
