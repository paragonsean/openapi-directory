# ApiManagementClient.TenantConfigurationSyncStateApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenantConfigurationGetSyncState**](TenantConfigurationSyncStateApi.md#tenantConfigurationGetSyncState) | **GET** /tenant/{configurationName}/syncState | 



## tenantConfigurationGetSyncState

> TenantConfigurationSyncStateContract tenantConfigurationGetSyncState(apiVersion, configurationName)



Gets the status of the most recent synchronization between the configuration database and the Git repository.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.TenantConfigurationSyncStateApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let configurationName = "configurationName_example"; // String | The identifier of the Git Configuration Operation.
apiInstance.tenantConfigurationGetSyncState(apiVersion, configurationName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **configurationName** | **String**| The identifier of the Git Configuration Operation. | 

### Return type

[**TenantConfigurationSyncStateContract**](TenantConfigurationSyncStateContract.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

