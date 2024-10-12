# BrowshotApi.InstanceApi

All URIs are relative to *https://api.browshot.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getInstanceInfo**](InstanceApi.md#getInstanceInfo) | **GET** /instance/info | Get information about an instance
[**getInstancesInfo**](InstanceApi.md#getInstancesInfo) | **GET** /instance/list | Get all instances



## getInstanceInfo

> Instance getInstanceInfo(id)

Get information about an instance

Get information about an instance.

### Example

```javascript
import BrowshotApi from 'browshot_api';
let defaultClient = BrowshotApi.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';

let apiInstance = new BrowshotApi.InstanceApi();
let id = 56; // Number | instance ID
apiInstance.getInstanceInfo(id, (error, data, response) => {
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
 **id** | **Number**| instance ID | 

### Return type

[**Instance**](Instance.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInstancesInfo

> InstanceList getInstancesInfo()

Get all instances

Get all instances.

### Example

```javascript
import BrowshotApi from 'browshot_api';
let defaultClient = BrowshotApi.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';

let apiInstance = new BrowshotApi.InstanceApi();
apiInstance.getInstancesInfo((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**InstanceList**](InstanceList.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

