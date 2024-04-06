# from osgeo import gdal as gd
import geopandas as gpd
import pandas as pd
import math
def sumpi(num):
    num += math.pi
    return num
base_shp = gpd.read_file("")
base_image_Nightlight = ""
base_image_clcd = ""
