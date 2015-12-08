import openpyxl
wb = openpyxl.load_workbook('work.xlsx')
ws = wb['Sheet1']
central = [i.value for i in ws.rows[0][1:10]]
eastern = [i.value for i in ws.rows[0][11:19]]
nort_east = [i.value for i in ws.rows[0][20:40]]
northern = [i.value for i in ws.rows[0][41:59]]
western = [i.value for i in ws.rows[0][60:68]]
southern = [i.value for i in ws.rows[0][69:83]]
thai = central + eastern + nort_east + northern + western + southern
type_drive = [i.value.lstrip(' ').rstrip(' ') for i in ws.columns[0][1:21]]
#for i in ws.rows[0][:84]:
