import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xlrd
import os
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
wb = xlrd.open_workbook(r"G:\graduation_database\calcuate\model\result_clcd\西安市.xls")
sheet = wb.sheet_by_index(0)

all_data = []

for i in range(1,10):
    all_data.append(sheet.col_values(i)[1:])
        
dict1 = dict(zip(name_list,all_data))

df = pd.DataFrame(dict1)
sns.boxplot(data=df)
plt.show()
"""

#文件夹
#耕地	林地	灌木	草地	水体	冰雪	裸地	不透水面	湿地
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题
name_list = ["耕地","林地","灌木","草地","水体","冰雪","裸地","不透水面","湿地"]
img_folder = r"G:\graduation_database\calcuate\model\clcd_result_img"

def summery_img(xls_folder,save_folder):

    for filename in os.listdir(xls_folder):
        xls_dir = xls_folder + "\\\\" + filename
        city_name = xls_dir[-7:-4]
        save_dir = save_folder + "\\\\" + city_name + ".png"
        wb = xlrd.open_workbook(xls_dir)
        sheet = wb.sheet_by_index(0)
        #print(sheet)
        years = sheet.col_values(0)[1:]
        #print(years)
        #get all landcover data
        all_data = []

        for i in range(1,10):
            all_data.append(sheet.col_values(i)[1:])

        #create dict
        dict1 = dict(zip(name_list,all_data))
        #print(dict1)
        #create pandas dataframe
        df = pd.DataFrame(dict1,index=years)
        plt.figure(figsize=(8.5,6.2),dpi=300)
        #print(df)
        sns.lineplot(data=df,markers=True)
        plt.title(city_name + "土地利用变化")
        plt.xlabel("年度")
        plt.ylabel("土地占比")
        plt.xticks(rotation=45)
        plt.savefig(save_dir)

def summery_clcd_mean(xls_folder,save_folder):

    for filename in os.listdir(xls_folder):
        xls_dir = xls_folder + "\\\\" + filename
        city_name = xls_dir[-7:-4]
        save_dir = save_folder + "\\\\" + city_name + ".png"
        wb = xlrd.open_workbook(xls_dir)
        sheet = wb.sheet_by_index(0)
        #print(sheet)
        #print(years)
        #get all landcover data
        all_data = []

        for i in range(1,10):
            all_data.append(sheet.col_values(i)[1:])
        
        dict1 = dict(zip(name_list,all_data))

        df = pd.DataFrame(dict1)
        plt.figure(figsize=(6,4),dpi=300)
        sns.boxplot(data=df)
        plt.title(city_name + "土地利用情况")
        plt.xlabel("土地利用类型")
        plt.ylabel("占比")
        #plt.show()
        plt.savefig(save_dir)


#execute line img
#summery_img(r"G:\graduation_database\calcuate\model\result_clcd",img_folder)
#summery_clcd_mean(r"G:\graduation_database\calcuate\model\result_clcd",img_folder)
        