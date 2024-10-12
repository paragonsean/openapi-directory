# HotelNameAutocomplete.SuccessDataInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**SuccessDataInnerAddress**](SuccessDataInnerAddress.md) |  | [optional] 
**geoCode** | [**SuccessDataInnerGeoCode**](SuccessDataInnerGeoCode.md) |  | [optional] 
**hotelIds** | **[String]** | HotelIDs associated with the location only if it&#39;s a hotel. For leisure property dupes ID are listed as well.  | 
**iataCode** | **String** | [IATA codes](http://www.iata.org/publications/Pages/code-search.aspx) associated with the location. | 
**id** | **Number** | ID of the resource. | 
**name** | **String** | Name of the location (Hotel Name) | 
**relevance** | **Number** | A no. between 1-100. The higher the number better is the relevant search for that location. | [optional] 
**subType** | **String** | The category of the location or Point of reference (HOTEL_LEISURE,HOTEL_GDS). | 
**type** | **String** | Type of resource or the resource name. | 



## Enum: SubTypeEnum


* `GDS` (value: `"HOTEL_GDS"`)

* `LEISURE` (value: `"HOTEL_LEISURE"`)




