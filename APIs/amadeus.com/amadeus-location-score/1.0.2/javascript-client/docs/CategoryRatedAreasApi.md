# LocationScore.CategoryRatedAreasApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCategoryRatedAreas**](CategoryRatedAreasApi.md#getCategoryRatedAreas) | **GET** /location/analytics/category-rated-areas | GET category rated areas



## getCategoryRatedAreas

> GetCategoryRatedAreas200Response getCategoryRatedAreas(latitude, longitude)

GET category rated areas



### Example

```javascript
import LocationScore from 'location_score';

let apiInstance = new LocationScore.CategoryRatedAreasApi();
let latitude = 41.397158; // Number | Latitude in decimal coordinates
let longitude = 2.160873; // Number | Longitude in decimal coordinates
apiInstance.getCategoryRatedAreas(latitude, longitude, (error, data, response) => {
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
 **latitude** | **Number**| Latitude in decimal coordinates | 
 **longitude** | **Number**| Longitude in decimal coordinates | 

### Return type

[**GetCategoryRatedAreas200Response**](GetCategoryRatedAreas200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

