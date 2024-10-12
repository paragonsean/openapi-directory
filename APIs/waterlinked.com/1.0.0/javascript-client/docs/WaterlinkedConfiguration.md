# TheWaterLinkedUnderwaterGpsApi.WaterlinkedConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**antennaEnabled** | **Boolean** | Enable use of antenna | [optional] 
**channel** | **Number** | Channel to use | 
**compass** | **String** | Compass provider setting | 
**environment** | **String** | [Deprecated] Environment setting | [optional] 
**externalPpsEnabled** | **Boolean** | Enable external PPS input to master | [optional] 
**gps** | **String** | GPS provider setting | 
**imuVehicleEnabled** | **Boolean** | [Deprecated] Enable IMU input from vehicle | [optional] 
**locatorType** | **String** | Locator type in use | 
**rangeMaxX** | **Number** | [Deprecated] Max range (meters) | [optional] 
**rangeMaxY** | **Number** | [Deprecated] Max range (meters) | [optional] 
**rangeMaxZ** | **Number** | [Deprecated] Max range (meters) | [optional] 
**rangeMinX** | **Number** | [Deprecated] Max range (meters) | [optional] 
**rangeMinY** | **Number** | [Deprecated] Max range (meters) | [optional] 
**searchDirection** | **Number** | Direction of circular search area section | [optional] 
**searchRadius** | **Number** | Radius of circular search area | [optional] 
**searchSector** | **Number** | Sector angle of circular search area | [optional] 
**speedOfSound** | **Number** | Speed of sound use by the system | [optional] 
**staticLat** | **Number** | Latitude to use in static mode | 
**staticLon** | **Number** | Longitude to use in static mode | 
**staticOrientation** | **Number** | Orientation/compass reading to use in static mode (degrees) | 



## Enum: CompassEnum


* `onboard` (value: `"onboard"`)

* `static` (value: `"static"`)

* `external` (value: `"external"`)





## Enum: EnvironmentEnum


* `reflective` (value: `"reflective"`)

* `openwater` (value: `"openwater"`)





## Enum: GpsEnum


* `onboard` (value: `"onboard"`)

* `static` (value: `"static"`)

* `external` (value: `"external"`)





## Enum: LocatorTypeEnum


* `d1` (value: `"d1"`)

* `a1` (value: `"a1"`)

* `s2` (value: `"s2"`)

* `p2` (value: `"p2"`)

* `u1` (value: `"u1"`)




