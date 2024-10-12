# RedirectionIo.UserProjectFlattenedApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getUserProjectFlattenedItem**](UserProjectFlattenedApi.md#getUserProjectFlattenedItem) | **GET** /user-project-flatteneds/{id} | Retrieves a UserProjectFlattened resource.



## getUserProjectFlattenedItem

> UserProjectFlattenedRead getUserProjectFlattenedItem(id)

Retrieves a UserProjectFlattened resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.UserProjectFlattenedApi();
let id = "id_example"; // String | 
apiInstance.getUserProjectFlattenedItem(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**UserProjectFlattenedRead**](UserProjectFlattenedRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv

