# RedirectionIo.MatchingUrlApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMatchingUrlItem**](MatchingUrlApi.md#getMatchingUrlItem) | **GET** /matching-urls/{id} | Retrieves a MatchingUrl resource.
[**postMatchingUrlCollection**](MatchingUrlApi.md#postMatchingUrlCollection) | **POST** /matching-urls | Creates a MatchingUrl resource.



## getMatchingUrlItem

> MatchingUrlRead getMatchingUrlItem(id)

Retrieves a MatchingUrl resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.MatchingUrlApi();
let id = "id_example"; // String | 
apiInstance.getMatchingUrlItem(id, (error, data, response) => {
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

[**MatchingUrlRead**](MatchingUrlRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## postMatchingUrlCollection

> MatchingUrlRead postMatchingUrlCollection(opts)

Creates a MatchingUrl resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.MatchingUrlApi();
let opts = {
  'matchingUrl': new RedirectionIo.MatchingUrlWrite() // MatchingUrlWrite | The new MatchingUrl resource
};
apiInstance.postMatchingUrlCollection(opts, (error, data, response) => {
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
 **matchingUrl** | [**MatchingUrlWrite**](MatchingUrlWrite.md)| The new MatchingUrl resource | [optional] 

### Return type

[**MatchingUrlRead**](MatchingUrlRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv

