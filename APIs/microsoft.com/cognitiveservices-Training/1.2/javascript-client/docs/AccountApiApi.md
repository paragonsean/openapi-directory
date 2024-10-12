# TrainingApi.AccountApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAccountInfo**](AccountApiApi.md#getAccountInfo) | **GET** /account | Get basic information about your account



## getAccountInfo

> Account getAccountInfo(trainingKey)

Get basic information about your account

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.AccountApiApi();
let trainingKey = "{API Key}"; // String | 
apiInstance.getAccountInfo(trainingKey, (error, data, response) => {
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
 **trainingKey** | **String**|  | 

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

