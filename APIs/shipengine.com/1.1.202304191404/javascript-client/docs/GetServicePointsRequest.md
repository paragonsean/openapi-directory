# ShipEngineApi.GetServicePointsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**GetServicePointsRequestBodyAddress**](GetServicePointsRequestBodyAddress.md) |  | [optional] 
**addressQuery** | **String** | Unstructured text to search for service points by. | [optional] 
**lat** | **Number** | The latitude of the point. Represented as signed degrees. Required if long is provided. http://www.geomidpoint.com/latlon.html | [optional] 
**_long** | **Number** | The longitude of the point. Represented as signed degrees. Required if lat is provided. http://www.geomidpoint.com/latlon.html | [optional] 
**maxResults** | **Number** | The maximum number of service points to return | [optional] 
**providers** | [**[GetServicePointsRequestBodyProvidersInner]**](GetServicePointsRequestBodyProvidersInner.md) | An array of shipping service providers and service codes | 
**radius** | **Number** | Search radius in kilometers | [optional] 


