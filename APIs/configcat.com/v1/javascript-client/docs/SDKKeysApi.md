# ConfigCatPublicManagementApi.SDKKeysApi

All URIs are relative to *https://api.configcat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSdkKeys**](SDKKeysApi.md#getSdkKeys) | **GET** /v1/configs/{configId}/environments/{environmentId} | Get SDK Key



## getSdkKeys

> SdkKeysModel getSdkKeys(configId, environmentId)

Get SDK Key

This endpoint returns the SDK Key for your Config in a specified Environment.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.SDKKeysApi();
let configId = "configId_example"; // String | The identifier of the Config.
let environmentId = "environmentId_example"; // String | The identifier of the Environment.
apiInstance.getSdkKeys(configId, environmentId, (error, data, response) => {
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
 **configId** | **String**| The identifier of the Config. | 
 **environmentId** | **String**| The identifier of the Environment. | 

### Return type

[**SdkKeysModel**](SdkKeysModel.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json

