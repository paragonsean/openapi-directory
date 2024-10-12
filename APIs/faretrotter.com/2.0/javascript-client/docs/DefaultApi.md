# FaretrotterTravelApi.DefaultApi

All URIs are relative to *https://api.faretrotter.com/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gETPlaces**](DefaultApi.md#gETPlaces) | **GET** /places | Returns possible modes of transportation between two cities.
[**gETRoutes**](DefaultApi.md#gETRoutes) | **GET** /routes | 



## gETPlaces

> PlaceResponse gETPlaces()

Returns possible modes of transportation between two cities.

### Example

```javascript
import FaretrotterTravelApi from 'faretrotter_travel_api';

let apiInstance = new FaretrotterTravelApi.DefaultApi();
apiInstance.gETPlaces((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**PlaceResponse**](PlaceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gETRoutes

> RoutesResponse gETRoutes(originLat, originLng, destinationLat, destinationLng)



### Example

```javascript
import FaretrotterTravelApi from 'faretrotter_travel_api';

let apiInstance = new FaretrotterTravelApi.DefaultApi();
let originLat = 3.4; // Number | 
let originLng = 3.4; // Number | 
let destinationLat = 3.4; // Number | 
let destinationLng = 3.4; // Number | 
apiInstance.gETRoutes(originLat, originLng, destinationLat, destinationLng, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **originLat** | **Number**|  | 
 **originLng** | **Number**|  | 
 **destinationLat** | **Number**|  | 
 **destinationLng** | **Number**|  | 

### Return type

[**RoutesResponse**](RoutesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

