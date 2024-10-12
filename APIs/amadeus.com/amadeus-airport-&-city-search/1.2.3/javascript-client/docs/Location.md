# AirportCitySearch.Location

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**analytics** | [**Analytics**](Analytics.md) |  | [optional] 
**category** | **String** | category of the location | [optional] 
**detailedName** | **String** | detailed name of the location. For a city location it contains city name and country code. For an airport location it contains city name; country code and airport full name | [optional] 
**distance** | [**Distance**](Distance.md) |  | [optional] 
**geoCode** | [**GeoCode**](GeoCode.md) |  | [optional] 
**iataCode** | **String** | IATA code of the location. ([IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx) here) | [optional] 
**id** | **String** | id of the ressource | [optional] 
**name** | **String** | short name of the location | [optional] 
**rank** | **String** | the rank is the position compared to other locations based on how famous is a place. 1 being the highest. | [optional] 
**relevance** | **Number** | score value calculated based on distance and analytics | [optional] 
**self** | [**Links**](Links.md) |  | [optional] 
**subType** | **String** | location sub type | [optional] 
**tags** | **[String]** | list of tags related to the location | [optional] 
**timeZoneOffset** | **String** | timezone offset of the location at the date of the API call (including daylight saving time) | [optional] 
**type** | **String** | the resource name | [optional] 



## Enum: CategoryEnum


* `SIGHTS` (value: `"SIGHTS"`)

* `BEACH_PARK` (value: `"BEACH_PARK"`)

* `HISTORICAL` (value: `"HISTORICAL"`)

* `NIGHTLIFE` (value: `"NIGHTLIFE"`)

* `RESTAURANT` (value: `"RESTAURANT"`)

* `SHOPPING` (value: `"SHOPPING"`)





## Enum: SubTypeEnum


* `AIRPORT` (value: `"AIRPORT"`)

* `CITY` (value: `"CITY"`)

* `POINT_OF_INTEREST` (value: `"POINT_OF_INTEREST"`)

* `DISTRICT` (value: `"DISTRICT"`)




