# Using ArcGIS Collector with OpenStreetMap

## Background
Kigeme refugee camp is located in Southern Rwanda, Africa and serves over 18,000 refugees, up to 40% of which are children. Rochester Institute of Technology researchers and students [visited](https://www.rit.edu/news/story.php?id=54486) the camp and collected GIS survey data using [ArcGIS Collector](http://www.esri.com/products/collector-for-arcgis) about boundaries, roads, and facilities. Access to geographic data empowers researchers, administrators, and residents to improve life in the camp, however there exists no direct way to incorporate the information gathered along with metadata into the world's largest free geographical database: OpenStreetMap. Currently, the data around the camp is sparse at best:

![](https://github.com/kwm4385/ArcGIS_collector2OSM/raw/master/Screenshots/before.PNG)

## Solution
The researchers using ArcGIS Collector had stored the majority of feature-specific data such as building and path types, names, and more using the comments field in a non-standard format, since it is difficult to ad-hoc information into predefined feature classes in ArcGIS. While easy for users collecting the data, it is more difficult to symbolize these attributes once the data is exported. Therefore, heuristics were needed to classify different types of data points and add attributes which would be necessary for OpenStreetMap. Many of the comment fields were populated in a similar fashion with general information about the feature:

```Name: Umurava, 5 classrooms, Function: Office building```

While not all data was properly formatted, it was enough to start breaking out various fields from the comments, such as `name` by performing string operations to identify key-value pairs denoted `Key: Value,`. These were then added as individual fields on the feature class. Field names were also modified as necessary to conform to known required OSM attributes. To ensure that polygons would be drawn as such when exported instead of closed ways (lines), the `area=true` attribute was added. 

Once the required modifications were made to prepare the data, the newly exported shapefiles containing each type of feature were loaded into [JOSM](https://josm.openstreetmap.de/), a desktop editor for OpenStreetMap using the OpenData plugin to enable reading of ESRI shapefiles. Once imported, it was only a matter of entering credentials for an OSM account and uploading the data. Once done, spot checks were performed on the new features and conversions tweaked until a satisfactory result was reached.

## Limitations
Due to the fact that OSM uses a slightly different data format from the relational databases of ESRI products, some attributes of the Kigeme could not be directly converted within ArcMap. For example, the `line_feature` class contained different types of real-world objects such as roads an fences. While it may make sense to store both in a single line feature class, it meant that adding a `barrier` field for fence instances would force the entire table to carry this column. OSM places meaning on the existance of keys, not just values, and no distinction would be made between the fence and non-fence objects in the class. For cases such as this, the data was manually separated in OSM and the correct attributes applied. The most straightforward workaround for this in future runs would be to create multiple feature classes for each type of line, point, or polygon at the time of collection. Not only would this have the benefit of being easier to export to OSM, but the resulting data would be more friendly to work with in ArcMap as well.

Since OpenStreetMap does not support attachments of any type, images associated with certain features were not included in the export.
