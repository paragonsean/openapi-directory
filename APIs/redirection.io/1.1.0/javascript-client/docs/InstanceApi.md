# RedirectionIo.InstanceApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getInstanceCollection**](InstanceApi.md#getInstanceCollection) | **GET** /instances | Retrieves the collection of Instance resources.
[**getInstanceItem**](InstanceApi.md#getInstanceItem) | **GET** /instances/{id} | Retrieves a Instance resource.
[**liveInstanceItem**](InstanceApi.md#liveInstanceItem) | **PUT** /instances/{id}/live | Replaces the Instance resource.
[**loggingInstanceItem**](InstanceApi.md#loggingInstanceItem) | **PUT** /instances/{id} | Replaces the Instance resource.
[**postInstanceCollection**](InstanceApi.md#postInstanceCollection) | **POST** /agent-instance-updates | Creates a Instance resource.
[**putInstanceItem**](InstanceApi.md#putInstanceItem) | **PUT** /agent-instance-updates/{id} | Replaces the Instance resource.



## getInstanceCollection

> [InstanceRead] getInstanceCollection(projectId)

Retrieves the collection of Instance resources.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.InstanceApi();
let projectId = "projectId_example"; // String | 
apiInstance.getInstanceCollection(projectId, (error, data, response) => {
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

### Return type

[**[InstanceRead]**](InstanceRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## getInstanceItem

> InstanceRead getInstanceItem(id)

Retrieves a Instance resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.InstanceApi();
let id = "id_example"; // String | 
apiInstance.getInstanceItem(id, (error, data, response) => {
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

[**InstanceRead**](InstanceRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## liveInstanceItem

> InstanceRead liveInstanceItem(id, opts)

Replaces the Instance resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.InstanceApi();
let id = "id_example"; // String | 
let opts = {
  'instance': new RedirectionIo.InstanceWrite() // InstanceWrite | The updated Instance resource
};
apiInstance.liveInstanceItem(id, opts, (error, data, response) => {
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
 **instance** | [**InstanceWrite**](InstanceWrite.md)| The updated Instance resource | [optional] 

### Return type

[**InstanceRead**](InstanceRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv


## loggingInstanceItem

> InstanceRead loggingInstanceItem(id, opts)

Replaces the Instance resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.InstanceApi();
let id = "id_example"; // String | 
let opts = {
  'instance': new RedirectionIo.InstanceWrite() // InstanceWrite | The updated Instance resource
};
apiInstance.loggingInstanceItem(id, opts, (error, data, response) => {
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
 **instance** | [**InstanceWrite**](InstanceWrite.md)| The updated Instance resource | [optional] 

### Return type

[**InstanceRead**](InstanceRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv


## postInstanceCollection

> InstanceRead postInstanceCollection(opts)

Creates a Instance resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.InstanceApi();
let opts = {
  'instance': new RedirectionIo.InstanceWrite() // InstanceWrite | The new Instance resource
};
apiInstance.postInstanceCollection(opts, (error, data, response) => {
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
 **instance** | [**InstanceWrite**](InstanceWrite.md)| The new Instance resource | [optional] 

### Return type

[**InstanceRead**](InstanceRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv


## putInstanceItem

> InstanceRead putInstanceItem(id, opts)

Replaces the Instance resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.InstanceApi();
let id = "id_example"; // String | 
let opts = {
  'instance': new RedirectionIo.InstanceWrite() // InstanceWrite | The updated Instance resource
};
apiInstance.putInstanceItem(id, opts, (error, data, response) => {
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
 **instance** | [**InstanceWrite**](InstanceWrite.md)| The updated Instance resource | [optional] 

### Return type

[**InstanceRead**](InstanceRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv

