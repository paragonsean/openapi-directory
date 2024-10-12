# RedirectionIo.ImpactSmartListApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getImpactSmartListItem**](ImpactSmartListApi.md#getImpactSmartListItem) | **GET** /impact-smart-lists/{id} | Retrieves a ImpactSmartList resource.
[**postImpactSmartListCollection**](ImpactSmartListApi.md#postImpactSmartListCollection) | **POST** /impact-smart-lists | Creates a ImpactSmartList resource.



## getImpactSmartListItem

> ImpactSmartListRead getImpactSmartListItem(id)

Retrieves a ImpactSmartList resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.ImpactSmartListApi();
let id = "id_example"; // String | 
apiInstance.getImpactSmartListItem(id, (error, data, response) => {
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

[**ImpactSmartListRead**](ImpactSmartListRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## postImpactSmartListCollection

> ImpactSmartListRead postImpactSmartListCollection(opts)

Creates a ImpactSmartList resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.ImpactSmartListApi();
let opts = {
  'impactSmartList': new RedirectionIo.ImpactSmartListWrite() // ImpactSmartListWrite | The new ImpactSmartList resource
};
apiInstance.postImpactSmartListCollection(opts, (error, data, response) => {
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
 **impactSmartList** | [**ImpactSmartListWrite**](ImpactSmartListWrite.md)| The new ImpactSmartList resource | [optional] 

### Return type

[**ImpactSmartListRead**](ImpactSmartListRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv

