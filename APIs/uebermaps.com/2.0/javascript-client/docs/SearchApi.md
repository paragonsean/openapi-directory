# UebermapsApiEndpoints.SearchApi

All URIs are relative to *http://uebermaps.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mapsSearchGet**](SearchApi.md#mapsSearchGet) | **GET** /maps/search | Search maps
[**spotsSearchGet**](SearchApi.md#spotsSearchGet) | **GET** /spots/search | Search spots
[**usersSearchGet**](SearchApi.md#usersSearchGet) | **GET** /users/search | Search users



## mapsSearchGet

> Map mapsSearchGet(opts)

Search maps

Search maps

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.SearchApi();
let opts = {
  'q': "q_example", // String | Query
  'd': 56, // Number | Distance. Diameter of search radius in meter (default: 2000 meter)
  'lat': 3.4, // Number | Latitude for search radius (default distance: 2000 meter)
  'lon': 3.4 // Number | Longitude for search radius (default distance: 2000 meter)
};
apiInstance.mapsSearchGet(opts, (error, data, response) => {
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
 **q** | **String**| Query | [optional] 
 **d** | **Number**| Distance. Diameter of search radius in meter (default: 2000 meter) | [optional] 
 **lat** | **Number**| Latitude for search radius (default distance: 2000 meter) | [optional] 
 **lon** | **Number**| Longitude for search radius (default distance: 2000 meter) | [optional] 

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## spotsSearchGet

> Spot spotsSearchGet(opts)

Search spots

Search spots

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.SearchApi();
let opts = {
  'q': "q_example", // String | Query
  'd': 56, // Number | Distance. Diameter of search radius in meter (default: 2000 meter)
  'lat': 3.4, // Number | Latitude for search radius (2 km)
  'lon': 3.4 // Number | Longitude for search radius (2 km)
};
apiInstance.spotsSearchGet(opts, (error, data, response) => {
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
 **q** | **String**| Query | [optional] 
 **d** | **Number**| Distance. Diameter of search radius in meter (default: 2000 meter) | [optional] 
 **lat** | **Number**| Latitude for search radius (2 km) | [optional] 
 **lon** | **Number**| Longitude for search radius (2 km) | [optional] 

### Return type

[**Spot**](Spot.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersSearchGet

> User usersSearchGet(opts)

Search users

Search users

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.SearchApi();
let opts = {
  'q': "q_example" // String | Query
};
apiInstance.usersSearchGet(opts, (error, data, response) => {
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
 **q** | **String**| Query | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

