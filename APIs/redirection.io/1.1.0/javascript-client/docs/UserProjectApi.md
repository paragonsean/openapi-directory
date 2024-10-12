# RedirectionIo.UserProjectApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteUserProjectItem**](UserProjectApi.md#deleteUserProjectItem) | **DELETE** /user-projects/{id} | Removes the UserProject resource.
[**getUserProjectItem**](UserProjectApi.md#getUserProjectItem) | **GET** /user-projects/{id} | Retrieves a UserProject resource.
[**postUserProjectCollection**](UserProjectApi.md#postUserProjectCollection) | **POST** /user-projects | Creates a UserProject resource.
[**putUserProjectItem**](UserProjectApi.md#putUserProjectItem) | **PUT** /user-projects/{id} | Replaces the UserProject resource.



## deleteUserProjectItem

> deleteUserProjectItem(id)

Removes the UserProject resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.UserProjectApi();
let id = "id_example"; // String | 
apiInstance.deleteUserProjectItem(id, (error, data, response) => {
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


## getUserProjectItem

> UserProjectRead getUserProjectItem(id)

Retrieves a UserProject resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.UserProjectApi();
let id = "id_example"; // String | 
apiInstance.getUserProjectItem(id, (error, data, response) => {
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

[**UserProjectRead**](UserProjectRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## postUserProjectCollection

> UserProjectRead postUserProjectCollection(opts)

Creates a UserProject resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.UserProjectApi();
let opts = {
  'userProject': new RedirectionIo.UserProjectCreationWrite() // UserProjectCreationWrite | The new UserProject resource
};
apiInstance.postUserProjectCollection(opts, (error, data, response) => {
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
 **userProject** | [**UserProjectCreationWrite**](UserProjectCreationWrite.md)| The new UserProject resource | [optional] 

### Return type

[**UserProjectRead**](UserProjectRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv


## putUserProjectItem

> UserProjectRead putUserProjectItem(id, opts)

Replaces the UserProject resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.UserProjectApi();
let id = "id_example"; // String | 
let opts = {
  'userProject': new RedirectionIo.UserProjectWrite() // UserProjectWrite | The updated UserProject resource
};
apiInstance.putUserProjectItem(id, opts, (error, data, response) => {
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
 **userProject** | [**UserProjectWrite**](UserProjectWrite.md)| The updated UserProject resource | [optional] 

### Return type

[**UserProjectRead**](UserProjectRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv

