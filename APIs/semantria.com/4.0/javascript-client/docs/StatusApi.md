# Semantria.StatusApi

All URIs are relative to *https://api.semantria.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getStatus**](StatusApi.md#getStatus) | **GET** /status.{content_type} | Retrieve API status



## getStatus

> Status getStatus(contentType)

Retrieve API status

This method retrieves API status information such as the app version, current API version, supported languages and encodings, the overall service status, etc.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.StatusApi();
let contentType = "contentType_example"; // String | 
apiInstance.getStatus(contentType, (error, data, response) => {
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
 **contentType** | **String**|  | 

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

