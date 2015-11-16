from openpyxl import *##ทดสอบการดึงไฟล์จากexcel
wb = load_workbook('work.xlsx')##ไฟล์excelต้องอยู่ในโฟลเดอร์เดียวกับpython
ws = wb['Sheet1']## กรณีใช้interactive modeไฟล์อยู่ใน Python34\Lib\idlelib
lis = []
for i in range(1, 85):
    if ws.rows[1][i].value not in ['Central', 'Western']:
        lis.append(ws.rows[1][i].value)
    else:
        print(ws.rows[1][i].value)
print(lis)
