# BlockchainManagementClient.SkuApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**skusList**](SkuApi.md#skusList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Blockchain/skus | 



## skusList

> ResourceTypeSkuCollection skusList(apiVersion, subscriptionId)



Lists the Skus of the resource type.

### Example

```javascript
import BlockchainManagementClient from 'blockchain_management_client';
let defaultClient = BlockchainManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlockchainManagementClient.SkuApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
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
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | 

### Return type

[**ResourceTypeSkuCollection**](ResourceTypeSkuCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

