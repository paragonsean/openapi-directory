# MicrosoftStorageSync.OperationStatusApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationStatusGet**](OperationStatusApi.md#operationStatusGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/locations/{locationName}/workflows/{workflowId}/operations/{operationId} | 



## operationStatusGet

> OperationStatus operationStatusGet(subscriptionId, resourceGroupName, apiVersion, locationName, workflowId, operationId)



Get Operation status

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.OperationStatusApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let locationName = "locationName_example"; // String | The desired region to obtain information from.
let workflowId = "workflowId_example"; // String | workflow Id
let operationId = "operationId_example"; // String | operation Id
apiInstance.operationStatusGet(subscriptionId, resourceGroupName, apiVersion, locationName, workflowId, operationId, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **locationName** | **String**| The desired region to obtain information from. | 
 **workflowId** | **String**| workflow Id | 
 **operationId** | **String**| operation Id | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

