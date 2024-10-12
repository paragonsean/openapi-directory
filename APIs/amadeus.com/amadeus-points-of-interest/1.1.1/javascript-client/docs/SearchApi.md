# PointsOfInterest.SearchApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPointsOfInterest**](SearchApi.md#getPointsOfInterest) | **GET** /reference-data/locations/pois | Returns points of interest for a given location and radius.
[**getPointsOfInterestBySquare**](SearchApi.md#getPointsOfInterestBySquare) | **GET** /reference-data/locations/pois/by-square | Returns points of interest for a given area



## getPointsOfInterest

> Success getPointsOfInterest(latitude, longitude, opts)

Returns points of interest for a given location and radius.

### Example

```javascript
import PointsOfInterest from 'points_of_interest';

let apiInstance = new PointsOfInterest.SearchApi();
let latitude = 41.397158; // Number | Latitude (decimal coordinates)
let longitude = 2.160873; // Number | Longitude (decimal coordinates)
let opts = {
  'radius': 1, // Number | radius of the search in Kilometer. Can be from 0 to 20, default value is 1 Km.
  'pageLimit': 10, // Number | maximum items in one page
  'pageOffset': 0, // Number | start index of the requested page
  'categories': ["null"] // [String] | category of the location.   Multiple value can be selected using a comma i.e. SIGHTS, SHOPPING 
};
apiInstance.getPointsOfInterest(latitude, longitude, opts, (error, data, response) => {
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
 **categories** | [**[String]**](String.md)| category of the location.   Multiple value can be selected using a comma i.e. SIGHTS, SHOPPING  | [optional] 

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json


## getPointsOfInterestBySquare

> Success getPointsOfInterestBySquare(north, west, south, east, opts)

Returns points of interest for a given area

### Example

```javascript
import PointsOfInterest from 'points_of_interest';

let apiInstance = new PointsOfInterest.SearchApi();
let north = 41.397158; // Number | Latitude north of bounding box (decimal coordinates)
let west = 2.160873; // Number | Longitude west of bounding box (decimal coordinates)
let south = 41.394582; // Number | Latitude south of bounding box (decimal coordinates)
let east = 2.177181; // Number | Longitude east of bounding box (decimal coordinates)
let opts = {
  'pageLimit': 10, // Number | maximum items in one page
  'pageOffset': 0, // Number | start index of the requested page
  'categories': ["null"] // [String] | category of the location.   Multiple value can be selected using a comma i.e. SIGHTS, SHOPPING 
};
apiInstance.getPointsOfInterestBySquare(north, west, south, east, opts, (error, data, response) => {
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
 **categories** | [**[String]**](String.md)| category of the location.   Multiple value can be selected using a comma i.e. SIGHTS, SHOPPING  | [optional] 

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

