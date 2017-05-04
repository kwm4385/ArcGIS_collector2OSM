# Adds the area=yes tag to polygons to be recognized by OpenStreetMap

# import system modules
import arcpy, sys
from arcpy import env

arcpy.OverWriteOutput = True

feature = arcpy.GetParameterAsText(0)

# Get FC description
desc = arcpy.Describe(feature)
geometryType = desc.shapeType

# Continue if the FC is a polygon type
if geometryType == 'Polygon':
    arcpy.AddMessage('Input is geometryType: polygon. Adding area tags.')

    # Add new field
    arcpy.AddField_management(feature, "area", "TEXT", field_length = 5)

    # Populate it with "yes" for each row
    with arcpy.da.UpdateCursor(feature, "area") as cursor:
        for row in cursor:
            row[0] = "yes"
            cursor.updateRow(row)
else:
    arcpy.AddMessage('Input is not geometryType: polygon. Skipping...')

# Set output param true to indicate done
arcpy.SetParameterAsText(1, True)
