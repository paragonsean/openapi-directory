# StorageManagementClient.GCApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**farmsGetGarbageCollectionState**](GCApi.md#farmsGetGarbageCollectionState) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/operationresults/{operationId} | 



## farmsGetGarbageCollectionState

> String farmsGetGarbageCollectionState(subscriptionId, resourceGroupName, farmId, apiVersion, operationId)



Returns the state of the garbage collection job.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.GCApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let farmId = "farmId_example"; // String | Farm Id.
let apiVersion = "apiVersion_example"; // String | REST Api Version.
let operationId = "operationId_example"; // String | Operation Id.
apiInstance.farmsGetGarbageCollectionState(subscriptionId, resourceGroupName, farmId, apiVersion, operationId, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **farmId** | **String**| Farm Id. | 
 **apiVersion** | **String**| REST Api Version. | 
 **operationId** | **String**| Operation Id. | 

### Return type

**String**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

