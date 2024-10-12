# RedirectionIo.CrawlUrlApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCrawlUrlCollection**](CrawlUrlApi.md#getCrawlUrlCollection) | **GET** /crawl-urls | Retrieves the collection of CrawlUrl resources.
[**getCrawlUrlItem**](CrawlUrlApi.md#getCrawlUrlItem) | **GET** /crawl-urls/{id} | Retrieves a CrawlUrl resource.



## getCrawlUrlCollection

> [CrawlUrlRead] getCrawlUrlCollection(opts)

Retrieves the collection of CrawlUrl resources.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.CrawlUrlApi();
let opts = {
  'page': 56 // Number | The collection page number
};
apiInstance.getCrawlUrlCollection(opts, (error, data, response) => {
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
 **page** | **Number**| The collection page number | [optional] 

### Return type

[**[CrawlUrlRead]**](CrawlUrlRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## getCrawlUrlItem

> CrawlUrlRead getCrawlUrlItem(id)

Retrieves a CrawlUrl resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.CrawlUrlApi();
let id = "id_example"; // String | 
apiInstance.getCrawlUrlItem(id, (error, data, response) => {
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

[**CrawlUrlRead**](CrawlUrlRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv

