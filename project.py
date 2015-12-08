import openpyxl
wb = openpyxl.load_workbook('work.xlsx')
ws = wb['Sheet1']
def find_data(rows):
    """Find all data in rows of excel"""
    dic = {'central':[], 'eastern':[], 'nort_east':[], 'northern':[], 'western':[], 'southern':[]}
    for w,x,y in [('central',2,11),('eastern',12, 20),('nort_east', 21, 41),('northern', 42, 60),('western', 61, 69), ('southern', 70, 84)]:
        for i in ws.rows[rows][x:y]:
            dic[w].append(i.value)
    return dic

thai = find_data(0)
type_1 = find_data(1)
type_2 = find_data(2)
type_3 = find_data(3)
type_7 = find_data(7)
type_8 = find_data(8)
type_9 = find_data(9)
type_10 = find_data(10)
type_11 = find_data(11)
type_12 = find_data(12)
type_13 = find_data(13)
type_14 = find_data(14)
type_15 = find_data(15)
type_16 = find_data(16)
type_17 = find_data(17)
type_18 = find_data(18)
type_19 = find_data(19)
type_20 = find_data(20)

##central = find_data(0)
##eastern = [i.value for i in ws.rows[0][12:20]]
##nort_east = [i.value for i in ws.rows[0][21:41]]
##northern = [i.value for i in ws.rows[0][42:60]]
##western = [i.value for i in ws.rows[0][61:69]]
##southern = [i.value for i in ws.rows[0][70:84]]
##thai = central + eastern + nort_east + northern + western + southern
##type_drive = [i.value.lstrip(' ').rstrip(' ') for i in ws.columns[0][1:21]]
##for i in ws.rows[0][:84]:
##
