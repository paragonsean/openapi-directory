# RedirectionIo.ExplainUrlApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getExplainUrlItem**](ExplainUrlApi.md#getExplainUrlItem) | **GET** /explain-urls/{id} | Retrieves a ExplainUrl resource.
[**postExplainUrlCollection**](ExplainUrlApi.md#postExplainUrlCollection) | **POST** /explain-urls | Creates a ExplainUrl resource.



## getExplainUrlItem

> ExplainUrl getExplainUrlItem(id)

Retrieves a ExplainUrl resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.ExplainUrlApi();
let id = "id_example"; // String | 
apiInstance.getExplainUrlItem(id, (error, data, response) => {
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

[**ExplainUrl**](ExplainUrl.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## postExplainUrlCollection

> ExplainUrl postExplainUrlCollection(opts)

Creates a ExplainUrl resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.ExplainUrlApi();
let opts = {
  'explainUrl': new RedirectionIo.ExplainUrlWrite() // ExplainUrlWrite | The new ExplainUrl resource
};
apiInstance.postExplainUrlCollection(opts, (error, data, response) => {
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
 **explainUrl** | [**ExplainUrlWrite**](ExplainUrlWrite.md)| The new ExplainUrl resource | [optional] 

### Return type

[**ExplainUrl**](ExplainUrl.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv

