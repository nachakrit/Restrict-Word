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
###########################################################################################
####################โค้ทที่ดึงไฟล์Excelมาใช้####################################################
###########################################################################################
from openpyxl import *
wb = load_workbook('work.xlsx')
ws = wb['Sheet1']
lis = []
lis_type = []
dic = {}
for i in range(1, 85):##ส่วนนี้ใช้หาชื่อจังหวัดจากexcel
    if ws.rows[0][i].value not in ['Central', 'Western']:
        lis.append(ws.rows[1][i].value)
    else:
        print(ws.rows[1][i].value)
for i in range(1, 20):###ส่วนนี้หาจำนวนคนแยกตามใบขับขี่ + listของชนิดใบขับขี่แบบเรียงลำดับ
    lis_type.append(ws.rows[i][0].value)
    for j in range(85):
        if j== 0:
            print(i)
            dic.setdefault(ws.rows[i][0].value)
            dic[ws.rows[i][0].value] = []
            print(ws.rows[i][0].value)
        else:
            dic[ws.rows[i][0].value].append(ws.rows[i][j].value)
print(dic)#dictแบ่งตามลักษณะใบขับขี่(keys)จำนวนคนเป็นlist
print(lis)#listชื่อของจังหวัด
