# SafePlace.SearchApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSafetyRankBySquare**](SearchApi.md#getSafetyRankBySquare) | **GET** /safety/safety-rated-locations/by-square | Returns the safety rating of a given area
[**getSafetyRanking**](SearchApi.md#getSafetyRanking) | **GET** /safety/safety-rated-locations | Returns safety rating for a given location and radius.



## getSafetyRankBySquare

> Success getSafetyRankBySquare(north, west, south, east, opts)

Returns the safety rating of a given area

### Example

```javascript
import SafePlace from 'safe_place';

let apiInstance = new SafePlace.SearchApi();
let north = 41.397158; // Number | Latitude north of bounding box (decimal coordinates)
let west = 2.160873; // Number | Longitude west of bounding box (decimal coordinates)
let south = 41.394582; // Number | Latitude south of bounding box (decimal coordinates)
let east = 2.177181; // Number | Longitude east of bounding box (decimal coordinates)
let opts = {
  'pageLimit': 10, // Number | maximum items in one page
  'pageOffset': 0 // Number | start index of the requested page
};
apiInstance.getSafetyRankBySquare(north, west, south, east, opts, (error, data, response) => {
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
 **pageLimit** | **Number**| maximum items in one page | [optional] [default to 10]
 **pageOffset** | **Number**| start index of the requested page | [optional] [default to 0]

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json


## getSafetyRanking

> Success getSafetyRanking(latitude, longitude, opts)

Returns safety rating for a given location and radius.

### Example

```javascript
import SafePlace from 'safe_place';

let apiInstance = new SafePlace.SearchApi();
let latitude = 41.397158; // Number | Latitude (decimal coordinates)
let longitude = 2.160873; // Number | Longitude (decimal coordinates)
let opts = {
  'radius': 1, // Number | radius of the search in Kilometer. Can be from 0 to 20, default value is 1 Km.
  'pageLimit': 10, // Number | maximum items in one page
  'pageOffset': 0 // Number | start index of the requested page
};
apiInstance.getSafetyRanking(latitude, longitude, opts, (error, data, response) => {
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
 **pageLimit** | **Number**| maximum items in one page | [optional] [default to 10]
 **pageOffset** | **Number**| start index of the requested page | [optional] [default to 0]

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

