

# Location


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**Address**](Address.md) |  |  [optional] |
|**analytics** | [**Analytics**](Analytics.md) |  |  [optional] |
|**detailedName** | **String** | detailed name of the location. For a city location it contains city name and country code. For an airport location it contains city name; country code and airport full name |  [optional] |
|**distance** | [**Distance**](Distance.md) |  |  [optional] |
|**geoCode** | [**GeoCode**](GeoCode.md) |  |  [optional] |
|**iataCode** | **String** | IATA code of the location. ([IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx) here) |  [optional] |
|**name** | **String** | short name of the location |  [optional] |
|**relevance** | **Double** | score value calculated based on distance and analytics |  [optional] |
|**subType** | [**SubTypeEnum**](#SubTypeEnum) | location sub type |  [optional] |
|**timeZoneOffset** | **String** | timezone offset of the location at the date of the API call (including daylight saving time) |  [optional] |
|**type** | **String** | the resource name |  [optional] |



## Enum: SubTypeEnum

| Name | Value |
|---- | -----|
| AIRPORT | &quot;AIRPORT&quot; |
| CITY | &quot;CITY&quot; |
| POINT_OF_INTEREST | &quot;POINT_OF_INTEREST&quot; |
| DISTRICT | &quot;DISTRICT&quot; |



