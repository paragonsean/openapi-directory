

# Location


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**CategoryEnum**](#CategoryEnum) | category of the location |  [optional] |
|**geoCode** | [**GeoCode**](GeoCode.md) |  |  [optional] |
|**id** | **String** | id of the ressource |  [optional] |
|**name** | **String** | short name of the location |  [optional] |
|**rank** | **String** | the rank is the position compared to other locations based on how famous is a place. 1 being the highest. |  [optional] |
|**self** | [**Links**](Links.md) |  |  [optional] |
|**subType** | [**SubTypeEnum**](#SubTypeEnum) | location sub type |  [optional] |
|**tags** | **List&lt;String&gt;** | list of tags related to the location |  [optional] |
|**type** | **String** | the resource name |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| SIGHTS | &quot;SIGHTS&quot; |
| BEACH_PARK | &quot;BEACH_PARK&quot; |
| HISTORICAL | &quot;HISTORICAL&quot; |
| NIGHTLIFE | &quot;NIGHTLIFE&quot; |
| RESTAURANT | &quot;RESTAURANT&quot; |
| SHOPPING | &quot;SHOPPING&quot; |



## Enum: SubTypeEnum

| Name | Value |
|---- | -----|
| AIRPORT | &quot;AIRPORT&quot; |
| CITY | &quot;CITY&quot; |
| POINT_OF_INTEREST | &quot;POINT_OF_INTEREST&quot; |
| DISTRICT | &quot;DISTRICT&quot; |



