import os
import rasterio
import numpy as np
import xlwt
import gdal_clip as gc
'''
# 打开栅格文件
with rasterio.open('path_to_your_raster.tif') as raster:
    # 读取栅格数据
    raster_data = raster.read()
 
# 选择一个波段进行统计，如果是多波段则选择波段索引，例如band_index = 1
band_index = 1  # 根据实际情况修改
band_data = raster_data[band_index]
 
# 计算最大值、最小值和平均值
max_value = np.max(band_data)
min_value = np.min(band_data)
mean_value = np.mean(band_data)
 
print(f"最大值: {max_value}")
print(f"最小值: {min_value}")
print(f"平均值: {mean_value}")

'''


#遍历文件

def summery_mean(folder,xlsname):

    #excle存放路径和名称
    excel_save_dir = "G:\\\\graduation_database\\\\Analysis_temp\\\\xls\\\\" + xlsname + ".xls"
    #create workspace
    workbook = xlwt.Workbook(encoding="utf-8")
    #create sheet
    sheet = workbook.add_sheet(xlsname,cell_overwrite_ok=True)
    head = ["年度","均值"]
    years = []
    data = []

    #循环获取数据
    for filename in os.listdir(folder):
        year = gc.keep_digits(filename)
        filedir = folder + "\\\\" + filename
        with rasterio.open(filedir) as raster:
        # 读取栅格数据
            raster_data = raster.read()
        band_index = 0  # 根据实际情况修改
        band_data = raster_data[band_index]
        mean_value = np.mean(band_data)
        data.append(mean_value)
        years.append(year)

    #循环写入数据
    for i in head:
        sheet.write(0,head.index(i),i)

    for i in years:
        sheet.write(years.index(i)+1,0,i)

    for i in data:
        sheet.write(data.index(i)+1,1,i)

    #保存
    workbook.save(excel_save_dir)

#集成化