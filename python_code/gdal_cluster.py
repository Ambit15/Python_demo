from osgeo import gdal as gd
import os
import rasterio
import numpy as np

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
folder = "G:\\\\graduation_database\\\\N_clip"

for filename in os.listdir(folder):
    filedir = folder + "\\\\" + filename
    with rasterio.open(filedir) as raster:
    # 读取栅格数据
        raster_data = raster.read()
    band_index = 0  # 根据实际情况修改
    band_data = raster_data[band_index]
    mean_value = np.mean(band_data)
    print(f"平均值: {mean_value}")

