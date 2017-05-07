# Using ArcGIS Collector with OpenStreetMap

## Background
Kigeme refugee camp is located in Southern Rwanda, Africa and serves over 18,000 refugees, up to 40% of which are children. Rochester Institute of Technology researchers and students [visited](https://www.rit.edu/news/story.php?id=54486) the camp and collected GIS survey data using [ArcGIS Collector](http://www.esri.com/products/collector-for-arcgis) about boundaries, roads, and facilities. Access to geographic data empowers researchers, administrators, and residents to improve life in the camp, however there exists no direct way to incorporate the information gathered along with metadata into the world's largest free geographical database: OpenStreetMap. Currently, the data around the camp is sparse at best:

![](https://github.com/kwm4385/ArcGIS_collector2OSM/raw/master/Screenshots/before.PNG)

## Solution
The researchers using ArcGIS Collector had stored the majority of feature-specific data such as building and path types, names, and more using the comments field in a non-standard format, since it is difficult to ad-hoc information into predefined feature classes in ArcGIS. While easy for users collecting the data, it is more difficult to symbolize these attributes once the data is exported. Therefore, heuristics were needed to classify different types of data points and add attributes which would be necessary for OpenStreetMap. Many of the comment fields were populated in a similar fashion with general information about the feature:

`Name: Umurava, 5 classrooms, Function: Office building`

While not all data was properly formatted, it was enough to start breaking out various fields from the comments, such as `name` by performing string operations to identify key-value pairs denoted `Key: Value,`. These were then added as individual fields on the feature class. Field names were also modified as necessary to conform to known required OSM attributes. To ensure that polygons would be drawn as such when exported instead of closed ways (lines), the `area=true` attribute was added. 

Once the required modifications were made to prepare the data, the newly exported shapefiles containing each type of feature were loaded into [JOSM](https://josm.openstreetmap.de/), a desktop editor for OpenStreetMap using the OpenData plugin to enable reading of ESRI shapefiles. Once imported, it was only a matter of entering credentials for an OSM account and uploading the data. Once done, spot checks were performed on the new features and conversions tweaked until a satisfactory result was reached.

*Detail view of the data symbolized in the OpenStreetMap web view after upload:*
![](https://github.com/kwm4385/ArcGIS_collector2OSM/raw/master/Screenshots/after.png)

## Limitations
Due to the fact that OSM uses a slightly different data format from the relational databases of ESRI products, some attributes of the Kigeme could not be directly converted within ArcMap. For example, the `line_feature` class contained different types of real-world objects such as roads an fences. While it may make sense to store both in a single line feature class, it meant that adding a `barrier` field for fence instances would force the entire table to carry this column. OSM places meaning on the existance of keys, not just values, and no distinction would be made between the fence and non-fence objects in the class. For cases such as this, the data was manually separated in OSM and the correct attributes applied. The most straightforward workaround for this in future runs would be to create multiple feature classes for each type of line, point, or polygon at the time of collection. Not only would this have the benefit of being easier to export to OSM, but the resulting data would be more friendly to work with in ArcMap as well.

Since OpenStreetMap does not support attachments of any type, images associated with certain features were not included in the export.

# Usage
The following instructions and accompanying repository are designed to allow the automation and repetition of the process described above. 

## Collecting Data
For the purposes of this outline, it is assumed the user is already proficient using the ArcGIS collector app and associated ESRI web services. For more information: visit http://doc.arcgis.com/en/collector/

1. Create a map feature for each type of entity you wish to create: such as buildings, areas, roads, and barriers.
2. Decide upon which tags will be used to describe each feature. This includes any metadata like names or business types. [OSM TagFinder](https://tagfinder.herokuapp.com/) may be used to search for appropriate tags which are compatable with OpenStreetMap. 
3. Enter comments on new features using the format `Tag: value` and separate with commas. 

## Preparing Data for Export
1. Open the collected data in ArcMap.
2. Create a new Feature Dataset which will contain the feature classes to be exported. The coordinate system should be set to `WGS_1984`. All data in OpenStreetMap uses this system.
3. Export the feature classes to be used to this feature dataset using Export > To Geodatabase... (Single).
4. The ArcMap Toolset in this repo contains several scripts used to add the required OSM tags to the data. The primary method for doing this is via the Prepare_OSM model, which runs all of the scripts on each feature class in a feature dataset and deposits the new copies in a specified output folder. The interface is shown below:

![](https://raw.githubusercontent.com/kwm4385/ArcGIS_collector2OSM/master/Screenshots/model_window.png)

Enter any OSM tag names you used in the comments field when collecting in the `Additional Field Names` box, seperated by commas. The script will search for the `Name` tag by default.

## Importing the Data to OpenStreetMap
There are many ways to import ESRI shapefiles into OpenStreetMap. Most involve converting them into the OSM XML format. While either way will work with the data you have created, the rest of the instructions will refer to JOSM, which can read shapefiles and edit directly and does not require conversion.
1. Download and install [JOSM](https://josm.openstreetmap.de/), a desktop OpenStreetMap editor.
2. Download and install the [OpenData plugin](https://wiki.openstreetmap.org/wiki/JOSM/Plugins/OpenData) for JOSM by following the [instructions](https://wiki.openstreetmap.org/wiki/JOSM/Plugins/OpenData#Installation) in the documentation.
3. For each shapefile exported using the Prepare_OSM model, choose File > Open to open it in JOSM. (It is recommended to do the following steps on one shapefile at a time)
4. Spot check the data shown in the map view to ensure it is geographically correct and contains all the desired metadata. It may be helpful to download the existing data at the location from OpenStreetMap to view alongside. This can be accomplished by clicking the Download button in the toolbar and using one of the provided methods to choose a download area. 
5. Once you are sure the data appears correct, click the upload button. 

**Important** 

*Excersise extreme caution if you are uploading data in an already well-mapped area. It may be covered under a well-established community of editors with whom you should consult before making mass changes. There is also no direct way to revert a changeset within OpenStreetMap.*
