# RedirectionIo.PublishHistoryApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPublishHistoryCollection**](PublishHistoryApi.md#getPublishHistoryCollection) | **GET** /publish-histories | Retrieves the collection of PublishHistory resources.
[**getPublishHistoryItem**](PublishHistoryApi.md#getPublishHistoryItem) | **GET** /publish-histories/{id} | Retrieves a PublishHistory resource.



## getPublishHistoryCollection

> [PublishHistoryRead] getPublishHistoryCollection(projectId, opts)

Retrieves the collection of PublishHistory resources.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.PublishHistoryApi();
let projectId = "projectId_example"; // String | 
let opts = {
  'createdAtBefore': "createdAtBefore_example", // String | 
  'createdAtStrictlyBefore': "createdAtStrictlyBefore_example", // String | 
  'createdAtAfter': "createdAtAfter_example", // String | 
  'createdAtStrictlyAfter': "createdAtStrictlyAfter_example", // String | 
  'page': 56 // Number | The collection page number
};
apiInstance.getPublishHistoryCollection(projectId, opts, (error, data, response) => {
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
 **projectId** | **String**|  | 
 **createdAtBefore** | **String**|  | [optional] 
 **createdAtStrictlyBefore** | **String**|  | [optional] 
 **createdAtAfter** | **String**|  | [optional] 
 **createdAtStrictlyAfter** | **String**|  | [optional] 
 **page** | **Number**| The collection page number | [optional] 

### Return type

[**[PublishHistoryRead]**](PublishHistoryRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## getPublishHistoryItem

> PublishHistoryRead getPublishHistoryItem(id)

Retrieves a PublishHistory resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.PublishHistoryApi();
let id = "id_example"; // String | 
apiInstance.getPublishHistoryItem(id, (error, data, response) => {
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

[**PublishHistoryRead**](PublishHistoryRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv

