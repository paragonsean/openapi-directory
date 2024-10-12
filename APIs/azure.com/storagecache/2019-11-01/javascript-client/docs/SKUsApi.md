# StorageCacheMgmtClient.SKUsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**skusList**](SKUsApi.md#skusList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.StorageCache/skus | 



## skusList

> ResourceSkusResult skusList(apiVersion, subscriptionId)



Get the list of StorageCache.Cache SKUs available to this subscription.

### Example

```javascript
import StorageCacheMgmtClient from 'storage_cache_mgmt_client';
let defaultClient = StorageCacheMgmtClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageCacheMgmtClient.SKUsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.skusList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ResourceSkusResult**](ResourceSkusResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

