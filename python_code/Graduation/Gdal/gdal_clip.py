from osgeo import gdal as gd
import re
 

#different python version may cause different error
#please check python version
#check out email seting

def keep_digits(string):
    return re.sub("\D", "", string)
#该函数将字符串保留了数字

#确认年数字正确
def check_year(str):
    length = len(str)
    if length > 4:
        str = str[2:]
    return str

# 定义源数据文件名和裁剪矢量数据文件名
def clip_rester(rester_file,clip_boundry,save_file):

    #src_filename = 'source.tif'
    #vector_filename = 'clip_extent.shp'

    save_name = save_file + "\\" + check_year(keep_digits(rester_file)) + "_clip.tif"

    # 打开源数据集和裁剪矢量数据集
    src_ds = gd.Open(rester_file)
    vector_ds = gd.OpenEx(clip_boundry)
    #vector_ds = ogr.Open("xian.shp")

    # 指定裁剪操作的参数
    options = gd.WarpOptions(cutlineDSName=clip_boundry,cropToCutline=True,dstNodata=0)  # 可以根据需要修改 nodata 值 -1 night 

    # 执行裁剪操作，并将结果保存到目标文件中
    gd.Warp(save_name, src_ds, options=options)

    # 关闭数据集
    src_ds = None
    vector_ds = None

#clip_rester("G:\\graduation_database\\Night\\PANDA_China_2020.tif",r"G:\graduation_database\boundry\city\xian.shp","G:\\graduation_database\\N_clip")
#测试调用

#os 下的遍历文件

#night_folder = "G:\\\\graduation_database\\\\Night"

#for filename in os.listdir(night_folder):
#    rester_dir = night_folder + "\\\\" + filename
#    clip_rester(rester_dir,r"G:\graduation_database\boundry\city\xian.shp","G:\\graduation_database\\N_clip")