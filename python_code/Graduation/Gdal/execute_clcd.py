import os
import time
import gdal_clip
import gdal_select as gs
import gdal_summery_clcd as gsc
from osgeo import ogr

start_time = time.time()
#可选参数 #####
city_name = "铜川市"
#"西安市" "咸阳市"  "宝鸡市"  "渭南市"  "商洛市"  "汉中市"  "安康市"  "榆林市"  "延安市"  "铜川市"
clcd_folder = "G:\\\\graduation_database\\\\CLCD"
#night_folder = "G:\\\\graduation_database\\\\Night"
base_shp_dir = r"G:\graduation_database\boundry\base\陕西省.shp"
#下一步时间

temp_folder = r"G:\graduation_database\Analysis_temp"
temp_xls_folder = "G:\\\\graduation_database\\\\Analysis_temp\\\\xls"
temp_clcd_folder = r"G:\graduation_database\Analysis_temp\temp_clcd"

city = []
temp_shp_folder = "G:\\\\graduation_database\\\\Analysis_temp\\\\shp"
temp_shp_dir = temp_shp_folder + "\\\\" + city_name + ".shp"

city.append(city_name)

#clear and rebuild folderee
gs.clear_folder(temp_folder)
gs.cerate_folder(temp_xls_folder)
gs.cerate_folder(temp_shp_folder)
gs.cerate_folder(temp_clcd_folder)
#select boundry
gs.SelectByAttribute(base_shp_dir,"name",ogr.OFTString,city,"WGS84",temp_shp_dir)
#clip raster
for filename in os.listdir(clcd_folder):
    rester_dir = clcd_folder + "\\\\" + filename
    gdal_clip.clip_rester(rester_dir,temp_shp_dir,temp_clcd_folder)
#summery


#caculate execute time
end_time = time.time()
execute_time = end_time - start_time
print(f"Execution time : {execute_time} sec.")