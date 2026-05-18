import openpyxl
wb = openpyxl.load_workbook(r'd:\Masho&Gio\Mosacvevebi.xlsx')
ws = wb.active
for i, row in enumerate(ws.iter_rows(min_row=1, values_only=True), start=1):
    print(f'Row {i}: {row}')