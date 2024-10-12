# ToursAndActivities.SearchApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listActivities**](SearchApi.md#listActivities) | **GET** /shopping/activities | Returns Activities around a given location
[**listActivitiesBySquare**](SearchApi.md#listActivitiesBySquare) | **GET** /shopping/activities/by-square | Returns Activities around a given location



## listActivities

> SuccessfulSearch listActivities(latitude, longitude, opts)

Returns Activities around a given location

### Example

```javascript
import ToursAndActivities from 'tours_and_activities';

let apiInstance = new ToursAndActivities.SearchApi();
let latitude = 41.397158; // Number | Latitude (decimal coordinates)
let longitude = 2.160873; // Number | Longitude (decimal coordinates)
let opts = {
  'radius': 1 // Number | radius of the search in Kilometer. Can be from 0 to 20, default value is 1 Km.
};
apiInstance.listActivities(latitude, longitude, opts, (error, data, response) => {
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
 **latitude** | **Number**| Latitude (decimal coordinates) | 
 **longitude** | **Number**| Longitude (decimal coordinates) | 
 **radius** | **Number**| radius of the search in Kilometer. Can be from 0 to 20, default value is 1 Km. | [optional] [default to 1]

### Return type

[**SuccessfulSearch**](SuccessfulSearch.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json


## listActivitiesBySquare

> SuccessfulSearch listActivitiesBySquare(north, west, south, east)

Returns Activities around a given location

### Example

```javascript
import ToursAndActivities from 'tours_and_activities';

let apiInstance = new ToursAndActivities.SearchApi();
let north = 41.397158; // Number | Latitude north of bounding box (decimal coordinates)
let west = 2.160873; // Number | Longitude west of bounding box (decimal coordinates)
let south = 41.394582; // Number | Latitude south of bounding box (decimal coordinates)
let east = 2.177181; // Number | Longitude east of bounding box (decimal coordinates)
apiInstance.listActivitiesBySquare(north, west, south, east, (error, data, response) => {
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
 **north** | **Number**| Latitude north of bounding box (decimal coordinates) | 
 **west** | **Number**| Longitude west of bounding box (decimal coordinates) | 
 **south** | **Number**| Latitude south of bounding box (decimal coordinates) | 
 **east** | **Number**| Longitude east of bounding box (decimal coordinates) | 

### Return type

[**SuccessfulSearch**](SuccessfulSearch.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

