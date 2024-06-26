import os
import time
import gdal_clip
import gdal_select as gs
import gdal_summery_night as gsl
from osgeo import ogr

start_time = time.time()
#可选参数 #####
city_name = "铜川市"
#"西安市" "咸阳市"  "宝鸡市"  "渭南市"  "商洛市"  "汉中市"  "安康市"  "榆林市"  "延安市"  "铜川市"
#下一步时间

temp_folder = r"G:\graduation_database\Analysis_temp"
temp_xls_folder = "G:\\\\graduation_database\\\\calcuate\\\\model\\\\city_sum" + "\\\\" + city_name + ".xls"
temp_night_folder = r"G:\graduation_database\Analysis_temp\night"

city = []
temp_shp_folder = "G:\\\\graduation_database\\\\Analysis_temp\\\\shp"
temp_shp_dir = temp_shp_folder + "\\\\" + city_name + ".shp"
base_shp_dir = r"G:\graduation_database\boundry\base\陕西省.shp"
night_folder = "G:\\\\graduation_database\\\\Night"
city.append(city_name)

#clear and rebuild folderee
gs.clear_folder(temp_folder)
#gs.cerate_folder(temp_xls_folder)
gs.cerate_folder(temp_shp_folder)
gs.cerate_folder(temp_night_folder)
#select boundry
gs.SelectByAttribute(base_shp_dir,"name",ogr.OFTString,city,"WGS84",temp_shp_dir)
#clip night_light_raster
for filename in os.listdir(night_folder):
    rester_dir = night_folder + "\\\\" + filename
    gdal_clip.clip_rester(rester_dir,temp_shp_dir,temp_night_folder)
#summery
gsl.summery_mean(temp_night_folder,city_name,temp_xls_folder)

end_time = time.time()
execute_time = end_time - start_time
print(f"Execution time : {execute_time} sec.")