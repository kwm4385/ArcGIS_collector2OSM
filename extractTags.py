# Extracts various tags from the comment field by looking for keywords.

# import system modules
import arcpy, sys
from arcpy import env

# Searches the comment field for field name + ":" and if found, adds a new field with the given name
# and value containing the comment content until the next comma. For this works best with comment fields formatted as such:
# "field1: value, field2: value, field3: value"
def tryFindField(name, comment):
    name = name.lower()
    if comment and name + ':' in comment.lower():
        arcpy.AddField_management(feature, name, "TEXT", field_length = 50)
        start = comment.lower().find(name + ":");
        end = comment.find(",", start);

        if end == -1:
            value = comment[start + 5:]
        else:
            value = comment[start + 5: end if end < len(comment) else len(comment)]

        cursor.updateRow(row)
        row.setValue(name, value)


arcpy.OverWriteOutput = True

# Takes a feature class as input
feature = arcpy.GetParameterAsText(0)

# Input: additional tag names to search for in comment fields
tagNames = arcpy.GetParameterAsText(1)

# Examine row comment fields
cursor = arcpy.UpdateCursor(feature)
row = cursor.next()
while row:
    comment = row.getValue("comment")

    # Search for name value
    tryFindField("name", comment)

    # Search additional tag names provided
    if tagNames:
        for tag in tagNames.split(","):
            tryFindField(tag)

    row = cursor.next()

del row, cursor

# Examine existing field names
desc = arcpy.Describe(feature)
for field in desc.fields:
    if "business" in field.name:
        # General shop field will mark features appropriately
        arcpy.AddField_management(feature, "shop", "TEXT", field_length = 50)

    if "facility" in field.name:
        # General social_facility field will mark features appropriately
        arcpy.AddField_management(feature, "amenity", "TEXT", field_length = 50)
        cursor = arcpy.UpdateCursor(feature)
        row = cursor.next()
        while row:
            row.setValue("amenity", "social_facility")
            cursor.updateRow(row)
            row = cursor.next()
        del row, cursor

if desc.shapeType == "Polyline":
    # Add generic route tag to all lines
    arcpy.AddField_management(feature, "route", "TEXT", field_length = 50)


# Set output param true to indicate done
arcpy.SetParameterAsText(2, True)
