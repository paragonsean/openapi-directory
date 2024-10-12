

# WaterlinkedConfiguration

Configuration parameters (default view)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**antennaEnabled** | **Boolean** | Enable use of antenna |  [optional] |
|**channel** | **Integer** | Channel to use |  |
|**compass** | [**CompassEnum**](#CompassEnum) | Compass provider setting |  |
|**environment** | [**EnvironmentEnum**](#EnvironmentEnum) | [Deprecated] Environment setting |  [optional] |
|**externalPpsEnabled** | **Boolean** | Enable external PPS input to master |  [optional] |
|**gps** | [**GpsEnum**](#GpsEnum) | GPS provider setting |  |
|**imuVehicleEnabled** | **Boolean** | [Deprecated] Enable IMU input from vehicle |  [optional] |
|**locatorType** | [**LocatorTypeEnum**](#LocatorTypeEnum) | Locator type in use |  |
|**rangeMaxX** | **BigDecimal** | [Deprecated] Max range (meters) |  [optional] |
|**rangeMaxY** | **BigDecimal** | [Deprecated] Max range (meters) |  [optional] |
|**rangeMaxZ** | **BigDecimal** | [Deprecated] Max range (meters) |  [optional] |
|**rangeMinX** | **BigDecimal** | [Deprecated] Max range (meters) |  [optional] |
|**rangeMinY** | **BigDecimal** | [Deprecated] Max range (meters) |  [optional] |
|**searchDirection** | **BigDecimal** | Direction of circular search area section |  [optional] |
|**searchRadius** | **BigDecimal** | Radius of circular search area |  [optional] |
|**searchSector** | **BigDecimal** | Sector angle of circular search area |  [optional] |
|**speedOfSound** | **Integer** | Speed of sound use by the system |  [optional] |
|**staticLat** | **BigDecimal** | Latitude to use in static mode |  |
|**staticLon** | **BigDecimal** | Longitude to use in static mode |  |
|**staticOrientation** | **BigDecimal** | Orientation/compass reading to use in static mode (degrees) |  |



## Enum: CompassEnum

| Name | Value |
|---- | -----|
| ONBOARD | &quot;onboard&quot; |
| STATIC | &quot;static&quot; |
| EXTERNAL | &quot;external&quot; |



## Enum: EnvironmentEnum

| Name | Value |
|---- | -----|
| REFLECTIVE | &quot;reflective&quot; |
| OPENWATER | &quot;openwater&quot; |



## Enum: GpsEnum

| Name | Value |
|---- | -----|
| ONBOARD | &quot;onboard&quot; |
| STATIC | &quot;static&quot; |
| EXTERNAL | &quot;external&quot; |



## Enum: LocatorTypeEnum

| Name | Value |
|---- | -----|
| D1 | &quot;d1&quot; |
| A1 | &quot;a1&quot; |
| S2 | &quot;s2&quot; |
| P2 | &quot;p2&quot; |
| U1 | &quot;u1&quot; |



