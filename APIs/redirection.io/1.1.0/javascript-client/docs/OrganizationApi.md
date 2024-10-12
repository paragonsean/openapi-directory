# RedirectionIo.OrganizationApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteOrganizationItem**](OrganizationApi.md#deleteOrganizationItem) | **DELETE** /organizations/{id} | Removes the Organization resource.
[**getOrganizationItem**](OrganizationApi.md#getOrganizationItem) | **GET** /organizations/{id} | Retrieves a Organization resource.
[**postOrganizationCollection**](OrganizationApi.md#postOrganizationCollection) | **POST** /organizations | Creates a Organization resource.
[**putOrganizationItem**](OrganizationApi.md#putOrganizationItem) | **PUT** /organizations/{id} | Replaces the Organization resource.



## deleteOrganizationItem

> deleteOrganizationItem(id)

Removes the Organization resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.OrganizationApi();
let id = "id_example"; // String | 
apiInstance.deleteOrganizationItem(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationItem

> OrganizationRead getOrganizationItem(id)

Retrieves a Organization resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.OrganizationApi();
let id = "id_example"; // String | 
apiInstance.getOrganizationItem(id, (error, data, response) => {
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

[**OrganizationRead**](OrganizationRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## postOrganizationCollection

> OrganizationRead postOrganizationCollection(opts)

Creates a Organization resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.OrganizationApi();
let opts = {
  'organization': new RedirectionIo.OrganizationWrite() // OrganizationWrite | The new Organization resource
};
apiInstance.postOrganizationCollection(opts, (error, data, response) => {
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
 **organization** | [**OrganizationWrite**](OrganizationWrite.md)| The new Organization resource | [optional] 

### Return type

[**OrganizationRead**](OrganizationRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv


## putOrganizationItem

> OrganizationRead putOrganizationItem(id, opts)

Replaces the Organization resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.OrganizationApi();
let id = "id_example"; // String | 
let opts = {
  'organization': new RedirectionIo.OrganizationWrite() // OrganizationWrite | The updated Organization resource
};
apiInstance.putOrganizationItem(id, opts, (error, data, response) => {
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
 **organization** | [**OrganizationWrite**](OrganizationWrite.md)| The updated Organization resource | [optional] 

### Return type

[**OrganizationRead**](OrganizationRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv

