

# SuccessDataInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**SuccessDataInnerAddress**](SuccessDataInnerAddress.md) |  |  [optional] |
|**geoCode** | [**SuccessDataInnerGeoCode**](SuccessDataInnerGeoCode.md) |  |  [optional] |
|**hotelIds** | **Set&lt;String&gt;** | HotelIDs associated with the location only if it&#39;s a hotel. For leisure property dupes ID are listed as well.  |  |
|**iataCode** | **String** | [IATA codes](http://www.iata.org/publications/Pages/code-search.aspx) associated with the location. |  |
|**id** | **BigDecimal** | ID of the resource. |  |
|**name** | **String** | Name of the location (Hotel Name) |  |
|**relevance** | **Integer** | A no. between 1-100. The higher the number better is the relevant search for that location. |  [optional] |
|**subType** | [**SubTypeEnum**](#SubTypeEnum) | The category of the location or Point of reference (HOTEL_LEISURE,HOTEL_GDS). |  |
|**type** | **String** | Type of resource or the resource name. |  |



## Enum: SubTypeEnum

| Name | Value |
|---- | -----|
| GDS | &quot;HOTEL_GDS&quot; |
| LEISURE | &quot;HOTEL_LEISURE&quot; |



