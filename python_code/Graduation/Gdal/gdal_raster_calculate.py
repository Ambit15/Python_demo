import rasterio
import os
import numpy as np

def calculate_mean(raster_folder,result_dir):
    """
    raster_folder
    result_dir with .tif
    """
    #计数
    len_number = 0
    list_raster_array = []
    #循环导入栅格数据
    for filename in os.listdir(raster_folder):
        raster_dir = raster_folder + "\\\\" + filename
        #计数加一
        len_number += 1
        with rasterio.open(raster_dir) as raster:
            data = raster.read()
            profile = raster.profile
            profile.update(count=raster.count)
        list_raster_array.append(data)

    result_array = sum(list_raster_array)
    result_array = result_array / len_number

    #写入栅格

    with rasterio.open(result_dir,"w",**profile) as result_raster:
        result_raster.write(result_array)

calculate_mean(r"G:\graduation_database\Analysis_temp\night",r"G:\graduation_database\Analysis_temp\tongchuan.tif")