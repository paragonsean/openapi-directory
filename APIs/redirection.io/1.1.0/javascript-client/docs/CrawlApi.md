# RedirectionIo.CrawlApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelCrawlItem**](CrawlApi.md#cancelCrawlItem) | **POST** /crawls/{id}/cancel | Creates a Crawl resource.
[**getCrawlCollection**](CrawlApi.md#getCrawlCollection) | **GET** /crawls | Retrieves the collection of Crawl resources.
[**getCrawlItem**](CrawlApi.md#getCrawlItem) | **GET** /crawls/{id} | Retrieves a Crawl resource.
[**postCrawlCollection**](CrawlApi.md#postCrawlCollection) | **POST** /crawls | Creates a Crawl resource.



## cancelCrawlItem

> CrawlReadDetails cancelCrawlItem(id, opts)

Creates a Crawl resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.CrawlApi();
let id = "id_example"; // String | 
let opts = {
  'crawl': new RedirectionIo.Crawl() // Crawl | The new Crawl resource
};
apiInstance.cancelCrawlItem(id, opts, (error, data, response) => {
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
 **crawl** | [**Crawl**](Crawl.md)| The new Crawl resource | [optional] 

### Return type

[**CrawlReadDetails**](CrawlReadDetails.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv


## getCrawlCollection

> [CrawlRead] getCrawlCollection(projectId, opts)

Retrieves the collection of Crawl resources.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.CrawlApi();
let projectId = "projectId_example"; // String | 
let opts = {
  'firstUrl': "firstUrl_example", // String | 
  'sortCreatedAt': "sortCreatedAt_example", // String | 
  'page': 56 // Number | The collection page number
};
apiInstance.getCrawlCollection(projectId, opts, (error, data, response) => {
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
 **firstUrl** | **String**|  | [optional] 
 **sortCreatedAt** | **String**|  | [optional] 
 **page** | **Number**| The collection page number | [optional] 

### Return type

[**[CrawlRead]**](CrawlRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## getCrawlItem

> CrawlReadDetails getCrawlItem(id)

Retrieves a Crawl resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.CrawlApi();
let id = "id_example"; // String | 
apiInstance.getCrawlItem(id, (error, data, response) => {
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

[**CrawlReadDetails**](CrawlReadDetails.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## postCrawlCollection

> Crawl postCrawlCollection(opts)

Creates a Crawl resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.CrawlApi();
let opts = {
  'crawl': new RedirectionIo.CrawlWrite() // CrawlWrite | The new Crawl resource
};
apiInstance.postCrawlCollection(opts, (error, data, response) => {
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
 **crawl** | [**CrawlWrite**](CrawlWrite.md)| The new Crawl resource | [optional] 

### Return type

[**Crawl**](Crawl.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv

