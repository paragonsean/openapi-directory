

# GetServicePointsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**GetServicePointsRequestBodyAddress**](GetServicePointsRequestBodyAddress.md) |  |  [optional] |
|**addressQuery** | **String** | Unstructured text to search for service points by. |  [optional] |
|**lat** | **Double** | The latitude of the point. Represented as signed degrees. Required if long is provided. http://www.geomidpoint.com/latlon.html |  [optional] |
|**_long** | **Double** | The longitude of the point. Represented as signed degrees. Required if lat is provided. http://www.geomidpoint.com/latlon.html |  [optional] |
|**maxResults** | **Integer** | The maximum number of service points to return |  [optional] |
|**providers** | [**List&lt;GetServicePointsRequestBodyProvidersInner&gt;**](GetServicePointsRequestBodyProvidersInner.md) | An array of shipping service providers and service codes |  |
|**radius** | **Integer** | Search radius in kilometers |  [optional] |



