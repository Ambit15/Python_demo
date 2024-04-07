from osgeo import ogr, osr, gdal
import shutil
import os


def is_empty(dir):
    a = None
    
    if len(os.listdir(dir)) == 0:
        a = 0
    else:
        a = 1
    #0 empty ; 1 not empty
    return a


def clear_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')
 

def cerate_folder(folder_path):
    os.makedirs(folder_path, exist_ok=True)

#https://blog.csdn.net/qq_20373723/article/details/123504321
# -*- coding: utf-8 -*-
 
gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8", "YES")
gdal.SetConfigOption("SHAPE_ENCODING", "UTF8")
 
#gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8", "NO")
#gdal.SetConfigOption( "SHAPE_ENCODING", "GBK")

def Add_Field(input_lyr, field_name, ogr_field_type):
    """
    Add a field to a layer using the following ogr field types:
    0 = ogr.OFTInteger
    1 = ogr.OFTIntegerList
    2 = ogr.OFTReal
    3 = ogr.OFTRealList
    4 = ogr.OFTString
    5 = ogr.OFTStringList
    6 = ogr.OFTWideString
    7 = ogr.OFTWideStringList
    8 = ogr.OFTBinary
    9 = ogr.OFTDate
    10 = ogr.OFTTime
    11 = ogr.OFTDateTime
    """
 
    # List fields
    fields_ls = List_Fields(input_lyr)
 
    # Check if field exist
    if field_name in fields_ls:
        raise Exception('Field: "{0}" already exists'.format(field_name))
 
    # Create field
    inp_field = ogr.FieldDefn(field_name, ogr_field_type)
    input_lyr.CreateField(inp_field)
 
    return inp_field

def SelectByAttribute(InShp, Field, FieldType, attriNames, coor, outShp):
    ds = ogr.Open(InShp,0)
    if ds is None:
        raise OSError('Could not open {}'.format(InShp))
    ly_count = ds.GetLayerCount()
    layer = ds.GetLayer(0)
    lyInfo = layer.GetLayerDefn()
    driver = ogr.GetDriverByName("ESRI Shapefile") 
    if os.access(outShp, os.F_OK ): #如文件已存在，则删除
        driver.DeleteDataSource(outShp) 
    ds_new = driver.CreateDataSource(outShp) #创建shp文件
    spatialref_new = osr.SpatialReference()
    CoorDict = {'WGS84':4326, 'BeiJing54': 4214, 'XIAN80':4610, 'CGCS2000': 4490}
    spatialref_new.ImportFromEPSG(CoorDict[coor])
    geomtype = ogr.wkbPolygon 
 
    layer_new = ds_new.CreateLayer(outShp[:-4], srs=spatialref_new, geom_type=geomtype,) 
    #创建图层 for fd in fieldlist: #将字段列表写入图层
    layer_new.CreateField(ogr.FieldDefn(Field, FieldType))
 
    features = []
    for i in range(layer.GetFeatureCount()):
        feature = layer.GetFeature(i)
        geom_polygon = feature.GetGeometryRef()
        name = feature.GetField(Field)
        feat = ogr.Feature(layer_new.GetLayerDefn())
 
        if name in attriNames:
            feat.SetGeometry(geom_polygon)
            feat.SetField(Field, name)
            features.append(feat)
 
    for f in features:
        layer_new.CreateFeature(f)
    ds.Destroy()
    ds_new.Destroy()

#test

#cerate_folder(temp_shp_folder)
#SelectByAttribute(base_shp_dir,"name",ogr.OFTString,city,"WGS84",temp_shp_dir)
