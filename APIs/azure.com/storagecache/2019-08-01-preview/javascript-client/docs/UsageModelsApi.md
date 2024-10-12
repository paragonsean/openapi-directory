# StorageCacheMgmtClient.UsageModelsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usageModelsList**](UsageModelsApi.md#usageModelsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.StorageCache/usageModels | 



## usageModelsList

> UsageModelsResult usageModelsList(apiVersion, subscriptionId)



Get the list of cache Usage Models available to this subscription.

### Example

```javascript
import StorageCacheMgmtClient from 'storage_cache_mgmt_client';
let defaultClient = StorageCacheMgmtClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageCacheMgmtClient.UsageModelsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.usageModelsList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**UsageModelsResult**](UsageModelsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

