# BlockchainManagementClient.BlockchainMemberOperationResultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blockchainMemberOperationResultsGet**](BlockchainMemberOperationResultApi.md#blockchainMemberOperationResultsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Blockchain/locations/{locationName}/blockchainMemberOperationResults/{operationId} | 



## blockchainMemberOperationResultsGet

> OperationResult blockchainMemberOperationResultsGet(locationName, operationId, apiVersion, subscriptionId)



Get Async operation result.

### Example

```javascript
import BlockchainManagementClient from 'blockchain_management_client';
let defaultClient = BlockchainManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlockchainManagementClient.BlockchainMemberOperationResultApi();
let locationName = "locationName_example"; // String | Location name.
let operationId = "operationId_example"; // String | Operation Id.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
apiInstance.blockchainMemberOperationResultsGet(locationName, operationId, apiVersion, subscriptionId, (error, data, response) => {
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
 **locationName** | **String**| Location name. | 
 **operationId** | **String**| Operation Id. | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | 

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

