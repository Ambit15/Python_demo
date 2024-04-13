import pandas as pd
import seaborn as sns
import xlrd

#文件夹
#耕地	林地	灌木	草地	水体	冰雪	裸地	不透水面	湿地

xls_dir = r"G:\graduation_database\calcuate\model\result_clcd\安康市.xls"

name_list = ["耕地","林地","灌木","草地","水体","冰雪","裸地","不透水面","湿地"]
wb = xlrd.open_workbook(xls_dir)
sheet = wb.sheet_by_index(0)
#print(sheet)
years = sheet.col_values(0)[1:]
#print(years)
#get all landcover data
all_data = []

"""
corpland = sheet.col_values(1)[1:]
forest = sheet.col_values(2)[1:]
shore = sheet.col_values(3)[1:]
gressland = sheet.col_values(4)[1:]
water = sheet.col_values(5)[1:]
snow = sheet.col_values(6)[1:]
barren = sheet.col_values(7)[1:]
city_land = sheet.col_values(8)[1:]
wetland = sheet.col_values(9)[1:]
"""

for i in range(1,10):
    all_data.append(sheet.col_values(i)[1:])

#create dict
dict1 = dict(zip(name_list,all_data))
#print(dict1)
#create pandas dataframe
df = pd.DataFrame(dict1,index=years)
#print(df)