# RedirectionIo.ImportApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getImportCollection**](ImportApi.md#getImportCollection) | **GET** /imports | Retrieves the collection of Import resources.
[**getImportItem**](ImportApi.md#getImportItem) | **GET** /imports/{id} | Retrieves a Import resource.
[**postImportCollection**](ImportApi.md#postImportCollection) | **POST** /imports | Creates a Import resource.



## getImportCollection

> [ImportRead] getImportCollection(projectId, opts)

Retrieves the collection of Import resources.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.ImportApi();
let projectId = "projectId_example"; // String | 
let opts = {
  'page': 56 // Number | The collection page number
};
apiInstance.getImportCollection(projectId, opts, (error, data, response) => {
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
 **page** | **Number**| The collection page number | [optional] 

### Return type

[**[ImportRead]**](ImportRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## getImportItem

> ImportRead getImportItem(id)

Retrieves a Import resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.ImportApi();
let id = "id_example"; // String | 
apiInstance.getImportItem(id, (error, data, response) => {
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

[**ImportRead**](ImportRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## postImportCollection

> ImportRead postImportCollection(opts)

Creates a Import resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.ImportApi();
let opts = {
  '_import': new RedirectionIo.ImportWrite() // ImportWrite | The new Import resource
};
apiInstance.postImportCollection(opts, (error, data, response) => {
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
 **_import** | [**ImportWrite**](ImportWrite.md)| The new Import resource | [optional] 

### Return type

[**ImportRead**](ImportRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv

