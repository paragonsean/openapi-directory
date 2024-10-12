# AzureAppConfiguration.KeysApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkKeys**](KeysApi.md#checkKeys) | **HEAD** /keys | Requests the headers and status of the given resource.
[**getKeys**](KeysApi.md#getKeys) | **GET** /keys | Gets a list of keys.



## checkKeys

> checkKeys(apiVersion, opts)

Requests the headers and status of the given resource.

### Example

```javascript
import AzureAppConfiguration from 'azure_app_configuration';

let apiInstance = new AzureAppConfiguration.KeysApi();
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let opts = {
  'name': "name_example", // String | A filter for the name of the returned keys.
  'syncToken': "syncToken_example", // String | Used to guarantee real-time consistency between requests.
  'after': "after_example", // String | Instructs the server to return elements that appear after the element referred to by the specified token.
  'acceptDatetime': "acceptDatetime_example" // String | Requests the server to respond with the state of the resource at the specified time.
};
apiInstance.checkKeys(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **name** | **String**| A filter for the name of the returned keys. | [optional] 
 **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] 
 **after** | **String**| Instructs the server to return elements that appear after the element referred to by the specified token. | [optional] 
 **acceptDatetime** | **String**| Requests the server to respond with the state of the resource at the specified time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getKeys

> KeyListResult getKeys(apiVersion, opts)

Gets a list of keys.

### Example

```javascript
import AzureAppConfiguration from 'azure_app_configuration';

let apiInstance = new AzureAppConfiguration.KeysApi();
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let opts = {
  'name': "name_example", // String | A filter for the name of the returned keys.
  'syncToken': "syncToken_example", // String | Used to guarantee real-time consistency between requests.
  'after': "after_example", // String | Instructs the server to return elements that appear after the element referred to by the specified token.
  'acceptDatetime': "acceptDatetime_example" // String | Requests the server to respond with the state of the resource at the specified time.
};
apiInstance.getKeys(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **name** | **String**| A filter for the name of the returned keys. | [optional] 
 **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] 
 **after** | **String**| Instructs the server to return elements that appear after the element referred to by the specified token. | [optional] 
 **acceptDatetime** | **String**| Requests the server to respond with the state of the resource at the specified time. | [optional] 

### Return type

[**KeyListResult**](KeyListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.microsoft.appconfig.keyset+json, application/json, application/problem+json

