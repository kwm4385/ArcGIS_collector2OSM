# Using ArcGIS Collector with OpenStreetMap

## Background
Kigeme refugee camp is located in Southern Rwanda, Africa and serves over 18,000 refugees, up to 40% of which are children. Rochester Institute of Technology researchers and students [visited](https://www.rit.edu/news/story.php?id=54486) the camp and collected GIS survey data using [ArcGIS Collector](http://www.esri.com/products/collector-for-arcgis) about boundaries, roads, and facilities. Access to geographic data empowers researchers, administrators, and residents to improve life in the camp, however there exists no direct way to incorporate the information gathered along with metadata into the world's largest free geographical database: OpenStreetMap. Currently, the data around the camp is sparse at best:

![](https://github.com/kwm4385/ArcGIS_collector2OSM/raw/master/Screenshots/before.PNG)

## Solution
The researchers using ArcGIS Collector had stored the majority of feature-specific data such as building and path types, names, and more using the comments field in a non-standard format, since it is difficult to ad-hoc information into predefined feature classes in ArcGIS. While easy for users collecting the data, it is more difficult to symbolize these attributes once the data is exported. Therefore, heuristics were needed to classify different types of data points and add attributes which would be necessary for OpenStreetMap. Many of the comment fields were populated in a similar fashion with general information about the feature:

```Name: Umurava, 5 classrooms, Function: Office building```

While not all data was properly formatted, it was enough to start breaking out various fields from the comments, such as `name` by performing string operations to identify key-value pairs denoted `Key: Value,`. These were then added as individual fields on the feature class. Field names were also modified as necessary to conform to known required OSM attributes. To ensure that polygons would be drawn as such when exported instead of closed ways (lines), the `area=true` attribute was added. 
