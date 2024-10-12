# SafePlace.RetrieveApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLocationSafetyRanking**](RetrieveApi.md#getLocationSafetyRanking) | **GET** /safety/safety-rated-locations/{safety-rated-locationId} | Retieve safety information of a location by its Id.



## getLocationSafetyRanking

> Success1 getLocationSafetyRanking(safetyRatedLocationId)

Retieve safety information of a location by its Id.

### Example

```javascript
import SafePlace from 'safe_place';

let apiInstance = new SafePlace.RetrieveApi();
let safetyRatedLocationId = "safetyRatedLocationId_example"; // String | identifier of the location
apiInstance.getLocationSafetyRanking(safetyRatedLocationId, (error, data, response) => {
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
 **safetyRatedLocationId** | **String**| identifier of the location | 

### Return type

[**Success1**](Success1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

