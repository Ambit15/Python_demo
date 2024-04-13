import re
import numpy as np

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