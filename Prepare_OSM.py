# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Prepare_OSM.py
# Created on: 2017-05-10 23:19:15.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: Prepare_OSM <Features> <Output_Location> <Additional_Field_Names> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Load required toolboxes
arcpy.ImportToolbox("Model Functions")
arcpy.ImportToolbox("D:/ArcMap/Project/OSM_Data.gdb/OSM")

# Script arguments
Features = arcpy.GetParameterAsText(0)
if Features == '#' or not Features:
    Features = "D:\\ArcMap\\Project\\OSM_Data.gdb\\Features" # provide a default value if unspecified

Output_Location = arcpy.GetParameterAsText(1)

Additional_Field_Names = arcpy.GetParameterAsText(2)

# Local variables:
Feature = "D:\\ArcMap\\Project\\OSM_Data.gdb\\Features\\areas"
Output_Feature_Class = Feature
Name = "areas"
Done = ""
Done__2_ = ""

# Process: Iterate Feature Classes
arcpy.IterateFeatureClasses_mb(Features, "", "", "NOT_RECURSIVE")

# Process: Feature Class to Feature Class
arcpy.FeatureClassToFeatureClass_conversion(Feature, Output_Location, Name, "", "", "")

# Process: AddAreaTags
arcpy.gp.toolbox = "D:/ArcMap/Project/OSM_Data.gdb/OSM";
# Warning: the toolbox D:/ArcMap/Project/OSM_Data.gdb/OSM DOES NOT have an alias. 
# Please assign this toolbox an alias to avoid tool name collisions
# And replace arcpy.gp.AddAreaTags(...) with arcpy.AddAreaTags_ALIAS(...)
arcpy.gp.AddAreaTags(Output_Feature_Class)

# Process: ExtractOSMTags
arcpy.gp.toolbox = "D:/ArcMap/Project/OSM_Data.gdb/OSM";
# Warning: the toolbox D:/ArcMap/Project/OSM_Data.gdb/OSM DOES NOT have an alias. 
# Please assign this toolbox an alias to avoid tool name collisions
# And replace arcpy.gp.ExtractOSMTags(...) with arcpy.ExtractOSMTags_ALIAS(...)
arcpy.gp.ExtractOSMTags(Output_Feature_Class, Additional_Field_Names)

