# AzureAppConfiguration.LocksApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteLock**](LocksApi.md#deleteLock) | **DELETE** /locks/{key} | Unlocks a key-value.
[**putLock**](LocksApi.md#putLock) | **PUT** /locks/{key} | Locks a key-value.



## deleteLock

> KeyValue deleteLock(key, apiVersion, opts)

Unlocks a key-value.

### Example

```javascript
import AzureAppConfiguration from 'azure_app_configuration';

let apiInstance = new AzureAppConfiguration.LocksApi();
let key = "key_example"; // String | The key of the key-value to unlock.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let opts = {
  'label': "label_example", // String | The label, if any, of the key-value to unlock.
  'syncToken': "syncToken_example", // String | Used to guarantee real-time consistency between requests.
  'ifMatch': "ifMatch_example", // String | Used to perform an operation only if the targeted resource's etag matches the value provided.
  'ifNoneMatch': "ifNoneMatch_example" // String | Used to perform an operation only if the targeted resource's etag does not match the value provided.
};
apiInstance.deleteLock(key, apiVersion, opts, (error, data, response) => {
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
 **key** | **String**| The key of the key-value to unlock. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **label** | **String**| The label, if any, of the key-value to unlock. | [optional] 
 **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] 
 **ifMatch** | **String**| Used to perform an operation only if the targeted resource&#39;s etag matches the value provided. | [optional] 
 **ifNoneMatch** | **String**| Used to perform an operation only if the targeted resource&#39;s etag does not match the value provided. | [optional] 

### Return type

[**KeyValue**](KeyValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.microsoft.appconfig.kv+json, application/json, application/problem+json


## putLock

> KeyValue putLock(key, apiVersion, opts)

Locks a key-value.

### Example

```javascript
import AzureAppConfiguration from 'azure_app_configuration';

let apiInstance = new AzureAppConfiguration.LocksApi();
let key = "key_example"; // String | The key of the key-value to lock.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let opts = {
  'label': "label_example", // String | The label, if any, of the key-value to lock.
  'syncToken': "syncToken_example", // String | Used to guarantee real-time consistency between requests.
  'ifMatch': "ifMatch_example", // String | Used to perform an operation only if the targeted resource's etag matches the value provided.
  'ifNoneMatch': "ifNoneMatch_example" // String | Used to perform an operation only if the targeted resource's etag does not match the value provided.
};
apiInstance.putLock(key, apiVersion, opts, (error, data, response) => {
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
 **key** | **String**| The key of the key-value to lock. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **label** | **String**| The label, if any, of the key-value to lock. | [optional] 
 **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] 
 **ifMatch** | **String**| Used to perform an operation only if the targeted resource&#39;s etag matches the value provided. | [optional] 
 **ifNoneMatch** | **String**| Used to perform an operation only if the targeted resource&#39;s etag does not match the value provided. | [optional] 

### Return type

[**KeyValue**](KeyValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.microsoft.appconfig.kv+json, application/json, application/problem+json

