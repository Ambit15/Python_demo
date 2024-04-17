import os
import rasterio
import numpy as np
import xlwt
import gdal_clip as gc

#def get_data(list):


def summery_clcd(folder,xlsname,save_dir):
    #excle存放路径和名称 save_dir
    #create workspace
    workbook = xlwt.Workbook(encoding="utf-8")
    #create sheet
    sheet = workbook.add_sheet(xlsname,cell_overwrite_ok=True)

    head = ["年度","1","2","3","4","5","6","7","8","9"]
    years = []
    start_x = 1
    for filename in os.listdir(folder):
        sum_list = []
        year = gc.check_year(gc.keep_digits(filename))
        years.append(year)
        filedir = folder + "\\\\" + filename
        with rasterio.open(filedir) as raster:
            raster_data = raster.read()

            band_index = 0  # 根据实际情况修改
            #降维
            band_data = raster_data[band_index].reshape(-1)
            len_raster = len(band_data)

            #band_data = np.fromiter(band_data,"uint8",count = -1)
            ID_list = [1,2,3,4,5,6,7,8,9]
            #数组计数
            #counts = np.bincount(band_data)
            for i in ID_list:
                count = round(np.sum(band_data == i) / len_raster,6)
                sum_list.append(count)
            print(sum_list)
            start_y = 1
            for i in sum_list:
                sheet.write(start_x,start_y,float(i))
                start_y = start_y + 1
            start_x = start_x + 1
            #print(sum_list)
    
    for i in head:
        sheet.write(0,head.index(i),i)

    for i in years:
        sheet.write(years.index(i)+1,0,i)
    
    workbook.save(save_dir)

#函数测试成功
#summery_clcd(r"G:\graduation_database\Analysis_temp\temp_clcd","test",r"G:\graduation_database\Analysis_temp\xls\test.xls")
"""
with rasterio.open(r"G:\graduation_database\Analysis_temp\temp_clcd\011990_clip.tif") as raster:
    raster_data = raster.read()

    band_index = 0  # 根据实际情况修改
    band_data = raster_data[band_index].reshape(-1)
    len_raster = len(band_data)

    #降维
    #band_data = np.fromiter(band_data,"uint8",count = -1)
    ID_list = [1,2,3,4,5,6,7,8,9]
    sum_list = []
    #数组计数
    #counts = np.bincount(band_data)
    for i in ID_list:
        count = np.sum(band_data == i)
    print(sum_list)
"""

def year_clcd():
    return 1