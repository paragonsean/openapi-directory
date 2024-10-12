

# Address


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**curbside** | [**CurbsideEnum**](#CurbsideEnum) | Optional parameter. Specifies on which side a point should be relative to the driver when she leaves/arrives at a start/target/via point. Only supported for motor vehicles and OpenStreetMap. |  [optional] |
|**lat** | **Double** | Latitude of location. |  |
|**locationId** | **String** | Specifies the id of the location. |  |
|**lon** | **Double** | Longitude of location. |  |
|**name** | **String** | Name of location. |  [optional] |
|**streetHint** | **String** | Optional parameter. Specifies a hint for each address to better snap the coordinates (lon,lat) to road network. E.g. if there is an address or house with two or more neighboring streets you can control for which street the closest location is looked up. |  [optional] |



## Enum: CurbsideEnum

| Name | Value |
|---- | -----|
| RIGHT | &quot;right&quot; |
| LEFT | &quot;left&quot; |
| ANY | &quot;any&quot; |



