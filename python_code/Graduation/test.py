import re
import os
import numpy as np
import xlrd
import xlwt

"""
def keep_digits(string):
    return re.sub("\D", "", string)

def check_year(str):
    length = len(str)
    if length > 4:
        str = str[2:]
    return str

a = "aa011990"

print(check_year(keep_digits(a)))

 
# 示例数组
arr = np.array([1, 2, 2, 3, 1, 1, 3, 4, 4, 4])
 
# 使用bincount统计每个元素的出现次数
counts = np.bincount(arr)
 
print(counts)

for i in range(5):
    print(i)

xls_dir = r"G:\graduation_database\calcuate\model\result_clcd\安康市.xls"
city_name = xls_dir[-7:-4]
print(city_name)

sum_folder = r"G:\graduation_database\calcuate\model\city_sum"
mean_folder = r"G:\graduation_database\calcuate\model\city_mean"
return_folder = r"G:\graduation_database\calcuate\model\clcd_result_img"

for filename in os.listdir(sum_folder):
    xls_sum_dir = sum_folder + "\\\\" + filename
    xls_mean_dir = mean_folder + "\\\\" + filename
    xls_dir =  return_folder + "\\\\" +filename

    wb_sum = xlrd.open_workbook(xls_sum_dir)
    sheet_sum = wb_sum.sheet_by_index(0)
    list_sum = sheet_sum.col_values(1)[17:]
    #print(list_sum)

    wb_mean = xlrd.open_workbook(xls_mean_dir)
    sheet_mean = wb_mean.sheet_by_index(0)
    list_mean = sheet_mean.col_values(2)[17:-1]
    #print(list_mean)
    
    #print(filename[0:3])
    workbook = xlwt.Workbook(encoding="utf-8")
    #create sheet
    sheet = workbook.add_sheet(filename[0:3],cell_overwrite_ok=True)
    
    for i in list_mean:
        sheet.write(list_mean.index(i),0,i)

    for i in list_sum:
        sheet.write(list_sum.index(i),1,i)

    workbook.save(xls_dir)

"""

"""
numpy运算
import numpy as np
 
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [10, 11, 12]])

list1 = []
list1.append(A)
list1.append(B)

C = sum(list1) / 2
print(C)

"""

