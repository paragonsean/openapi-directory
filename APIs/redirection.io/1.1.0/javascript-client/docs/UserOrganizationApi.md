# RedirectionIo.UserOrganizationApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteUserOrganizationItem**](UserOrganizationApi.md#deleteUserOrganizationItem) | **DELETE** /user-organizations/{id} | Removes the UserOrganization resource.
[**getUserOrganizationItem**](UserOrganizationApi.md#getUserOrganizationItem) | **GET** /user-organizations/{id} | Retrieves a UserOrganization resource.
[**postUserOrganizationCollection**](UserOrganizationApi.md#postUserOrganizationCollection) | **POST** /user-organizations | Creates a UserOrganization resource.
[**putUserOrganizationItem**](UserOrganizationApi.md#putUserOrganizationItem) | **PUT** /user-organizations/{id} | Replaces the UserOrganization resource.



## deleteUserOrganizationItem

> deleteUserOrganizationItem(id)

Removes the UserOrganization resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.UserOrganizationApi();
let id = "id_example"; // String | 
apiInstance.deleteUserOrganizationItem(id, (error, data, response) => {
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


## getUserOrganizationItem

> UserOrganizationRead getUserOrganizationItem(id)

Retrieves a UserOrganization resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.UserOrganizationApi();
let id = "id_example"; // String | 
apiInstance.getUserOrganizationItem(id, (error, data, response) => {
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

[**UserOrganizationRead**](UserOrganizationRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## postUserOrganizationCollection

> UserOrganizationRead postUserOrganizationCollection(opts)

Creates a UserOrganization resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.UserOrganizationApi();
let opts = {
  'userOrganization': new RedirectionIo.UserOrganizationCreationWrite() // UserOrganizationCreationWrite | The new UserOrganization resource
};
apiInstance.postUserOrganizationCollection(opts, (error, data, response) => {
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
 **userOrganization** | [**UserOrganizationCreationWrite**](UserOrganizationCreationWrite.md)| The new UserOrganization resource | [optional] 

### Return type

[**UserOrganizationRead**](UserOrganizationRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv


## putUserOrganizationItem

> UserOrganizationRead putUserOrganizationItem(id, opts)

Replaces the UserOrganization resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.UserOrganizationApi();
let id = "id_example"; // String | 
let opts = {
  'userOrganization': new RedirectionIo.UserOrganizationWrite() // UserOrganizationWrite | The updated UserOrganization resource
};
apiInstance.putUserOrganizationItem(id, opts, (error, data, response) => {
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
 **userOrganization** | [**UserOrganizationWrite**](UserOrganizationWrite.md)| The updated UserOrganization resource | [optional] 

### Return type

[**UserOrganizationRead**](UserOrganizationRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv

