# ToursAndActivities.RetrieveApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gETActivity**](RetrieveApi.md#gETActivity) | **GET** /shopping/activities/{activityId} | Retrieve one activity by its id



## gETActivity

> SuccessfulSearch1 gETActivity(activityId)

Retrieve one activity by its id

### Example

```javascript
import ToursAndActivities from 'tours_and_activities';

let apiInstance = new ToursAndActivities.RetrieveApi();
let activityId = "activityId_example"; // String | 
apiInstance.gETActivity(activityId, (error, data, response) => {
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
 **activityId** | **String**|  | 

### Return type

[**SuccessfulSearch1**](SuccessfulSearch1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

