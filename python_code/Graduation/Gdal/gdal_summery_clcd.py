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

    head = ["年度","0","1","2","3","4","5","6","7","8","9"]
    years = []

"""

"""
with rasterio.open(r"G:\graduation_database\Analysis_temp\temp_clcd\011990_clip.tif") as raster:
    raster_data = raster.read()

    band_index = 0  # 根据实际情况修改
    band_data = raster_data[band_index].reshape(-1)

    #降维
    #band_data = np.fromiter(band_data,"uint8",count = -1)
    ID_list = [1,2,3,4,5,6,7,8,9]
    sum_list = []
    #数组计数
    #counts = np.bincount(band_data)
    for i in ID_list:
        count = np.sum(band_data == i)
    print(sum_list)