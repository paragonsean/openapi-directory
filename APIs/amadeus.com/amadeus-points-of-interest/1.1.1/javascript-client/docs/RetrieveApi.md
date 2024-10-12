# PointsOfInterest.RetrieveApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPointOfInterest**](RetrieveApi.md#getPointOfInterest) | **GET** /reference-data/locations/pois/{poisId} | Retieve one point of interest by its Id.



## getPointOfInterest

> Success1 getPointOfInterest(poisId)

Retieve one point of interest by its Id.

### Example

```javascript
import PointsOfInterest from 'points_of_interest';

let apiInstance = new PointsOfInterest.RetrieveApi();
let poisId = "poisId_example"; // String | identifier of the pois
apiInstance.getPointOfInterest(poisId, (error, data, response) => {
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
 **poisId** | **String**| identifier of the pois | 

### Return type

[**Success1**](Success1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

