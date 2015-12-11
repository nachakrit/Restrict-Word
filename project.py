"""
This is 'The Number of Driving Licences and Transport Personnel Licences Classified by Type' program
which made by 'Restrict Word' for Problem Solving in Information Technology python project.

This program will return you the output by this following function :

find_data(num) this will return all number of num driver lincence type in dictionary.
data_to_percent(type_num) this will return all percentage of num driver lincence type in dictionary.
sum_region(type_num) this will return percentage of num driver licence type in each region in dictionary.

Note : 1.num is number for type of driver licence in work.xlsx which mean num is only available for 1-3 and 7-20,
         Otherwise it will return 0 in all number of information or this program may error.
       2.DO NOT use data_to_percent(type_num) before you use sum_region(type_num), You may recive incorrect information.
"""
import openpyxl
import plotly.plotly as py
import plotly.graph_objs as go
wb = openpyxl.load_workbook('work.xlsx')
ws = wb['Sheet1']
def find_data(rows):
    """Find all data in rows of excel"""
    dic = {'Central':[], 'Eastern':[], 'NorthEastern':[], 'Northern':[], 'Western':[], 'Southern':[]}
    for w,x,y in [('Central',2,11),('Eastern',12, 20),('NorthEastern', 21, 41),('Northern', 42, 59),('Western', 53, 68), ('Southern', 64, 83)]:
        for i in ws.rows[rows][x:y]:
            dic[w].append(i.value)
    return dic

def data_to_percent(dic):
    """Change dictionary of data to percent for drawing graph"""
    dic_data = dict(dic)
    for i in dic_data:
        sum_province = sum(dic_data[i])
        for j in range(len(dic_data[i])):
            dic_data[i][j] = float('%.2f' % ((dic_data[i][j]/sum_province*100)))
    return dic_data

def sum_region(dic):
    """Return percent of sum region"""
    dic_data = dict(dic)
    for i in dic_data.keys():
        dic_data[i] = sum(dic_data[i])
    sum_thai = sum([dic_data[i] for i in dic_data.keys()])
    for i in dic_data.keys():
        dic_data[i] = float('%.2f' % ((dic_data[i]/sum_thai)*100))
    return dic_data

def plot_regieon(num_type):
    """plot a regieon that have top percent of all regieon
    Example input = 1 this graph will plot a regieon in type_1 that have max percent"""
    title = ['Type 1 : Private  Automobile (Temporary)', 'Type 2 : Private  Motor  Tricycle (Temporary)', 'Type 3 : Motorcycle (Temporary)','', '', '', 'Type 7 : Private  Automobile (Five Years)  ',\
             'Type 8 : Private  Motor  Tricycle (Five Years)', 'Type 9 : Motorcycle (Five Years)', 'Type 10 : Private  Automobile (Life)', 'Type 11 : Motor  Tricycle (Life)',\
             'Type 12 : Motorcycle (Life)', 'Type 13 : Public  Automobile', 'Type 14 : Public  Motor  Tricycle', 'Type 15 : Public  Motorcycle', 'Type 16 : International  Driving  Licence',\
             'Type 17 : Tractor', 'Type 18 : Tractor Driving Licence', 'Type 19 : Farm Vehicle Driving Licence', 'Type 20 : Others Driving Licence']
    py.sign_in('ommohmjr', 'nbzbfcsu6o')
    dic = find_data(num_type)
    max_per = max(sum_region(dic).values())
    for i in dic.keys():
        if dic[i] == max_per:
            max_regieon = i
    fig = {
    'data': [{'labels': [i for i in thai[i]],
              'values': [j for j in data_to_percent(dic)[i]],
              'type': 'pie'}],
    'layout': {'title': title[num_type - 1]}
    }

    url = py.plot(fig, filename=title[num_type - 1].split()[1])

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
